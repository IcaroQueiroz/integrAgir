from interface import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget , QSizePolicy, QStackedWidget, QLabel, QVBoxLayout, QSizeGrip
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt, QPropertyAnimation
from PyQt5 import uic, QtCore
import iconify as ico
from iconify.qt import QtGui, QtWidgets, QtCore
from PySide2.QtCore import *
import os
import sys
from Custom_Widgets.Widgets import *
import requests

##########################################################
# CLASS API FIREBASE                                     #
##########################################################
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


##########################################################
# CLASS MAIN WINDOWS                                     #
##########################################################
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #--------------------------------------------------------#
        # APPLY JSON STYLESHEET  Lib.|Custom_Widgets.Widgets|    #
        #--------------------------------------------------------#
        #loadJsonStyle(self, self.ui)
        #self.show()
        
        # Personalização da barra de navegação
        self.ui.minimizeBtn.clicked.connect(self.showMinimized)
        self.ui.closeBtn.clicked.connect(self.close)
        self.ui.restoreBtn.clicked.connect(self.toggle_maximized)
        self.ui.restoreBtn.setCheckable(True)
        self.ui.restoreBtn.setChecked(self.isMaximized())
        # Ocultar a janela do Windows
        self.setWindowFlag(Qt.WindowTitleHint, False)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.show()
        # Permitir arrastar a janela ao clicar e arrastar no topo
        self.draggable = True
        self.draggable_area_height = 40  # Altura da área superior onde a janela pode ser arrastada
        
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
        # Conexão firebase e TabelaViwer Lacon                   #
        #--------------------------------------------------------#        
        firebase_url = "https://integragir-default-rtdb.firebaseio.com/Contratos-Lacon"
        self.firebase_api = FirebaseAPI(firebase_url)
        
        # Criar modelo de tabela
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["Contrato", "Imóvel", "Locatário", "CPF/CNPJ", "Valor", "Inicio", "Fim"])  # Definir rótulos das colunas

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
        # Funções do botoões MenuPrincipal                       #
        #--------------------------------------------------------#
        self.button_states = {
            self.ui.homeBtn: True,
            self.ui.appBtn: False,
            self.ui.cardBtn: False,
            self.ui.reportBtn: False}
    
        # Conecta o clique do botão à função de animação
        self.ui.menuBtn.clicked.connect(self.animate_menu)

        # Definir a geometria inicial do widget leftMenuContainer
        self.left_menu_width = 45
        self.ui.leftMenuSubContainer.setGeometry(0, 0, self.left_menu_width, self.height())

        # Conecta o clique dos botões do Menu aos Widget
        self.ui.homeBtn.clicked.connect(lambda: self.toggle_button_menuPrincipal(self.ui.homeBtn, 0))
        self.ui.appBtn.clicked.connect(lambda: self.toggle_button_menuPrincipal(self.ui.appBtn, 1))
        self.ui.cardBtn.clicked.connect(lambda: self.toggle_button_menuPrincipal(self.ui.cardBtn, 2))
        self.ui.reportBtn.clicked.connect(lambda: self.toggle_button_menuPrincipal(self.ui.reportBtn, 3))

        #--------------------------------------------------------#
        # Funções do botoões MenuTec                             #
        #--------------------------------------------------------#
        # Definir a geometria e configuração inicial do menu central como invisível
        self.center_menu_width = 200
        self.ui.centerMenuContainer.setMaximumWidth(0)
        self.ui.centerMenuContainer.setMinimumWidth(0)
        self.ui.centerMenuSubContainer.setGeometry(-self.center_menu_width, 0, 0, self.height())
        self.center_menu_visible = False

        # Conecta o clique dos botões aos Widget
        self.ui.settingsBtn.clicked.connect(lambda: self.toggle_button_menuTec(self.ui.settingsBtn, 0))
        self.ui.infoBtn.clicked.connect(lambda: self.toggle_button_menuTec(self.ui.infoBtn, 1))
        self.ui.closeCenterBtnSettings.clicked.connect(self.animate_center_menu)
        self.ui.closeCenterBtnInfo.clicked.connect(self.animate_center_menu)
                
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
        


