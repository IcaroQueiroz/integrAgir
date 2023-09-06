from PyQt5.QtWidgets import QFileDialog, QMessageBox
import os
import sys
import pandas as pd
from cod.app_eaj import AppEaj
from cod.app_agir import AppAgir
from cod.cielo import AppCielo
from cod.stone import AppStone
from cod.rede import AppRede
from cod.emprestimo import FuncoesEmpretimo

class Aplicacao(AppEaj, AppAgir, AppCielo, AppStone, AppRede, FuncoesEmpretimo):
    def caminho_arquivo(self, caminho_relativo):
        """ Obtém o caminho absoluto para o recurso, para PyInstaller """
        try:
            caminho_base = sys._MEIPASS
        except Exception:
            caminho_base = os.path.abspath(".")

        return os.path.join(caminho_base, caminho_relativo)    

    def file_open_excel(self, funcionalidade):
        filename, _ = QFileDialog.getOpenFileName(self, 'Abrir arquivo', 'C://file', 'Arquivos Excel (*.xlsx; *.xls; *.csv)')
        if filename:
            if filename.endswith('.csv'):
                self.df = pd.read_csv(filename)
            else:
                self.df = pd.read_excel(filename)
            
            print(self.df)
            print(type(self.df))
            funcionalidade()

    def file_open_csv_stone(self, funcionalidade):
        filename, _ = QFileDialog.getOpenFileName(self, 'Abrir arquivo', 'C://file', 'Arquivos Excel (*.xlsx; *.xls; *.csv)')
        if filename:
            if filename.endswith('.csv'):
                self.df = pd.read_csv(filename, sep=';', encoding='utf-8')
            else:
                self.df = pd.read_excel(filename)
            
            print(self.df)
            print(type(self.df))
            funcionalidade()

    def file_salve(self):
        filename, _ = QFileDialog.getSaveFileName(self, 'Salvar arquivo', 'C://file', 'Arquivos de Texto (*.txt)')
        if filename:
            with open(filename, 'w') as file:
                file.write(self.txt)
            QMessageBox.information(self, 'Info', 'TXT salvo com sucesso!')   

    def file_open_pdf(self):
        self.Criar_pdf() 
            
            

