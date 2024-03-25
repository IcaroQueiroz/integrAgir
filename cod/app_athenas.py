import pandas as pd
from itertools import combinations
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from datetime import datetime
from openpyxl.utils import get_column_letter
from openpyxl import Workbook
from openpyxl.styles import Font



def criar_planilha_com_cabecalhos(nome_arquivo, df_origem):
    # Criar uma nova planilha
    wb = Workbook()

    # Adicionar uma nova folha
    ws = wb.active

    # Cabeçalhos
    cabecalhos = [
        "Código do Fornecedor", "Nome Fornecedor", "CNPJ do Fornecedor", "Nota Fiscal", "Quantidade",
        "Patrimônio", "Data da Abertura", "Vida Útil", "Código da Conta Contábil", "Descrição do Bem",
        "Código do Centro de Custo", "Data da Entrada da Compra", "Data da Aquisição", "Valor Total da NF",
        "Base de Cálculo", "Aliquota", "Crédito de ICMS", "ICMS Adicional", "Valor do Mês", "Valor Alocado",
        "Código da Conta de Despesa da Depreciação", "SALDO DE ABERTURA", "CIAP", "ICMS Frete", "ICMS ST",
        "ICMS DIF", "Código da Conta de Depreciação Acumulada", "Valor Depreciado", "Código da Localização",
        "Parcelas CIAP", "Série", "Vida Útil em Meses", "Observações", "Tipo de Depreciação(0 - Fiscal, 1 - IFRS)",
        "Depreciar no Mês Seguinte(0 - Não, 1 - Sim)", "CPC - Natureza da BC Pis/Cofins", "CPC - Identificação dos Bens/Grupos",
        "CPC - Indicador de Origem do Bem", "CPC - CST Pis", "CPC - CST Cofins", "CPC - Indicador da Utilização do Bens",
        "CPC - Conta Contábil", "CPC - Indicador do Número de Parcelas", "CPC - Número de Parcelas",
        "CPC - Parcela a Excluir da B/C"
    ]

    # Adicionar cabeçalhos à nova planilha
    for col_num, cabecalho in enumerate(cabecalhos, start=1):
        coluna_letra = get_column_letter(col_num)
        ws[f"{coluna_letra}1"] = f" {coluna_letra} -> {cabecalho};"
        ws.column_dimensions[coluna_letra].width = len(cabecalho) + 4  # Ajuste a largura da coluna conforme necessário
        ws[f"{coluna_letra}1"].font = Font(bold=True)


    colunas_para_levar = {
            "Data aquisição": "G",
            "Taxa de depreciação": "H",
            "Código da conta": "I",
            "Nome do bem": "J",
            "Data aquisição": "L",
            "Data aquisição": "M",
            "Valor original da aquisição": "N"}

    # Mapeamento de substituição para a coluna "Código da conta"
    substituicoes_codigo_conta = {
        130: ["1.3.7.01.01.00000005", "verificar130"],
        103: ["1.3.7.01.01.00000005", "verificar103"],
        98: ["1.3.7.01.01.00000005", "verificar98"],
        99: ["1.3.7.01.01.00000005", "verificar99"],
    }
            
    # Adicionar dados das colunas da planilha de origem para as colunas correspondentes na planilha de destino
    for coluna_origem, coluna_destino in colunas_para_levar.items():
        if coluna_origem == "Código da conta":
            for i, valor in enumerate(df_origem[coluna_origem], start=2):
                valores_substituidos = substituicoes_codigo_conta.get(valor, [valor, ""])
                valor_tratado = valores_substituidos[0]  # Usar o primeiro valor da lista como valor tratado
                ws[f"{coluna_destino}{i}"] = valor_tratado

                # Adicionar o segundo valor da lista (se existir) à outra coluna
                if valores_substituidos[1]:
                    ws[f"AA{i}"] = valores_substituidos[1]  # Substituir "N" pela letra da coluna desejada
        elif coluna_origem == "Taxa de depreciação":
            for i, valor in enumerate(df_origem[coluna_origem], start=2):
                valor = float(valor.replace(',', '.'))
                if valor != 0:  # Evita divisão por zero
                    valor_tratado = 100 / valor
                    ws[f"{coluna_destino}{i}"] = valor_tratado
                else:
                    ws[f"{coluna_destino}{i}"] = 0  # Pode definir outro valor padrão se necessário
        else:
            for i, valor in enumerate(df_origem[coluna_origem], start=2):
                ws[f"{coluna_destino}{i}"] = valor

    # Salvar a nova planilha
    wb.save(nome_arquivo)


def abrir_planilha(nome_arquivo):
    # Carrega a planilha
    df_origem = pd.read_csv(nome_arquivo, sep=';', encoding='ISO-8859-1')  # Pula as duas primeiras linhas (considerando que a linha 3 seja a terceira)

    # Exibe o conteúdo da planilha a partir da linha 3
    print(df_origem)
    return df_origem

arquivo_excel = r'C:\Users\Icaro\Desktop\Develop\integrAgir\exemplos\Relatório da consulta.csv'
arquivo_excel_salvar = r'C:\Users\Icaro\Desktop\Develop\integrAgir\exemplos\Relatório da ativo 2.xlsx'
df_origem = abrir_planilha(arquivo_excel)
criar_planilha_com_cabecalhos(arquivo_excel_salvar, df_origem)

"""class AppAthenas():
    def Athenas(self):
        try:
                 

            QMessageBox.warning(self, 'Info', 'Excel carregado com Sucesso')  
        except KeyError as erro:
            QMessageBox.warning(self, 'KeyError', 'Não foi localizado a coluna: '+ str(erro))
        except ValueError as erro:
            QMessageBox.warning(self, 'ValueError', 'Retire os filtros da planilha.    ')                   
        except Exception as erro:
            QMessageBox.warning(self, 'Error', 'Erro ao tentar carregar o aquivo. - '+ str(erro))    
"""