#========================================================#
# Funçoes da Interface                                   #
#========================================================#
    def toggle_maximized(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.restoreBtn.setIcon(QIcon(":/icons/icons/square.svg"))
        else:
            self.showMaximized()
            self.ui.restoreBtn.setIcon(QIcon(":/icons/icons/copy.svg"))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.is_top_draggable_area(event.pos()):
            self.draggable = True
            self.offset = event.pos()
        else:
            QMainWindow.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        if hasattr(self, 'offset') and self.draggable and event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.offset)
            event.accept()
        else:
            QMainWindow.mouseMoveEvent(self, event)     

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.draggable = False

    def is_top_draggable_area(self, pos):
        return pos.y() <= self.draggable_area_height
        pass

    def change_theme(self):
     
        if self.styleSheet() == self.current_theme:
            # Carregue o arquivo CSS para o novo tema desejado
            new_icon = QtGui.QIcon(":/imagens/img/desligar.png")
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
                #comboBoxApp{
                    background-color:#fff;
                    font-size: 16px;
                    color: #348498;
                    font-family: Arial;
                    border-radius:10px;
                    border: 2px solid #348498;
                    padding-left: 5px;
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
            new_icon = QtGui.QIcon(":/imagens/img/ligar.png") 
        # Aplique o novo tema para o aplicativo
        self.setStyleSheet(new_theme)
        self.ui.temaBtn.setIcon(new_icon)
        # Atualizar o estilo dos botões ativados
        buttons_list = [self.ui.homeBtn, self.ui.appBtn, self.ui.cardBtn, self.ui.reportBtn]
        for btn in buttons_list:
            if self.button_states[btn]:
                if self.styleSheet() == self.current_theme:
                    btn.setStyleSheet("background-color: #2c313c; border-left: 2px solid rgb(255,255,255);")
                    self.ui.settingsBtn.setStyleSheet("background-color: #2c313c;")
                else:
                    btn.setStyleSheet("background-color: #348498; border-left: 2px solid rgb(255,255,255);")
                    self.ui.settingsBtn.setStyleSheet("background-color: #348498;")
        self.ui.infoBtn.setStyleSheet("background-color: transparent;")
