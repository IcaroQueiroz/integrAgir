from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize
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
from cod.app_athenas import AppAthenas


from cod.emprestimo import FuncoesEmpretimo

class Aplicacao(AppEaj, AppAgir, AppSabor, AppLacon, AppCielo, AppStone, AppRede, AppPagBank, FuncoesEmpretimo, AppAthenas):
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

    def file_salve_excel(self):
        try:
            filename, _ = QFileDialog.getSaveFileName(self, 'Salvar arquivo', 'C://file', 'Arquivos de Texto (*.xlsx)')
            if filename:
                self.wb.save(filename)
                QMessageBox.information(self, 'Info', 'Excel salvo com sucesso!')
        except Exception as erro:
            QMessageBox.warning(self, 'Error', 'Erro ao tentar salvar o arquivo Excel. - ' + str(erro))


    def open_save_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Salvar")

        # Carrega o ícone para a janela de diálogo
        dialog_icon = QIcon(":/imagens/img/icons8-press-kit-96.png")
        dialog.setWindowIcon(dialog_icon)

        
        layout = QHBoxLayout()

        # Definindo o estilo do botão para ter texto preto
        button_style = "QPushButton { color: black; }"

        # Criando o botão "Único" com o estilo definido
        save_unique_btn = QPushButton(" Único  ", dialog)
        save_unique_btn.setStyleSheet(button_style)
        save_unique_btn.setIcon(QIcon(":/imagens/img/Unico.png"))
        save_unique_btn.setIconSize(QSize(47, 47))
        save_unique_btn.clicked.connect(self.file_salve)
        save_unique_btn.setIcon(QIcon(":/imagens/img/Unico.png"))
        layout.addWidget(save_unique_btn)

        # Criando o botão "Athenas" com o estilo definido
        save_excel_btn = QPushButton(" Athenas ", dialog)
        save_excel_btn.setStyleSheet(button_style)
        save_excel_btn.setIcon(QIcon(":/imagens/img/Athenas.png"))
        save_excel_btn.setIconSize(QSize(40, 40))
        save_excel_btn.clicked.connect(self.file_salve_excel)
        save_excel_btn.clicked.connect(dialog.close)
        layout.addWidget(save_excel_btn)

        # Aplicando um fundo preto à caixa de diálogo
        dialog.setStyleSheet("QDialog { background-color: #f4f4f3; color: #000000; }")

        dialog.setLayout(layout)
        dialog.exec_()



    def file_open_pdf(self):
        self.Criar_pdf() 
            
            

