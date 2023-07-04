import pandas as pd
import requests
import json

df = pd.read_excel('exemplo lacon.xlsx', header=[2,3])


    def exibir_caixa_dialogo(self, tipo, titulo, mensagem):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(titulo)
        msg_box.setText(mensagem)

        # Definir o ícone e o tipo da caixa de diálogo
        if tipo == 'warning':
            msg_box.setIcon(QMessageBox.Warning)
        elif tipo == 'info':
            msg_box.setIcon(QMessageBox.Information)
        elif tipo == 'error':
            msg_box.setIcon(QMessageBox.Critical)

        # Aplicar estilo personalizado usando folhas de estilo
        msg_box.setStyleSheet("""
            QMessageBox {
                background-color: #FFFFFF;  /* Cor de fundo */
                color: #000000;  /* Cor do texto */
                font-size: 12pt;  /* Tamanho da fonte */
            }

            QMessageBox QLabel {
                font-weight: bold;  /* Texto em negrito */
            }

            QMessageBox QPushButton {
                background-color: #E0E0E0;  /* Cor de fundo do botão */
                color: #000000;  /* Cor do texto do botão */
                font-size: 11pt;  /* Tamanho da fonte do botão */
                padding: 5px;  /* Espaçamento interno do botão */
                border: none;  /* Remover borda do botão */
            }

            QMessageBox QPushButton:hover {
                background-color: #C0C0C0;  /* Cor de fundo do botão ao passar o mouse */
            }
        """)

        msg_box.exec_()