#========================================================#
# Funçoes do Menu                                        #
#========================================================#
    def animate_menu(self):
        # Verificar se o menu está recolhido ou expandido
        if self.left_menu_width == 45:
            # Criar uma animação para expandir o widget
            anim = QPropertyAnimation(self.ui.leftMenuContainer, b'geometry')
            anim.setDuration(500)  # Duração da animação em milissegundos
            anim.setStartValue(QRect(0, 0, self.left_menu_width, self.height()))
            anim.setEndValue(QRect(0, 0, 190, self.height()))  # Definir a geometria desejada
            self.left_menu_width = 190

            # Criar uma animação para ajustar a posição do leftMenuContainer
            pos_animation = QPropertyAnimation(self.ui.leftMenuContainer, b'pos')
            pos_animation.setDuration(500)  # Duração da animação em milissegundos
            pos_animation.setStartValue(QPoint(0, 0))
            pos_animation.setEndValue(QPoint(145, 0))  # Definir a posição desejada

            # Redimensionar o leftMenuSubContainer
            self.ui.leftMenuContainer.setMaximumWidth(190)
            self.ui.leftMenuContainer.setMinimumWidth(190)
            self.ui.leftMenuSubContainer.setMaximumWidth(190)
            self.ui.leftMenuSubContainer.setMinimumWidth(190)

            # Iniciar as animações
            anim.start()
            pos_animation.start()
            self.ui.menuBtn.setIcon(QIcon(":/icons/icons/chevron-left.svg"))

        else:
            # Criar uma animação para recolher o widget
            anim = QPropertyAnimation(self.ui.leftMenuContainer, b'geometry')
            anim.setDuration(500)  # Duração da animação em milissegundos
            anim.setStartValue(QRect(0, 0, self.left_menu_width, self.height()))
            anim.setEndValue(QRect(0, 0, 45, self.height()))  # Definir a geometria desejada
            self.left_menu_width = 45

            # Criar uma animação para ajustar a posição do leftMenuContainer
            pos_animation = QPropertyAnimation(self.ui.leftMenuContainer, b'pos')
            pos_animation.setDuration(500)  # Duração da animação em milissegundos
            pos_animation.setStartValue(QPoint(145, 0))
            pos_animation.setEndValue(QPoint(0, 0))  # Definir a posição desejada

            # Redimensionar o leftMenuSubContainer
            self.ui.leftMenuContainer.setMaximumWidth(45)
            self.ui.leftMenuContainer.setMinimumWidth(45)
            self.ui.leftMenuSubContainer.setMaximumWidth(45)
            self.ui.leftMenuSubContainer.setMinimumWidth(45)

            # Iniciar as animações
            anim.start()
            pos_animation.start()
            self.ui.menuBtn.setIcon(QIcon(":/icons/icons/align-justify.svg"))

    def toggle_button_menuPrincipal(self, button, index):
        buttons_list = [self.ui.homeBtn, self.ui.appBtn, self.ui.cardBtn, self.ui.reportBtn]

        self.button_states[button] = True
        for btn in buttons_list:
            if btn != button:
                btn.setStyleSheet("background-color: transparent;")
                self.button_states[btn] = False
                if btn.isChecked():
                    btn.setChecked(False)
                    

        if self.styleSheet() == self.current_theme:
            print('chegou a verificar == self.current_theme ')
            if button.isChecked():
                button.setStyleSheet("background-color: transparent;")
            else:
                button.setStyleSheet("background-color: #1f232a;  border-left: 2px solid rgb(255,255,255);")             
        else:
            if button.isChecked():
                button.setStyleSheet("background-color: transparent;")
            else:
                button.setStyleSheet("background-color: #348498;  border-left: 2px solid rgb(255,255,255);")
        self.ui.mainPages.setCurrentIndex(index)

    def animate_center_menu(self):
        # Verificar se o menu central está visível ou oculto
        if self.center_menu_visible:
            # Criar uma animação para ocultar o widget
            print('animação menu == visivel // entaão define false pois vai recolher')
            anim = QPropertyAnimation(self.ui.centerMenuSubContainer, b'geometry')
            anim.setDuration(500)  # Duração da animação em milissegundos
            anim.setStartValue(QRect(0, 0, self.center_menu_width, self.height()))
            anim.setEndValue(QRect(-self.center_menu_width, 0, self.center_menu_width, self.height()))  # Definir a geometria desejada

            # Redimensionar o centerMenuContainer e outros widgets
            self.ui.centerMenuContainer.setMaximumWidth(0)
            self.ui.centerMenuContainer.setMinimumWidth(0)
            # Ajustar outros widgets conforme necessário
            self.ui.centerMenuSubContainer.setMaximumWidth(0)
            self.ui.centerMenuSubContainer.setMinimumWidth(0)
            # Iniciar a animação
            anim.start()
            self.center_menu_visible = False

        else:
            print('animação menu == invisivel // entaão define true pois vai expandi')
            # Criar uma animação para exibir o widget
            anim = QPropertyAnimation(self.ui.centerMenuSubContainer, b'geometry')
            anim.setDuration(500)  # Duração da animação em milissegundos
            anim.setStartValue(QRect(-self.center_menu_width, 0, self.center_menu_width, self.height()))
            anim.setEndValue(QRect(0, 0, self.center_menu_width, self.height()))  # Definir a geometria desejada

            # Redimensionar o centerMenuContainer e outros widgets
            self.ui.centerMenuContainer.setMaximumWidth(self.center_menu_width)
            self.ui.centerMenuContainer.setMinimumWidth(self.center_menu_width)
            # Ajustar outros widgets conforme necessário
            self.ui.centerMenuSubContainer.setMaximumWidth(self.center_menu_width)
            self.ui.centerMenuSubContainer.setMinimumWidth(self.center_menu_width)
            # Iniciar a animação
            anim.start()
            self.center_menu_visible = True

    def toggle_button_menuTec(self, button, index):
        self.buttons_list = [self.ui.settingsBtn, self.ui.infoBtn]

        if self.center_menu_visible == True:
            if self.ui.infoBtn.isChecked() == False and self.ui.settingsBtn.isChecked() == True:
                self.ui.menuCenterPages.setCurrentIndex(index)
                print('entrou no returne e fim')
                for btn in self.buttons_list:
                    if self.styleSheet() == self.current_theme:
                        button.setStyleSheet("background-color: #2c313c;")
                    else:
                        button.setStyleSheet("background-color: #348498;")                   
                    if btn != button:
                        btn.setStyleSheet("background-color: transparent;")
                        if btn.isChecked():
                            btn.setChecked(False)
                            
                print('No verificação antes do retur ------------------------------')
                print('info', self.ui.infoBtn.isChecked())
                print('setting', self.ui.settingsBtn.isChecked())                    
                return

        print('No inicio de tudo ------------------------------')
        print('info', self.ui.infoBtn.isChecked())
        print('setting', self.ui.settingsBtn.isChecked())    
        if button.isChecked() == True:
            for btn in self.buttons_list:
                if btn != button:
                    btn.setStyleSheet("background-color: transparent;")
                    if btn.isChecked():
                        print('if que checa botão antes ---------------------------------')
                        print('info', self.ui.infoBtn.isChecked())
                        print('setting', self.ui.settingsBtn.isChecked())
                        btn.setChecked(False)
                        print('if que checa botão Depois ---------------------------------')
                        print('info', self.ui.infoBtn.isChecked())
                        print('setting', self.ui.settingsBtn.isChecked())
                        self.ui.menuCenterPages.setCurrentIndex(index)
                    else:
                        print('else que checa botão')
                        btn.setChecked(False)
                        self.animate_center_menu()
                        self.ui.menuCenterPages.setCurrentIndex(index)
        else:
            print('info', self.ui.infoBtn.isChecked())
            print('setting', self.ui.settingsBtn.isChecked())
            print(button)
            print(button.isChecked())
            print("foi para else final")
            self.animate_center_menu()


        if self.styleSheet() == self.current_theme:
            if button.isChecked() == True:
                button.setStyleSheet("background-color: #2c313c;")
            else:
                button.setStyleSheet("background-color: transparent;")
        else:
            if button.isChecked() == True:
                button.setStyleSheet("background-color: #348498;")
            else:
                button.setStyleSheet("background-color: transparent;")

    def handle_combobox_change(self, index):
        self.ui.stackedWidgetApp.setCurrentIndex(index)

#========================================================#
# Funçoes do Firebase                                    #
#========================================================#
    def on_table_data_changed(self, top_left, bottom_right):
        # Obter o modelo da tabela
        model = self.ui.tableViewLacon.model()
        field_mapping = {
                "Contrato": None,
                "Imóvel": "01-imovel",
                "Locatário": "02-locatario",
                "CPF/CNPJ": "03-cpf-cnpj",
                "Valor": "04-valor",
                "Inicio": "05-inicio",
                "Fim": "06-fim"  } 
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
                        firebase_key = field_mapping.get(column_name)
                        if firebase_key:
                            item_index = model.index(row, col)
                            item_data = item_index.data(Qt.DisplayRole)
                            row_data[firebase_key] = item_data

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


##########################################################
# EXECUÇÃO DA APLICAÇÃO                                  #
##########################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
