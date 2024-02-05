import pandas as pd
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from datetime import datetime


class AppLacon():
    def lacon(self):
        try:
            #self.df = pd.read_excel('exemplos\exemplo lacon.xlsx', header=[2])
            self.df.columns = self.df.iloc[1, :]
            print("---------------------------------LACON--------------------------------")
            print(self.df)
            print(self.data_dict)

            if 'CONFERIDO' in self.df.columns:
                try:
                    self.df = self.df.loc[self.df['CONFERIDO'] == 'OK']
                except:
                    print("Erro")

            self.df = self.df.reset_index(drop=False)
            print(self.df)

            self.txt = ''
            txtM = ''
            contador = 0
            meu_dict = {}

            imoveis_sem_contrato = []  # Lista para armazenar imóveis sem contrato
            imoveis_com_data_faltando = []  # Lista para armazenar imóveis com data faltando

            for i, controlador in enumerate(self.df['AGIR']):
                cpf_cnpj = ""
                data_timestamp = self.df.loc[i,'Data\nPag.\nExtrato']
                print(" -----------------------", i ,"-------------------------")
                data_str = data_timestamp.strftime("%d/%m/%Y")
                data_data = datetime.strptime(data_str, "%d/%m/%Y")
                data_txt = f"{data_data:%Y%m%d}"
                competencia_timestamp = self.df.loc[i,'Mês/\nRef.']
                competencia_str = competencia_timestamp.strftime("%d/%m/%Y")
                competencia_competencia = datetime.strptime(competencia_str, "%d/%m/%Y")
                competencia_txt = f"{competencia_competencia:%m%Y}"

                ValoresSimples = ['simples', 'Simples', 'SIMPLES']
                banco = "1591"
                bancoValor = round(self.df.loc[i,'Receita\nBruta\n(Extrato)'],2)
                contSimples = 0
                lancarBancoSimples = 0
                lanSim = ''

                imovel = self.df.loc[i, 'Imóvel']
                aluguel = abs(self.df.loc[i,'Aluguel'])
                aluguelConta = "16"
                condominio = abs(self.df.loc[i,'Condomínio'])
                condominioConta = "1324"		
                iptu = abs(self.df.loc[i,'IPTU'])
                iptuConta = "1327"		
                bombeiro = abs(self.df.loc[i,'Bombeiro'])
                bombeiroConta = "1334"		
                spu = abs(self.df.loc[i,'SPU'])
                spuConta = "1332"		
                taxaExtra = abs(self.df.loc[i,'Taxa Extra'])
                taxaExtraConta = "1324"
                agua = abs(self.df.loc[i,'Água'])
                aguaConta = "1323"
                multaJuros = abs(self.df.loc[i,'Multa/Juros'])
                multaJurosConta = "296"
                desconto = abs(self.df.loc[i,'Desconto'])
                descontoConta = "564"	
                seguro = abs(self.df.loc[i,'Seguro'])		
                seguroConta = "1330"
                cercaEletrica = abs(self.df.loc[i,'Cerca Elétrica'])
                cercaEletricaConta = "2061"
                outrosGastos = abs(self.df.loc[i,'Outros Gastos'])
                outrosGastosConta = "2061"            

                imoveis_sem_contrato_temp = []  # Lista para armazenar imóveis sem contrato          

                if aluguel > 0:
                    for chave, valor in self.data_dict.items():
                        if valor.get('01-imovel') == imovel:
                            inicio = valor.get('05-inicio')
                            fim = valor.get('06-fim')
                            
                            if fim == 'indeterminado':
                                fim = datetime.now().strftime("%d/%m/%Y")  # Use a data atual como o fim se for 'indeterminado'
                            
                            # Trate o caso em que '05-inicio' ou '06-fim' são vazios
                            if inicio and fim:
                                inicio_data = datetime.strptime(inicio, "%d/%m/%Y")
                                fim_data = datetime.strptime(fim, "%d/%m/%Y")
                                competencia_data = datetime.strptime(competencia_str, "%d/%m/%Y")
                                competencia_data_formatada = competencia_data.strftime("%d/%m/%Y")

                                if inicio_data <= competencia_data <= fim_data:
                                    print(f'A competência {competencia_data} está dentro do intervalo para a entrada {chave}')
                                    cpf_cnpj = valor.get('03-cpf-cnpj')
                                    print(f'O CPF/CNPJ correspondente a {imovel}: {cpf_cnpj}')
                                    imoveis_sem_contrato_temp = []
                                else:
                                    print(f'A competência não está no intervalo do contrato imóvel {imovel}')
                                    imoveis_sem_contrato_temp.append((imovel, competencia_data_formatada))  # Adicione o imóvel e a competência à lista
                            else:
                                imoveis_com_data_faltando.append((imovel, competencia_data_formatada))  # Adicione o imóvel e a competência à lista
                    
                    if imoveis_sem_contrato_temp:
                        for imovel, competencia_data in imoveis_sem_contrato_temp:
                            imoveis_sem_contrato.append((imovel, competencia_data))
                
                if controlador in ValoresSimples:
                    valoresSimplesContador = [aluguel, condominio, iptu, bombeiro, spu, taxaExtra, agua, multaJuros, desconto, seguro, cercaEletrica, outrosGastos]
                    
                    for valor in valoresSimplesContador:
                        if valor > 0:
                            contSimples += 1
                    
                    if contSimples > 1:
                        bancoSimples = 0
                        lancarBancoSimples = 1
                        contSimples = 1
                    else:
                        bancoSimples = banco
            
                    if aluguel > 0:
                        lanSim += str('{:06d}'.format(contSimples)) +"," + str(data_txt) + ","+str(aluguelConta)+","+str(bancoSimples)+"," + str(aluguel) + ",00000000," + "Recebimento de Aluguel do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",," + str(cpf_cnpj) + "," + "\n"
                        contSimples += 1
                        
                    if condominio > 0:
                        lanSim += str('{:06d}'.format(contSimples)) +"," + str(data_txt) + ",0,"+str(condominioConta)+"," + str(condominio) + ",00000000," + "Recuperação de condominio do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
                        contSimples += 1
                        
                    if iptu > 0:
                        lanSim += str('{:06d}'.format(contSimples)) +"," + str(data_txt) + ",0,"+str(iptuConta)+"," + str(iptu) + ",00000000," + "Recuperação de IPTU do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
                        contSimples += 1
                        
                    if bombeiro > 0:
                        lanSim += str('{:06d}'.format(contSimples)) +"," + str(data_txt) + ",0,"+str(bombeiroConta)+"," + str(bombeiro) + ",00000000," + "Recuperação da taxa do bombeiro do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
                        contSimples += 1
                        
                    if spu > 0:
                        lanSim += str('{:06d}'.format(contSimples)) +"," + str(data_txt) + ",0,"+str(spuConta)+"," + str(spu) + ",00000000," + "Recuperação de SPU do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
                        contSimples += 1
                        
                    if taxaExtra > 0:
                        lanSim += str('{:06d}'.format(contSimples)) +"," + str(data_txt) + ",0,"+str(taxaExtraConta)+"," + str(taxaExtra) + ",00000000," + "Recuperação de Taxas Extras do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
                        contSimples += 1
                        
                    if agua > 0:
                        lanSim += str('{:06d}'.format(contSimples)) +"," + str(data_txt) + ",0,"+str(aguaConta)+"," + str(agua) + ",00000000," + "Recuperação de Agua e Esgoto do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
                        contSimples += 1
                        
                    if multaJuros > 0:
                        lanSim += str('{:06d}'.format(contSimples)) +"," + str(data_txt) + ",0,"+str(multaJurosConta)+"," + str(multaJuros) + ",00000000," + "Valor Referente a Multas e Jutos do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
                        contSimples += 1
                        
                    if desconto > 0:
                        lanSim += str('{:06d}'.format(contSimples)) +"," + str(data_txt) + ","+str(descontoConta)+",0," + str(desconto) + ",00000000," + "Valor Referente a Desconto do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
                        contSimples += 1

                    if seguro > 0:
                        lanSim += str('{:06d}'.format(contSimples)) +"," + str(data_txt) + ",0,"+str(seguroConta)+"," + str(seguro) + ",00000000," + "Recuperação de Seguros do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
                        contSimples += 1
                        
                    if cercaEletrica > 0:
                        lanSim += str('{:06d}'.format(contSimples)) +"," + str(data_txt) + ",0,"+str(cercaEletricaConta)+"," + str(cercaEletrica) + ",00000000," + "Recuperação de Cerca Eletrica do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
                        contSimples += 1
                        
                    if outrosGastos > 0:
                        lanSim += str('{:06d}'.format(contSimples)) +"," + str(data_txt) + ",0,"+str(outrosGastosConta)+"," + str(outrosGastos) + ",00000000," + "Recuperação de Gastos no Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
                        contSimples += 1

                    if lancarBancoSimples == 1:
                        lanSim += str('{:06d}'.format(contSimples)) +"," + str(data_txt) + ","+str(banco)+",0," + str(bancoValor) + ",00000000," + "Recebimento do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"

                    self.txt += lanSim

                else:
                    MultVerificação = str(self.df.loc[i,'AGIR']) + str(self.df.loc[i,'Data\nPag.\nExtrato'])
                    print("MultVerificação", MultVerificação)
                    try:
                        contador = meu_dict[MultVerificação][1]
                        valorSoma = float(meu_dict[MultVerificação][0])
                    except:    
                        contador = 1
                        valorSoma = 0.0
                    lanMult = ''

                    if aluguel > 0:
                        lanMult += str('{:06d}'.format(contador)) +"," + str(data_txt) + ","+str(aluguelConta)+",0," + str(aluguel) + ",00000000," + "Recebimento de Aluguel do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",," + str(cpf_cnpj) + "," + "\n"
                        contador += 1
                        
                    if condominio > 0:
                        lanMult += str('{:06d}'.format(contador)) +"," + str(data_txt) + ",0,"+str(condominioConta)+"," + str(condominio) + ",00000000," + "Recuperação de condominio do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
                        contador += 1
                        
                    if iptu > 0:
                        lanMult += str('{:06d}'.format(contador)) +"," + str(data_txt) + ",0,"+str(iptuConta)+"," + str(iptu) + ",00000000," + "Recuperação de IPTU do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
                        contador += 1
                        
                    if bombeiro > 0:
                        lanMult += str('{:06d}'.format(contador)) +"," + str(data_txt) + ",0,"+str(bombeiroConta)+"," + str(bombeiro) + ",00000000," + "Recuperação da taxa do bombeiro do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
                        contador += 1
                        
                    if spu > 0:
                        lanMult += str('{:06d}'.format(contador)) +"," + str(data_txt) + ",0,"+str(spuConta)+"," + str(spu) + ",00000000," + "Recuperação de SPU do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
                        contador += 1
                        
                    if taxaExtra > 0:
                        lanMult += str('{:06d}'.format(contador)) +"," + str(data_txt) + ",0,"+str(taxaExtraConta)+"," + str(taxaExtra) + ",00000000," + "Recuperação de Taxas Extras do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
                        contador += 1
                        
                    if agua > 0:
                        lanMult += str('{:06d}'.format(contador)) +"," + str(data_txt) + ",0,"+str(aguaConta)+"," + str(agua) + ",00000000," + "Recuperação de Agua e Esgoto do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
                        contador += 1
                        
                    if multaJuros > 0:
                        lanMult += str('{:06d}'.format(contador)) +"," + str(data_txt) + ",0,"+str(multaJurosConta)+"," + str(multaJuros) + ",00000000," + "Valor Referente a Multas e Jutos do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
                        contador += 1
                        
                    if desconto > 0:
                        lanMult += str('{:06d}'.format(contador)) +"," + str(data_txt) + ","+str(descontoConta)+",0," + str(desconto) + ",00000000," + "Valor Referente a Desconto do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
                        contador += 1

                    if seguro > 0:
                        lanMult += str('{:06d}'.format(contador)) +"," + str(data_txt) + ",0,"+str(seguroConta)+"," + str(seguro) + ",00000000," + "Recuperação de Seguros do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
                        contador += 1
                        
                    if cercaEletrica > 0:
                        lanMult += str('{:06d}'.format(contador)) +"," + str(data_txt) + ",0,"+str(cercaEletricaConta)+"," + str(cercaEletrica) + ",00000000," + "Recuperação de Cerca Eletrica do Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
                        contador += 1
                        
                    if outrosGastos > 0:
                        lanMult += str('{:06d}'.format(contador)) +"," + str(data_txt) + ",0,"+str(outrosGastosConta)+"," + str(outrosGastos) + ",00000000," + "Recuperação de Gastos no Imóvel: " + str(imovel) + "/Ref:" + str(competencia_txt) + ",,," + "\n"
                        contador += 1

                    self.txt += lanMult
                    valorSoma = valorSoma + float(bancoValor)
                    meu_dict[MultVerificação] = [valorSoma,contador,banco,data_txt]


            for chave, valor in meu_dict.items():
                valorSoma, contador, banco, data_txt = valor
                lanMultFinal = str('{:06d}'.format(contador)) +"," + str(data_txt) + ","+str(banco)+",0," + str(round(valorSoma,2)) + ",00000000," + "Recebimento diversos" + ",,," + "\n"
                self.txt += lanMultFinal

            if imoveis_sem_contrato:
                # Exibir mensagem apenas se houver imóveis sem contrato
                mensagem = 'Competência fora do período contratual para os seguintes imóveis:\n\n'
                for imovel, competencia_data in imoveis_sem_contrato:
                    mensagem += f'Imóvel: {imovel}, Competência: {competencia_data}\n'
                mensagem += '\nVerifique para evitar erros na importação. Após isso, reiniciar o processo de importação do Excel.\n\n'
                QMessageBox.warning(self, 'Competência sem contrato.', mensagem)

            if imoveis_com_data_faltando:
                # Exibir mensagem apenas se houver imóveis sem contrato
                mensagem = 'Data não preenchidos no contrato para os seguintes imóveis:\n\n'
                for imovel, competencia_data in imoveis_com_data_faltando:
                    mensagem += f'Imóvel: {imovel}, Competência: {competencia_data}\n'
                mensagem += '\nVerifique para evitar erros na importação. Após isso, reiniciar o processo de importação do Excel.\n\n'  
                QMessageBox.warning(self, 'Competência sem contrato.', mensagem)

            print(meu_dict)
            print(self.txt)
        except KeyError as erro:
            QMessageBox.warning(self, 'KeyError', 'Não foi localizado a coluna: '+ str(erro))
        except ValueError as erro:
            QMessageBox.warning(self, 'ValueError', 'Valor Error: '+ str(erro))                   
        except Exception as erro:
            QMessageBox.warning(self, 'Error', 'Erro ao tentar carregar o aquivo. - '+ str(erro))    