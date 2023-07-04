import sys
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import pandas as pd
from datetime import datetime

class AppEaj():
    def eaj(self):       
        try:
            self.txt = ''
            self.txtM = ''
            contador = 0
            meu_dict = {}
            for i, controlador in enumerate (self.df['AGIR']):
                data_timestamp = self.df.loc[i,'Data de Crédito ou Débito (No Extrato)']
                data_str = data_timestamp.strftime("%Y-%m-%d %H:%M:%S")
                data_data = datetime.strptime(data_str, "%Y-%m-%d %H:%M:%S")
                data_txt = f"{data_data:%Y%m%d}"
                cpfoucnpj = self.df.loc[i,'CNPJ/CPF']
                cpfoucnpj = cpfoucnpj.replace('.','').replace('/','').replace('-','')
                ValoresSimples = ['simples','Simples']
                banco = self.df.loc[i,'Conta Corrente']
                if banco == 'Itaú Unibanco':
                    bancoConta = '1597'
                elif banco == 'Caixinha':
                    bancoConta = '5'
                elif banco == 'Caixa Econômica Federal 777-1':
                    bancoConta = '1577'
                else:
                    bancoConta = '5'

                if controlador in ValoresSimples:
                    if int(self.df.loc[i,'Juros']) > 0 or int(self.df.loc[i,'Desconto']) > 0 or int(self.df.loc[i,'Multa']) > 0:
                        lanMult = "000001," + str(data_txt) + ","+ bancoConta + ",0," + str(self.df.loc[i,'Recebido']) + ",00000000," + "Valor Recebido " + str(self.df.loc[i,'Projeto']) + " " + str(self.df.loc[i,'Nota Fiscal']) + " Parcela "+ str(self.df.loc[i,'Parcela']) + " - " + str(self.df.loc[i,'Cliente']) + ",,," + "\n"
                        lanMult += "000002," + str(data_txt) + ",0," + "16," + str(self.df.loc[i,'Recebido']-self.df.loc[i,'Juros']-self.df.loc[i,'Multa']+self.df.loc[i,'Desconto']) + ",00000000," + "Valor Recebido " + str(self.df.loc[i,'Projeto']) + " " + str(self.df.loc[i,'Nota Fiscal']) + " Parcela "+ str(self.df.loc[i,'Parcela']) + " - " + str(self.df.loc[i,'Cliente']) + ",,"+ cpfoucnpj + "," + "\n"
                        if int(self.df.loc[i,'Juros']) > 0:
                            lanMult += "000003," + str(data_txt) + ",0" + ",296," + str(self.df.loc[i,'Juros']) + ",00000000," + "Juros s/valor Recebido " + str(self.df.loc[i,'Projeto']) + " " + str(self.df.loc[i,'Nota Fiscal']) + " Parcela "+ str(self.df.loc[i,'Parcela']) + " - " + str(self.df.loc[i,'Cliente']) + ",,," + "\n"
                        if int(self.df.loc[i,'Multa']) > 0:
                            lanMult += "000003," + str(data_txt) + ",1469" + ",0," + str(self.df.loc[i,'Multa']) + ",00000000," + "Multa s/valor Recebido " + str(self.df.loc[i,'Projeto']) + " " + str(self.df.loc[i,'Nota Fiscal']) + " Parcela "+ str(self.df.loc[i,'Parcela']) + " - " + str(self.df.loc[i,'Cliente']) + ",,," + "\n"
                        if int(self.df.loc[i,'Desconto']) > 0:
                            lanMult += "000003," + str(data_txt) + ",0," + "564," + str(self.df.loc[i,'Desconto']) + ",00000000," + "Desconto s/valor Recebido " + str(self.df.loc[i,'Projeto']) + " " + str(self.df.loc[i,'Nota Fiscal']) + " Parcela "+ str(self.df.loc[i,'Parcela']) + " - " + str(self.df.loc[i,'Cliente']) + ",,," + "\n"
                        self.txt += str(lanMult)
                    else:
                        lanSimp = "000001," + str(data_txt) + ","+ bancoConta + "," + "16," + str(self.df.loc[i,'Recebido']) + ",00000000," + "Valor Recebido " + str(self.df.loc[i,'Projeto']) + " " + str(self.df.loc[i,'Nota Fiscal']) + " Parcela "+ str(self.df.loc[i,'Parcela']) + " - " + str(self.df.loc[i,'Cliente']) + ",,"+ cpfoucnpj + "," + "\n"       
                        self.txt += str(lanSimp)
                else:
                    MultVerificação = str(self.df.loc[i,'AGIR']) + str(self.df.loc[i,'Data de Crédito ou Débito (No Extrato)'])
                    try:
                        self.txtM = meu_dict[MultVerificação][0]
                        contador = meu_dict[MultVerificação][2]
                        valorSoma = float(meu_dict[MultVerificação][1])
                        if float(self.df.loc[i,'Juros']) > 0 or float(self.df.loc[i,'Desconto']) > 0 or float(self.df.loc[i,'Multa']) > 0:
                            contador = contador+1
                            lanMult = str('{:06d}'.format(contador)) +","+ str(data_txt) + ",0," + "16," + str(self.df.loc[i,'Recebido']-self.df.loc[i,'Juros']-self.df.loc[i,'Multa']+self.df.loc[i,'Desconto']) + ",00000000," + "Valor Recebido " + str(self.df.loc[i,'Projeto']) + " " + str(self.df.loc[i,'Nota Fiscal']) + " Parcela "+ str(self.df.loc[i,'Parcela']) + " - " + str(self.df.loc[i,'Cliente']) + ",,"+ cpfoucnpj + "," + "\n"
                            if float(self.df.loc[i,'Juros']) > 0:
                                contador = contador+1
                                lanMult += str('{:06d}'.format(contador)) +","+ str(data_txt) + ",0" + ",296," + str(self.df.loc[i,'Juros']) + ",00000000," + "Juros s/valor Recebido " + str(self.df.loc[i,'Projeto']) + " " + str(self.df.loc[i,'Nota Fiscal']) + " Parcela "+ str(self.df.loc[i,'Parcela']) + " - " + str(self.df.loc[i,'Cliente']) + ",,," + "\n"
                            if float(self.df.loc[i,'Multa']) > 0:
                                contador = contador+1
                                lanMult += str('{:06d}'.format(contador)) +","+ str(data_txt) + ",1469" + ",0," + str(self.df.loc[i,'Multa']) + ",00000000," + "Multa s/valor Recebido " + str(self.df.loc[i,'Projeto']) + " " + str(self.df.loc[i,'Nota Fiscal']) + " Parcela "+ str(self.df.loc[i,'Parcela']) + " - " + str(self.df.loc[i,'Cliente']) + ",,," + "\n"
                            if float(self.df.loc[i,'Desconto']) > 0:
                                contador = contador+1
                                lanMult += str('{:06d}'.format(contador)) +","+ str(data_txt) + ",0," + "564," + str(self.df.loc[i,'Desconto']) + ",00000000," + "Desconto s/valor Recebido " + str(self.df.loc[i,'Projeto']) + " " + str(self.df.loc[i,'Nota Fiscal']) + " Parcela "+ str(self.df.loc[i,'Parcela']) + " - " + str(self.df.loc[i,'Cliente']) + ",,," + "\n"
                            self.txtM += str(lanMult)
                            valorSoma = valorSoma + float(self.df.loc[i,'Recebido'])
                            meu_dict[MultVerificação] = [self.txtM,valorSoma,contador,bancoConta,data_txt]
                        else:
                            contador = contador+1
                            lanSimp = str('{:06d}'.format(contador)) +","+ str(data_txt) + ",0," + "16," + str(self.df.loc[i,'Recebido']) + ",00000000," + "Valor Recebido " + str(self.df.loc[i,'Projeto']) + " " + str(self.df.loc[i,'Nota Fiscal']) + " Parcela "+ str(self.df.loc[i,'Parcela']) + " - " + str(self.df.loc[i,'Cliente']) + ",,"+ cpfoucnpj + "," + "\n"         
                            self.txtM += str(lanSimp)
                            valorSoma = valorSoma + float(self.df.loc[i,'Recebido'])
                            meu_dict[MultVerificação] = [self.txtM,valorSoma,contador,bancoConta,data_txt]
                    except:
                        self.txtM = ''
                        contador = 0
                        valorSoma = 0.0
                        if float(self.df.loc[i,'Juros']) > 0 or float(self.df.loc[i,'Desconto']) > 0 or float(self.df.loc[i,'Multa']) > 0:
                            contador = contador+1
                            lanMult = str('{:06d}'.format(contador)) +","+ str(data_txt) + ",0," + "16," + str(self.df.loc[i,'Recebido']-self.df.loc[i,'Juros']-self.df.loc[i,'Multa']+self.df.loc[i,'Desconto']) + ",00000000," + "Valor Recebido " + str(self.df.loc[i,'Projeto']) + " " + str(self.df.loc[i,'Nota Fiscal']) + " Parcela "+ str(self.df.loc[i,'Parcela']) + " - " + str(self.df.loc[i,'Cliente']) + ",,"+ cpfoucnpj + "," + "\n"
                            if float(self.df.loc[i,'Juros']) > 0:
                                contador = contador+1
                                lanMult += str('{:06d}'.format(contador)) +","+ str(data_txt) + ",0" + ",296," + str(self.df.loc[i,'Juros']) + ",00000000," + "Juros s/valor Recebido " + str(self.df.loc[i,'Projeto']) + " " + str(self.df.loc[i,'Nota Fiscal']) + " Parcela "+ str(self.df.loc[i,'Parcela']) + " - " + str(self.df.loc[i,'Cliente']) + ",,," + "\n"
                            if float(self.df.loc[i,'Multa']) > 0:
                                contador = contador+1
                                lanMult += str('{:06d}'.format(contador)) +","+ str(data_txt) + ",1469" + ",0," + str(self.df.loc[i,'Multa']) + ",00000000," + "Multa s/valor Recebido " + str(self.df.loc[i,'Projeto']) + " " + str(self.df.loc[i,'Nota Fiscal']) + " Parcela "+ str(self.df.loc[i,'Parcela']) + " - " + str(self.df.loc[i,'Cliente']) + ",,," + "\n"
                            if float(self.df.loc[i,'Desconto']) > 0:
                                contador = contador+1
                                lanMult += str('{:06d}'.format(contador)) +","+ str(data_txt) + ",0," + "564," + str(self.df.loc[i,'Desconto']) + ",00000000," + "Desconto s/valor Recebido " + str(self.df.loc[i,'Projeto']) + " " + str(self.df.loc[i,'Nota Fiscal']) + " Parcela "+ str(self.df.loc[i,'Parcela']) + " - " + str(self.df.loc[i,'Cliente']) + ",,," + "\n"
                            self.txtM += str(lanMult)
                            valorSoma = float(self.df.loc[i,'Recebido'])
                            meu_dict[MultVerificação] = [self.txtM,valorSoma,contador,bancoConta,data_txt]
                        else:
                            contador = contador+1
                            lanSimp = str('{:06d}'.format(contador)) +","+ str(data_txt) + ",0," + "16," + str(self.df.loc[i,'Recebido']) + ",00000000," + "Valor Recebido " + str(self.df.loc[i,'Projeto']) + " " + str(self.df.loc[i,'Nota Fiscal']) + " Parcela "+ str(self.df.loc[i,'Parcela']) + " - " + str(self.df.loc[i,'Cliente']) + ",,"+ cpfoucnpj + "," + "\n"         
                            self.txtM += str(lanSimp)
                            valorSoma = float(self.df.loc[i,'Recebido'])
                            meu_dict[MultVerificação] = [self.txtM,valorSoma,contador,bancoConta,data_txt]

            for valor in meu_dict.values():
                self.txt += valor[0]
                valorNoFor = valor[1]
                contadorX =  valor[2]
                bancoNoFor = valor[3]
                data_txtX = valor[4]
                self.txt += str('{:06d}'.format(contadorX+1)) +","+ str(data_txtX) + ","+ bancoNoFor +"," + "0," + str(valorNoFor) + ",00000000," + "Valor Referente a Varios Recebimentos - Mov Tít Cob" + ",,," + "\n"
                
            print(self.txt)
            QMessageBox.warning(self, 'Info', 'Excel carregado com Sucesso')  
        except KeyError as erro:
            QMessageBox.warning(self, 'KeyError', 'Não foi localizado a coluna: '+ str(erro))
        except ValueError as erro:
            QMessageBox.warning(self, 'ValueError', 'Retire o filtor da planilha.')                   
        except Exception as erro:
            QMessageBox.warning(self, 'Error', 'Erro ao tentar carregar o aquivo. - '+ str(erro))    