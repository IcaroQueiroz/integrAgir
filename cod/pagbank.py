import pandas as pd
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from io import StringIO
import re

class AppPagBank():
    # Função para remover caracteres não numéricos e converter para float
    def convert_to_float(self, value):
        cleaned_value = str(value).replace(',', '.') # Remove tudo que não é dígito nem ponto
        try:
            return float(cleaned_value)
        except:
            return None
    
    def pagbank(self):
        try:

            data_venda = 'Data_Transacao'
            valor_venda = 'Valor_Bruto'
            valor_liquido = 'Valor_Liquido'
            bandeira = 'Bandeira_Cartao_Credito'
            modalidade = 'Tipo_Pagamento'

            self.df['Natureza'] = self.df[modalidade]
            self.df[data_venda] = pd.to_datetime(self.df[data_venda], dayfirst=True)  # Converta a coluna para o tipo de dados datetime, se ainda não estiver
            self.df[data_venda] = self.df[data_venda].dt.date  # Extraia apenas a parte da data, excluindo a hora
            self.df['DataNat'] = self.df[data_venda].astype(str) + self.df[bandeira].astype(str) + self.df['Natureza'].astype(str) # Concatene a data (sem hora) com a coluna 'Natureza'
            print("-----------------------------------NATUREZA--------------------------------------")
            print(self.df['Natureza'])

            # Converter as colunas para o tipo de dados numérico
            # Aplicar a função de conversão às colunas
            self.df[valor_venda] = self.df[valor_venda].apply(self.convert_to_float)
            self.df[valor_liquido] = self.df[valor_liquido].apply(self.convert_to_float)
            print(self.df['Status'])

            # Filtro para selecionar apenas as linhas com status "Aprovada"
            self.df_credito = self.df[self.df['Debito_Credito'] == 'Crédito']
            print("-----------------------------------df_credito--------------------------------------")
            print(self.df_credito)
            print(self.df_credito['Natureza'])

            self.df_aprovado = self.df_credito[self.df_credito['Status'] == 'Aprovada']
            print("-----------------------------------df_aprovado + 'DataNat' --------------------------------------")
            print(self.df_aprovado)
            print(self.df_aprovado['Natureza'])
            print(self.df_aprovado['DataNat'])


            # Agrupando e somando os valores
            self.df_aprovado[bandeira].fillna('Modalidade', inplace=True)
            self.df_agrupado = self.df_aprovado.groupby([data_venda, bandeira, 'Natureza', 'DataNat']).agg({valor_venda: 'sum', valor_liquido: 'sum', 'DataNat': 'count'}).rename(columns={'DataNat': 'Quantidade'}).reset_index()
            self.df_agrupado['Taxa'] = self.df_aprovado['Valor_Taxa']
            print("-----------------------------------df_agrupado + 'DataNat' --------------------------------------")
            print(self.df_agrupado)
            print(self.df_aprovado['Natureza'])
            print(self.df_aprovado['DataNat'])
            
            # Filtrar os dados relevantes
            dados_credito = self.df_agrupado[self.df_agrupado['Natureza'].str.contains('Crédito', case=False)]
            dados_debito = self.df_agrupado[self.df_agrupado['Natureza'].str.contains('Débito', case=False)]
            dados_voucher = self.df_agrupado[self.df_agrupado['Natureza'].str.contains('Voucher', case=False)]

            # Calcular os totais
            total_credito = dados_credito[valor_venda].sum()
            total_debito = dados_debito[valor_venda].sum()
            total_voucher = dados_voucher[valor_venda].sum()

            # Contar a quantidade
            quantidade_credito = dados_credito['Quantidade'].sum()
            quantidade_debito = dados_debito['Quantidade'].sum()
            quantidade_voucher = dados_voucher['Quantidade'].sum()

            # Calcular o total geral
            total_geral = total_credito + total_debito + total_voucher
            quantidade_total = quantidade_credito + quantidade_debito + quantidade_voucher

            # Imprimir o relatório
            print("Relatório de Pagamentos")
            print("Total de Crédito: R$", total_credito, "- Quantidade:", quantidade_credito)
            print("Total de Débito: R$", total_debito, "- Quantidade:", quantidade_debito)
            print("Total de Voucher: R$", total_voucher, "- Quantidade:", quantidade_voucher)
            print("Total Geral: R$", total_geral, "- Quantidade Total:", quantidade_total)

            self.relatorio = {
                'total_credito': total_credito,
                'total_debito': total_debito,
                'total_voucher': total_voucher,
                'quantidade_credito': quantidade_credito,
                'quantidade_debito': quantidade_debito,
                'quantidade_voucher': quantidade_voucher,
                'total_geral': total_geral,
                'quantidade_total': quantidade_total
            }

            self.txt = ''
            for i, controlador in enumerate (self.df_agrupado['DataNat']):
                data_str = self.df_agrupado.loc[i, data_venda]
                data_txt = f"{data_str:%Y%m%d}"
                data_nat = self.df_agrupado.loc[i,'DataNat']
                conta = ''
                cpfoucnpj = ''
                #if 'crédito' in data_nat:
                if re.search(r'crédito', data_nat, re.IGNORECASE):
                    conta_ativo = '22'
                    conta_despesa = '1423'
                    print("sim", controlador)
                #elif 'débito' in data_nat:
                elif re.search(r'débito', data_nat, re.IGNORECASE):
                    conta_ativo = '23'
                    conta_despesa = '1424'
                else:
                    conta_ativo = '1615'
                    conta_despesa = '1428'
                
                lanSimp = "000001,"+ str(data_txt) + ","+str(conta_ativo)+",18," + str(self.df_agrupado.loc[i, valor_venda]) + ",00000000," + "Vlr. Ref. Cartão "+ str(self.df_agrupado.loc[i,bandeira])+" "+ str(self.df_agrupado.loc[i,'Natureza']) + " - Nº de Vendas:"+ str(self.df_agrupado.loc[i,'Quantidade']) +",,"+ cpfoucnpj + "," + "\n"
                lanSimpT = "000001,"+ str(data_txt) + ","+str(conta_despesa)+","+str(conta_ativo)+"," + str(self.df_agrupado.loc[i, 'Taxa']) + ",00000000," + "Vlr. Ref. Taxa Cartão "+ str(self.df_agrupado.loc[i,bandeira])+" "+ str(self.df_agrupado.loc[i,'Natureza']) + " - Nº de Vendas:"+ str(self.df_agrupado.loc[i,'Quantidade']) +",,"+ cpfoucnpj + "," + "\n"
                self.txt += str(lanSimp)
                self.txt += str(lanSimpT)

            self.exibir_relatorio_pagbank(self.relatorio)
            print(self.txt)
            
            # Definir o cabeçalho
            header = [
                "Número do lançamento",
                "Data do Lançamento",
                "Conta Contábil/Conta Contábil Débito",
                "Centro Custo/Centro Custo Débito",
                "Vazio1",
                "Vazio2",
                "Conta Contábil/Conta Contábil Crédito",
                "Centro Custo/Centro Custo Crédito",
                "Vazio3",
                "Vazio4",
                "Valor",
                "Histórico",
                "Tipo D/C",
                "CAtividade/Atividade Débito",
                "Atividade Crédito"
            ]

            # Criar um dataframe a partir dos dados
            df_ath = pd.read_csv(StringIO(self.txt), header=None)

            # Adicionar colunas extras ao DataFrame
            for i in range(len(header) - len(df_ath.columns)):
                df_ath[len(df_ath.columns) + i] = ""
            
            # Atribuir o cabeçalho ao dataframe
            df_ath.columns = header

            # Preencher as colunas conforme especificado
            df_ath["Número do lançamento"] = df_ath.index + 1
            df_ath["Histórico"] = df_ath.iloc[:, 6]
            df_ath["Data do Lançamento"] = pd.to_datetime(df_ath.iloc[:, 1], format='%Y%m%d').dt.strftime('%d/%m/%Y')
            df_ath["Conta Contábil/Conta Contábil Débito"] = df_ath.iloc[:, 2]
            df_ath["Conta Contábil/Conta Contábil Crédito"] = df_ath.iloc[:, 3]
            df_ath["Valor"] = df_ath.iloc[:, 4].round(2)


            # Preencher outras colunas com valores padrão
            df_ath["Tipo D/C"] = ""
            df_ath["Centro Custo/Centro Custo Débito"] = ""
            df_ath["Centro Custo/Centro Custo Crédito"] = ""
            df_ath["Vazio1"] = ""
            df_ath["Vazio2"] = ""
            df_ath["Vazio3"] = ""
            df_ath["Vazio4"] = ""
            df_ath["CAtividade/Atividade Débito"] = ""
            df_ath["Atividade Crédito"] = ""

            # Exibir o dataframe
            print("--------------------------------------- df_ath -------------------------------------------------")
            print(df_ath)

            # Salvar o dataframe como uma planilha Excel
            arquivo_excel_salvar = r'C:\Users\Icaro\Desktop\Develop\integrAgir\exemplos\Relatório_cartão_athenas.xlsx'
            df_ath.to_excel(arquivo_excel_salvar, index=False)

            QMessageBox.warning(self, 'Info', 'Excel carregado com Sucesso')  
        except KeyError as erro:
            QMessageBox.warning(self, 'KeyError', 'Não foi localizado a coluna: '+ str(erro))
            print(erro)
        except ValueError as erro:
            QMessageBox.warning(self, 'ValueError', 'Retire o filtor da planilha.')
            print(erro)                   
        except Exception as erro:
            QMessageBox.warning(self, 'Error', 'Erro ao tentar carregar o aquivo. - '+ str(erro))
            print(erro)    

    def analisar_forma_pagamento(self, forma_pagamento):
        if 'crédito' in forma_pagamento:
            return 'Crédito'
        elif 'débito' in forma_pagamento:
            return 'Débito'
        else:
            return 'Voucher'

    def exibir_relatorio_pagbank(self, relatorio):
        # Criar os componentes do layout
        # fonte_titulo = QFont('Arial', 14, QFont.Bold)
        # fonte_conteudo = QFont('Arial', 8)
        
        titulo_label = QLabel('Relatório de Pagamentos')
        # titulo_label.setFont(fonte_titulo)
        
        credito_label = QLabel(f'<span style="font-size: 10pt;"><b>Total de Crédito:</b></span> R$ {relatorio["total_credito"]} - <b>Quantidade:</b> {relatorio["quantidade_credito"]}')
        debito_label = QLabel(f'<span style="font-size: 10pt;"><b>Total de Débito:</b></span> R$ {relatorio["total_debito"]} - <b>Quantidade:</b> {relatorio["quantidade_debito"]}')
        voucher_label = QLabel(f'<span style="font-size: 10pt;"><b>Total de Voucher:</b></span> R$ {relatorio["total_voucher"]} - <b>Quantidade:</b> {relatorio["quantidade_voucher"]}')
        geral_label = QLabel(f'<span style="font-size: 10pt;"><b>Total Geral:</b></span> R$ {relatorio["total_geral"]} - <b>Quantidade Total:</b> {relatorio["quantidade_total"]}')
        
        # Definir os estilos CSS
        estilo_titulo = "QLabel { border: none; font-size: 14pt; font-weight: bold; margin: 20px; margin-left: 45px}"
        estilo_conteudo = "QLabel { border: none; font-size: 10pt; margin:8px }"
        
        titulo_label.setStyleSheet(estilo_titulo)
        credito_label.setStyleSheet(estilo_conteudo)
        debito_label.setStyleSheet(estilo_conteudo)
        voucher_label.setStyleSheet(estilo_conteudo)
        geral_label.setStyleSheet(estilo_conteudo)
        
        # Criar o layout vertical
        layout = QVBoxLayout(self.ui.widgetRelatorioPagbank)
        layout.setContentsMargins(2, 2, 2, 2)  # Remover espaçamento interno
        layout.setSpacing(5)  # Definir espaçamento entre os widgets
        layout.setAlignment(Qt.AlignTop)  # Alinhar os widgets no topo

        layout.addWidget(titulo_label)
        layout.addWidget(credito_label)
        layout.addWidget(debito_label)
        layout.addWidget(voucher_label)
        layout.addWidget(geral_label)
                
        self.ui.widgetRelatorioPagbank.show()