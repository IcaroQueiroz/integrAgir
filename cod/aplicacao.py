from PyQt5.QtWidgets import QFileDialog, QMessageBox
import os
import sys
import pandas as pd
from cod.app_eaj import AppEaj
from cod.app_agir import AppAgir
from cod.app_sabor import AppSabor
from cod.app_lacon import AppLacon
from cod.cielo import AppCielo
from cod.stone import AppStone
from cod.rede import AppRede
from cod.pagbank import AppPagBank

from cod.emprestimo import FuncoesEmpretimo

class Aplicacao(AppEaj, AppAgir, AppSabor, AppLacon, AppCielo, AppStone, AppRede, AppPagBank, FuncoesEmpretimo):
    def caminho_arquivo(self, caminho_relativo):
        """ Obtém o caminho absoluto para o recurso, para PyInstaller """
        try:
            caminho_base = sys._MEIPASS
        except Exception:
            caminho_base = os.path.abspath(".")

        return os.path.join(caminho_base, caminho_relativo)    

    def file_open_excel(self, funcionalidade):
        try:
            filename, _ = QFileDialog.getOpenFileName(self, 'Abrir arquivo', 'C://file', 'Arquivos Excel (*.xlsx; *.xls; *.csv)')
            if filename:
                if filename.endswith('.csv'):
                    self.df = pd.read_csv(filename)
                else:
                    self.df = pd.read_excel(filename)
                
                print(self.df)
                print(type(self.df))
                funcionalidade()
        except ValueError as erro:
            QMessageBox.warning(self, 'ValueError', 'Retire o filtor da planilha.')                   
        except Exception as erro:
            QMessageBox.warning(self, 'Error', 'Erro ao tentar carregar o aquivo. - '+ str(erro))


    def file_open_csv(self, funcionalidade):
        filename, _ = QFileDialog.getOpenFileName(self, 'Abrir arquivo', 'C://file', 'Arquivos Excel (*.xlsx; *.xls; *.csv)')
        if filename:
            if filename.endswith('.csv'):
                try:
                    self.df = pd.read_csv(filename, sep=';', encoding='utf-8')
                except Exception as erro:
                    try:
                        self.df = pd.read_csv(filename, sep=';', encoding='latin1', index_col=False)
                    except Exception as erro:    
                        QMessageBox.warning(self, 'Error', "Erro ao ler o arquivo CSV com a codificação 'utf-8' e "+ str(erro))

            else:
                self.df = pd.read_excel(filename)
            
            print(self.df)
            print(type(self.df))
            funcionalidade()


    def file_salve(self):
        try:
            filename, _ = QFileDialog.getSaveFileName(self, 'Salvar arquivo', 'C://file', 'Arquivos de Texto (*.txt)')
            if filename:
                with open(filename, 'w') as file:
                    file.write(self.txt)
                QMessageBox.information(self, 'Info', 'TXT salvo com sucesso!')
        except Exception as erro:
               QMessageBox.warning(self, 'Error', 'Erro ao tentar salvar o aquivo. - '+ str(erro))

    def file_open_pdf(self):
        self.Criar_pdf() 
            
            

