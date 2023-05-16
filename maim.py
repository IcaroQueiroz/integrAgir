from interface import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget , QSizePolicy, QStackedWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt
from PyQt5 import uic, QtCore
import iconify as ico
from iconify.qt import QtGui, QtWidgets, QtCore
from PySide2.QtCore import *
import os
import sys
from Custom_Widgets.Widgets import *
import requests


class ErrorNotification(QWidget):
    def __init__(self, error_message, parent=None):
        super().__init__(parent)
        uic.loadUi('interface.ui', self)

        # Configure widget appearance
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Find the popupNotificationContantContainer widget and the messageNotification label
        self.popup_container = self.findChild(QWidget, "popupNotificationContantContainer")
        self.message_label = self.findChild(QLabel, "messageNotification")

        # Set the error message to the label
        self.message_label.setText(error_message)

        # Set widget to be hidden by default
        self.hide()

    def show_as_notification(self):
        # Calculate widget position
        parent_geometry = self.parent().geometry()
        x = parent_geometry.x() + parent_geometry.width() - self.width() - 10
        y = parent_geometry.y() + parent_geometry.height() - self.height() - 10
        self.move(x, y)

        # Show widget
        self.popup_container.show()
        self.show()
        self.raise_()
        self.activateWindow()


class FirebaseAPI():
    def __init__(self, firebase_url):
        self.firebase_url = firebase_url

    def post(self, data):
        url = f"{self.firebase_url}.json"
        response = requests.post(url, json=data)
        return response.json()

    def get(self):
        url = f"{self.firebase_url}.json"
        response = requests.get(url)
        return response.json()

    def patch(self, item_id, data):
        url = f"{self.firebase_url}/{item_id}.json"
        response = requests.patch(url, json=data)
        return response.json()

    def delete(self, item_id):
        url = f"{self.firebase_url}/{item_id}.json"
        response = requests.delete(url)
        return response.json()



