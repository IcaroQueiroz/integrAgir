from PyQt5.QtWidgets import QFileDialog, QMessageBox
import os
import sys
import pandas as pd
from cod.app_eaj import AppEaj
from cod.cielo import AppCielo
from cod.stone import AppStone

class Aplicacao(AppEaj, AppCielo, AppStone):
    def caminho_arquivo(self, caminho_relativo):
        """ Obtém o caminho absoluto para o recurso, para PyInstaller """
        try:
            caminho_base = sys._MEIPASS
        except Exception:
            caminho_base = os.path.abspath(".")

        return os.path.join(caminho_base, caminho_relativo)    

    def file_open_excel(self, funcionalidade):
        filename, _ = QFileDialog.getOpenFileName(self, 'Abrir arquivo', 'C://file', 'Arquivos Excel (*.xlsx; *.xls)')
        if filename:
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
            
            

