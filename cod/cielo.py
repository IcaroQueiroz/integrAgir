import pandas as pd
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from io import StringIO
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

class AppCielo():
    def cielo(self):
        try: 
            # Identificar a linha do título da coluna
            if self.df.iloc[:, 0].str.contains('Data da venda').any():
                linha_titulo = self.df[self.df.iloc[:, 0] == 'Data da venda'].index[0]
                data_venda = 'Data da venda'
                valor_venda = 'Valor da venda'
                valor_liquido = 'Valor líquido da venda'
                self.df = self.df.iloc[linha_titulo:]
                print('############################################## ok ############################################')
                print(self.df) 

            else:
                linha_titulo = self.df[self.df.iloc[:, 0] == 'Data de venda'].index[0]
                data_venda = 'Data de venda'
                valor_venda = 'Valor bruto'
                valor_liquido = 'Valor líquido'
                self.df = self.df.iloc[linha_titulo:]
                print('############################################## não localizado ############################################')
                print(self.df) 

            #self.df = self.df.iloc[linha_titulo:] # Definir o DataFrame para incluir apenas as colunas relevantes
            self.df = self.df.reset_index(drop=True) # Renumera as linhas a partir de 1 e remove a primeira linha duplicada do cabeçalho
            self.df = self.df.rename(columns=self.df.iloc[0]) # Definir a linha 0 como cabeçalho do DataFrame
            self.df = self.df[1:] # Descartar a linha 0, pois ela foi usada como cabeçalho

            self.df['Natureza'] = self.df['Forma de pagamento'].apply(self.analisar_forma_pagamento)
            self.df[data_venda] = pd.to_datetime(self.df[data_venda])  # Converta a coluna para o tipo de dados datetime, se ainda não estiver
            self.df[data_venda] = self.df[data_venda].dt.date  # Extraia apenas a parte da data, excluindo a hora
            self.df['DataNat'] = self.df[data_venda].astype(str) + self.df['Bandeira'].astype(str) + self.df['Natureza'].astype(str) # Concatene a data (sem hora) com a coluna 'Natureza'

            # Converter as colunas para o tipo de dados numérico
            self.df[valor_venda] = pd.to_numeric(self.df[valor_venda], errors='coerce')
            self.df[valor_liquido] = pd.to_numeric(self.df[valor_liquido], errors='coerce')


            # Agrupando e somando os valores
            self.df_agrupado = self.df.groupby([data_venda, 'Bandeira', 'Natureza', 'DataNat']).agg({valor_venda: 'sum', valor_liquido: 'sum', 'DataNat': 'count'}).rename(columns={'DataNat': 'Quantidade'}).reset_index()
            self.df_agrupado['Taxa'] = self.df_agrupado.apply(lambda row: row[valor_venda] - row[valor_liquido], axis=1)

            print(self.df_agrupado)

            
            # Filtrar os dados relevantes
            dados_credito = self.df_agrupado[self.df_agrupado['Natureza'] == 'Crédito']
            dados_debito = self.df_agrupado[self.df_agrupado['Natureza'] == 'Débito']
            dados_voucher = self.df_agrupado[self.df_agrupado['Natureza'] == 'Voucher']

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
                if 'Crédito' in data_nat:
                    conta_ativo = '22'
                    conta_despesa = '1423'
                elif 'Débito' in data_nat:
                    conta_ativo = '22'
                    conta_despesa = '1423'
                else:
                    conta_ativo = '1615'
                    conta_despesa = '1428'
                
                lanSimp = "000001,"+ str(data_txt) + ","+str(conta_ativo)+",18," + str(self.df_agrupado.loc[i, valor_venda]) + ",00000000," + "Vlr. Ref. Cartão "+ str(self.df_agrupado.loc[i,'Bandeira'])+" "+ str(self.df_agrupado.loc[i,'Natureza']) + " - Nº de Vendas:"+ str(self.df_agrupado.loc[i,'Quantidade']) +",,"+ cpfoucnpj + "," + "\n"
                lanSimpT = "000001,"+ str(data_txt) + ","+str(conta_despesa)+","+str(conta_ativo)+"," + str(self.df_agrupado.loc[i, 'Taxa']) + ",00000000," + "Vlr. Ref. Cartão "+ str(self.df_agrupado.loc[i,'Bandeira'])+" "+ str(self.df_agrupado.loc[i,'Natureza']) + " - Nº de Vendas:"+ str(self.df_agrupado.loc[i,'Quantidade']) +",,"+ cpfoucnpj + "," + "\n"
                self.txt += str(lanSimp)
                self.txt += str(lanSimpT)

            self.exibir_relatorio(self.relatorio)
            print(self.txt)

            # Criar uma nova planilha
            self.wb = Workbook()
            # Adicionar uma nova folha
            self.ws = self.wb.active


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
            self.df_ath = pd.read_csv(StringIO(self.txt), header=None)

            # Adicionar colunas extras ao DataFrame
            for i in range(len(header) - len(self.df_ath.columns)):
                self.df_ath[len(self.df_ath.columns) + i] = ""
            
            # Atribuir o cabeçalho ao dataframe
            self.df_ath.columns = header

            # Preencher as colunas conforme especificado
            self.df_ath["Número do lançamento"] = self.df_ath.index + 1
            self.df_ath["Histórico"] = self.df_ath.iloc[:, 6]
            self.df_ath["Data do Lançamento"] = pd.to_datetime(self.df_ath.iloc[:, 1], format='%Y%m%d').dt.strftime('%d/%m/%Y')
            self.df_ath["Conta Contábil/Conta Contábil Débito"] = self.df_ath.iloc[:, 2]
            self.df_ath["Conta Contábil/Conta Contábil Crédito"] = self.df_ath.iloc[:, 3]
            self.df_ath["Valor"] = self.df_ath.iloc[:, 4].round(2)


            # Preencher outras colunas com valores padrão
            self.df_ath["Tipo D/C"] = ""
            self.df_ath["Centro Custo/Centro Custo Débito"] = ""
            self.df_ath["Centro Custo/Centro Custo Crédito"] = ""
            self.df_ath["Vazio1"] = ""
            self.df_ath["Vazio2"] = ""
            self.df_ath["Vazio3"] = ""
            self.df_ath["Vazio4"] = ""
            self.df_ath["CAtividade/Atividade Débito"] = ""
            self.df_ath["Atividade Crédito"] = ""

            # Adicionar os dados do DataFrame à planilha
            for r in dataframe_to_rows(self.df_ath, index=False, header=True):
                self.ws.append(r)


            # Exibir o dataframe
            print("--------------------------------------- self.df_ath -------------------------------------------------")
            self.ws = self.df_ath          
            
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
        if 'Crédito' in forma_pagamento:
            return 'Crédito'
        elif 'Débito' in forma_pagamento:
            return 'Débito'
        else:
            return 'Voucher'

    def exibir_relatorio(self, relatorio):
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
        layout = QVBoxLayout(self.ui.widgetRelatorioCielo)
        layout.setContentsMargins(2, 2, 2, 2)  # Remover espaçamento interno
        layout.setSpacing(5)  # Definir espaçamento entre os widgets
        layout.setAlignment(Qt.AlignTop)  # Alinhar os widgets no topo

        layout.addWidget(titulo_label)
        layout.addWidget(credito_label)
        layout.addWidget(debito_label)
        layout.addWidget(voucher_label)
        layout.addWidget(geral_label)
                
        self.ui.widgetRelatorioCielo.show()