#--------------------------------------------------------#
# CLASS MAIN WINDOWS                                     #
#--------------------------------------------------------#
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #--------------------------------------------------------#
        # APPLY JSON STYLESHEET  Lib.|Custom_Widgets.Widgets|    #
        #--------------------------------------------------------#
        loadJsonStyle(self, self.ui)
        self.show()
        #--------------------------------------------------------#
        # Redimensionamento da janela e Definições iniciais      #
        #--------------------------------------------------------#
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumSize(400, 300)
        self.setMaximumSize(1680, 1050)
        #--------------------------------------------------------#
        # Definições de tema                                     #
        #--------------------------------------------------------#       
        self.current_theme = self.styleSheet()
        self.ui.temaBtn.clicked.connect(self.change_theme)

        #--------------------------------------------------------#
        # Funções do botoões Menu laco firebase                            #
        #--------------------------------------------------------#        
        firebase_url = "https://integragir-default-rtdb.firebaseio.com/Contratos-Lacon"
        self.firebase_api = FirebaseAPI(firebase_url)
        
        # Criar modelo de tabela
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["contrato", "nome", "cpf-cnpj", "imóvel", "inicio", "fim", "valor"])  # Definir rótulos das colunas

        # Carregar dados do Firebase
        data_dict = self.firebase_api.get()
        print("pint dic", data_dict)
        #data_dict = json.loads(data)

        # Preencher tabela com dados do Firebase
        for item_id, item in data_dict.items():  # Acessar as chaves e os valores dos dicionários
            row = [QStandardItem(str(item_id))]  # Adicionar o ID como o primeiro valor na linha
            row.extend(QStandardItem(str(value)) for value in item.values())  # Adicionar os demais valores do item
            model.appendRow(row)

        # Vincular modelo de tabela à tabela no Qt Designer
        self.ui.tableViewLacon.setModel(model)
        self.ui.tableViewLacon.horizontalHeader().setStretchLastSection(True)  # Ajustar largura das colunas
        self.ui.tableViewLacon.setSelectionBehavior(QTableView.SelectRows)  # Definir comportamento de seleção
        # Conectar o sinal de edição 'dataChanged' da tabela ao slot 'on_table_data_changed'
        self.ui.tableViewLacon.model().dataChanged.connect(self.on_table_data_changed)
        
        self.ui.btnNewRow.clicked.connect(self.add_new_row)
        self.ui.btnDeleteRow.clicked.connect(self.delete_row)
        
        
        
        #--------------------------------------------------------#
        # Funções do botoões MenuTec                             #
        #--------------------------------------------------------#
        self.ui.settingsBtn.clicked.connect(lambda: self.toggle_button_menuTec(self.ui.settingsBtn))
        self.ui.infoBtn.clicked.connect(lambda: self.toggle_button_menuTec(self.ui.infoBtn))
        self.ui.closeCenterBtnSettings.clicked.connect(lambda: self.toggle_button_menuTec(self.ui.closeCenterBtnSettings))
        self.ui.closeCenterBtnInfo.clicked.connect(lambda: self.toggle_button_menuTec(self.ui.closeCenterBtnInfo))
        
        
        #--------------------------------------------------------#
        # Funções do comboBox aba APP                            #
        #--------------------------------------------------------#        
        # adiciona as opções no comboBox
        self.ui.comboBoxApp.addItem('Home')
        self.ui.comboBoxApp.addItem('Eaj')
        self.ui.comboBoxApp.addItem('Lacon')
        # cria as páginas e as adiciona ao stackedWidget
        self.pageHomeApp = QWidget()
        label1 = QLabel('Conteúdo para Home')
        layout1 = QVBoxLayout(self.pageHomeApp)
        layout1.addWidget(label1)
        self.ui.stackedWidgetApp.addWidget(self.pageHomeApp)

        self.pageEaj = QWidget()
        label2 = QLabel('Conteúdo para Eaj')
        layout2 = QVBoxLayout(self.pageEaj)
        layout2.addWidget(label2)
        self.ui.stackedWidgetApp.addWidget(self.pageEaj)

        self.pageLacon = QWidget()
        label3 = QLabel('Conteúdo para lacon')
        layout3 = QVBoxLayout(self.pageLacon)
        layout3.addWidget(label3)
        self.ui.stackedWidgetApp.addWidget(self.pageLacon)
        
        # conecta o sinal currentIndexChanged do comboBox ao método handle_combobox_change

        self.ui.comboBoxApp.currentIndexChanged.connect(self.handle_combobox_change)
         
        
        # CLOSE MENU CENTER WIDGET SIZE
        
                # CLOSE MENU CENTER WIDGET SIZE
        self.ui.pushButton_6.clicked.connect(lambda: self.show_error_notification('Teste de msg notificação', self))

    def on_table_data_changed(self, top_left, bottom_right):
        # Obter o modelo da tabela
        model = self.ui.tableViewLacon.model()

        # Obter os novos dados editados
        for row in range(top_left.row(), bottom_right.row() + 1):
            # Obter o ID do item
            id_index = model.index(row, 0)
            item_id = id_index.data(Qt.DisplayRole)
            print("id_item", item_id)

            # Verificar se o campo de ID está vazio
            if item_id == '':
                QMessageBox.warning(self, 'Aviso', 'O campo CONTRATO não pode ser vazio.')
            else:
                # Verificar se o ID já existe em outro item
                for other_row in range(model.rowCount()):
                    if other_row != row:  # Ignorar a linha atual
                        other_id_index = model.index(other_row, 0)
                        other_item_id = other_id_index.data(Qt.DisplayRole)
                        if item_id == other_item_id:
                            QMessageBox.warning(self, 'Aviso', 'Já existe outro CONTRATO com o mesmo numero.')
                            break
                else:
                    # Obter as informações do item a ser atualizado
                    row_data = {}
                    for col in range(1, model.columnCount()):
                        column_name = model.headerData(col, Qt.Horizontal)
                        item_index = model.index(row, col)
                        item_data = item_index.data(Qt.DisplayRole)
                        row_data[column_name] = item_data

                    # Atualizar os dados no Firebase
                    self.firebase_api.patch(item_id, row_data)
                    continue

            # Limpar o campo ID
            model.setData(id_index, '')
            return


    def add_new_row(self):
        # Obter o modelo da tabela
        model = self.ui.tableViewLacon.model()

        # Obter a quantidade de colunas na tabela
        column_count = model.columnCount()

        # Criar uma nova linha com células vazias
        new_row = []
        for col in range(column_count):
            item = QStandardItem("")
            new_row.append(item)

        # Adicionar a nova linha ao modelo da tabela
        model.appendRow(new_row)
    
    def delete_row(self):
        # Obter o modelo da tabela
        model = self.ui.tableViewLacon.model()

        # Obter o índice da linha selecionada
        selected_index = self.ui.tableViewLacon.selectedIndexes()[0]

        # Obter o ID do item a ser excluído
        id_index = model.index(selected_index.row(), 0)
        item_id = id_index.data(Qt.DisplayRole)
        # Remover a linha selecionada da tabela
        model.removeRow(selected_index.row())

        # Excluir os dados correspondentes do Firebase
        self.firebase_api.delete(item_id)



    def toggle_button_menuTec(self, button):
        self.buttons_list = [self.ui.settingsBtn, self.ui.infoBtn]
        if button == self.ui.closeCenterBtnInfo or button == self.ui.closeCenterBtnSettings:
            self.ui.centerMenuContainer.collapseMenu()
            for btn in self.buttons_list:
                btn.setStyleSheet("background-color: transparent;")
                btn.setChecked(False)
            return

        for btn in self.buttons_list:
            if btn != button:
                btn.setStyleSheet("background-color: transparent;")
                print(btn.isChecked())
                if btn.isChecked():
                    print('checagem do btn')
                    self.ui.centerMenuContainer.collapseMenu()
                    btn.setChecked(False)
        self.ui.centerMenuContainer.slideMenu()

        if self.styleSheet() == self.current_theme:
            if button.isChecked():
                button.setStyleSheet("background-color: #2c313c;") 
            else:
                button.setStyleSheet("background-color: transparent;")

        else:
            if button.isChecked():
                button.setStyleSheet("background-color: #348498;")
            else:
                button.setStyleSheet("background-color: transparent;")
    def handle_combobox_change(self, index):
        self.ui.stackedWidgetApp.setCurrentIndex(index)


    def change_theme(self):
        self.buttons_list = [self.ui.settingsBtn, self.ui.infoBtn]
        
        if self.styleSheet() == self.current_theme:
            # Carregue o arquivo CSS para o novo tema desejado
            new_icon = QtGui.QIcon(":/icons/icons/toggle-left.svg")
            new_theme = """
                *{
                    border:none;
                    background-color: transparent;
                    background: transparent;
                    padding:0;
                    margin:0;
                }
                #centralwidget{
                    background-color: #F5FFFA;

                }
                #leftMenuSubContainer{
                    background-color: #004d61;
                }
                #leftMenuSubContainer QPushButton{
                    background-color: #004d61;
                    text-align: left;
                    padding:3px 10px;
                    color: #ffffff;
                }
                #frame_3 QPushButton{
                    background-color: #004d61;
                    text-align: left;
                    padding:3px 10px;
                    border-top-left-radius:10px;
                    border-bottom-left-radius:10px;
                }
                #centerMenuSubContainer{
                    background-color: #348498;
                }
                #centerMenuSubContainer QLabel{
                    color: #ffffff;
                }
                #widgetInfo, #widgetSettings, #popupNotificationContantContainer{
                    background-color: #004d61;
                    border-radius:10px;
                }
                #headerContainer, #footerContainer ,#footerContainer QLabel{
                    background-color: #348498;
                    color: #ffffff;
                }

                /* Outros seletores de estilo para widgets */

            """
        
        
        else:
            # Caso contrário, restaure a folha de estilos do tema anterior
            new_theme = self.current_theme
            new_icon = QtGui.QIcon(":/icons/icons/toggle-right.svg") 
        # Aplique o novo tema para o aplicativo
        self.setStyleSheet(new_theme)
        self.ui.temaBtn.setIcon(new_icon)
        # Atualizar o estilo dos botões ativados
        for btn in self.buttons_list:
            if btn.isChecked():
                if self.styleSheet() == self.current_theme:
                    btn.setStyleSheet("background-color: #2c313c;")
                else:
                    btn.setStyleSheet("background-color: #348498;")




    def show_error_notification(self, error_message, is_permanent=False):
        notification = ErrorNotification(error_message)
        notification.setParent(self.ui.centerMenuContainer)  # define QCustomSlideMenu como pai
        notification.show_as_notification()
        if not is_permanent:
            # Esconde a notificação após 5 segundos
            QtCore.QTimer.singleShot(15000, notification.hide)

   

#--------------------------------------------------------#
# EXECUÇÃO DA APLICAÇÃO                                  #
#--------------------------------------------------------#
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
