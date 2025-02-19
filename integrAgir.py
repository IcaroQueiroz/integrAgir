from interface import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QDateEdit, QWidget, QSizePolicy, QStackedWidget, QLabel, QVBoxLayout, QSizeGrip, QFileDialog, QMessageBox, QLineEdit
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon, QRegExpValidator, QValidator, QKeyEvent
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect, QPoint, QRegExp, QDate
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QTableView
import iconify as ico
from iconify.qt import QtGui, QtWidgets, QtCore
import re
import os
import sys
import requests
import pandas as pd
from datetime import datetime
from custom.theme import Theme
from cod.aplicacao import Aplicacao


##############################################################################
# CLASS API FIREBASE                                                         #
##############################################################################
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

##############################################################################
# CLASS MAIN WINDOWS                                                         #
##############################################################################
class MainWindow(QMainWindow, Aplicacao, Theme):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #--------------------------------------------------------------------------#
        # Personalização MainWindows                                               #
        #--------------------------------------------------------------------------#

        # Personalização da barra de navegação
        self.ui.minimizeBtn.clicked.connect(self.showMinimized)
        self.ui.closeBtn.clicked.connect(self.close)
        self.ui.restoreBtn.clicked.connect(self.toggle_maximized)
        self.ui.restoreBtn.setCheckable(True)
        self.ui.restoreBtn.setChecked(self.isMaximized())
        
        # Redimensionamento da janela e Definições iniciais                        #
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumSize(400, 300)
        self.setMaximumSize(1680, 1050)

        # Configuração do size grip
        size_grip = QSizeGrip(self.ui.sizeGrip)  # Use o seu QFrame existente
        size_grip.setToolTip('Redimensionar Janela')  # Opcional: Adicionar dica de ferramenta
        
        # Permitir arrastar a janela ao clicar e arrastar no topo
        self.draggable = True
        self.draggable_area_height = 40  # Altura da área superior onde a janela pode ser arrastada
        
        # Ocultar a janela(Windows)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.show()

        #--------------------------------------------------------------------------#
        # Definições de tema                                                       #
        #--------------------------------------------------------------------------#       
        self.current_theme = self.styleSheet()
        self.ui.temaBtn.clicked.connect(self.change_theme)

        #--------------------------------------------------------------------------#
        # Conexão firebase e TabelaViwer Lacon                                     #
        #--------------------------------------------------------------------------#        
        firebase_url = "https://integragir-default-rtdb.firebaseio.com/Contratos-Lacon"
        self.firebase_api = FirebaseAPI(firebase_url)
        
        # Criar modelo de tabela
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["Contrato", "Imóvel", "Locatário", "CPF/CNPJ", "Valor", "Inicio", "Fim"])  # Definir rótulos das colunas

        # Carregar dados do Firebase
        self.data_dict = self.firebase_api.get()
        print("pint dic", self.data_dict)
        #self.data_dict = json.loads(data)

        # Preencher tabela com dados do Firebase
        for item_id, item in self.data_dict.items():  # Acessar as chaves e os valores dos dicionários
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
        
        #--------------------------------------------------------------------------#
        # Funções do botoões MenuPrincipal                                         #
        #--------------------------------------------------------------------------#
        self.button_states = {
            self.ui.homeBtn: True,
            self.ui.appBtn: False,
            self.ui.cardBtn: False,
            self.ui.reportBtn: False,
            self.ui.athenasBtn: False}
    
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
        self.ui.athenasBtn.clicked.connect(lambda: self.toggle_button_menuPrincipal(self.ui.athenasBtn, 4))

        #--------------------------------------------------------------------------#
        # Funções do botoões MenuTec                                               #
        #--------------------------------------------------------------------------#
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
                
        #--------------------------------------------------------------------------#
        # Funções do comboBox aba APP                                              #
        #--------------------------------------------------------------------------#        
        # adiciona as opções no comboBox
        self.ui.comboBoxApp.addItem('Selecione uma empresa...')
        self.ui.comboBoxApp.addItem('EAJ ENGENHARIA LTDA EPP')
        self.ui.comboBoxApp.addItem('LACON EMPREENDIMENTOS IMOBILIARIOS')
        self.ui.comboBoxApp.addItem('AGIR - ASSESSORIA EMPRESARIAL LTDA')
        self.ui.comboBoxApp.addItem('SABOR DA CASA LTDA EPP')
        # cria as páginas e as adiciona ao stackedWidget
        self.pageHomeApp = QWidget()
        layout1 = QVBoxLayout(self.pageHomeApp)
        self.ui.stackedWidgetApp.addWidget(self.pageHomeApp)

        self.pageEaj = QWidget()
        layout2 = QVBoxLayout(self.pageEaj)
        self.ui.stackedWidgetApp.addWidget(self.pageEaj)

        self.pageLacon = QWidget()
        layout3 = QVBoxLayout(self.pageLacon)
        self.ui.stackedWidgetApp.addWidget(self.pageLacon)

        self.pageAgir = QWidget()
        layout4 = QVBoxLayout(self.pageAgir)
        self.ui.stackedWidgetApp.addWidget(self.pageAgir)

        self.pageSabor = QWidget()
        layout5 = QVBoxLayout(self.pageSabor)
        self.ui.stackedWidgetApp.addWidget(self.pageSabor)

        
        # conecta o sinal currentIndexChanged do comboBox ao método handle_combobox_change

        self.ui.comboBoxApp.currentIndexChanged.connect(self.handle_combobox_change)
        #--------------------------------------------------------------------------#
        # Funções na ABA Eaj do APP                                                #
        #--------------------------------------------------------------------------#
        self.ui.excelEajBtn.clicked.connect(lambda: self.file_open_excel(self.eaj))
        self.ui.txtEajBtn.clicked.connect(self.file_salve)

        #--------------------------------------------------------------------------#
        # Funções na ABA AGIR do APP                                               #
        #--------------------------------------------------------------------------#
        self.ui.excelAgirBtn.clicked.connect(lambda: self.file_open_excel(self.agir))
        self.ui.txtAgirBtn.clicked.connect(self.file_salve)

        #--------------------------------------------------------------------------#
        # Funções na ABA SABOR do APP                                              #
        #--------------------------------------------------------------------------#
        self.ui.excelSaborBtn.clicked.connect(lambda: self.file_open_excel(self.sabor))
        self.ui.txtSaborBtn.clicked.connect(self.file_salve)

        #--------------------------------------------------------------------------#
        # Funções na ABA LACOM do APP                                              #
        #--------------------------------------------------------------------------#
        self.ui.excelLaconBtn.clicked.connect(lambda: self.file_open_excel(self.lacon))
        self.ui.txtLaconBtn.clicked.connect(self.file_salve)


        #--------------------------------------------------------------------------#
        # Funções dos Entry ABA emprestimo                                         #
        #--------------------------------------------------------------------------#        
        # ------------  Aceita Datas --------------
        regex_data = QRegExp(r'^\d{2}/?\d{2}/?\d{4}$') # Expressão regular para datas
        validator_data = QRegExpValidator(regex_data)
        self.ui.entryDataEmp.setValidator(validator_data)        
        # ------------  Aceita Inteiros ------------ 
        regex_inteiro = QRegExp(r'^[0-9]+$') # Expressão regular para números inteiros
        validator_inteiro = QRegExpValidator(regex_inteiro)
        self.ui.entryParcelaEmp.setValidator(validator_inteiro)
        self.ui.entryParcelaEmp.installEventFilter(self)
        # ------------  Aceita Valores ------------ 
        regex_valor = QRegExp(r'^[0-9]*\.?[0-9]+$') # Expressão regular para números inteiros
        validator_valor = QRegExpValidator(regex_valor)
        self.ui.entryIoEmp.setValidator(validator_valor)

        self.ui.pushButton.clicked.connect(self.Calcular_Lan)
        


        #--------------------------------------------------------------------------#
        # Funções do comboBox aba Cartão                                           #
        #--------------------------------------------------------------------------#        
        # adiciona as opções no comboBox
        self.ui.comboBoxCartao.addItem('Selecione uma operadora ...')
        self.ui.comboBoxCartao.addItem('Cielo')
        self.ui.comboBoxCartao.addItem('Stone')
        self.ui.comboBoxCartao.addItem('Redecard')
        self.ui.comboBoxCartao.addItem('PagBank')
        # cria as páginas e as adiciona ao stackedWidget
        self.pageHomeCartao = QWidget()
        layout1 = QVBoxLayout(self.pageHomeCartao)
        self.ui.stackedWidgetCartao.addWidget(self.pageHomeCartao)

        self.pageCielo = QWidget()
        layout2 = QVBoxLayout(self.pageEaj)
        self.ui.stackedWidgetCartao.addWidget(self.pageCielo)

        self.pageStone = QWidget()
        layout3 = QVBoxLayout(self.pageStone)
        self.ui.stackedWidgetCartao.addWidget(self.pageStone)

        self.pageRedecard = QWidget()
        layout4 = QVBoxLayout(self.pageRedecard)
        self.ui.stackedWidgetCartao.addWidget(self.pageRedecard)

        self.pagePagBank = QWidget()
        layout5 = QVBoxLayout(self.pagePagBank)
        self.ui.stackedWidgetCartao.addWidget(self.pagePagBank)

        #--------------------------------------------------------------------------#
        # Funções dos Cartão de Credito                                            #
        #--------------------------------------------------------------------------#
        self.ui.cieloExcelBtn.clicked.connect(lambda: self.file_open_excel(self.cielo))
        self.ui.cieloTxtBtn.clicked.connect(self.open_save_dialog)
        self.ui.stoneExcelBtn.clicked.connect(lambda: self.file_open_csv(self.stone))
        self.ui.stoneTxtBtn.clicked.connect(self.open_save_dialog)
        self.ui.redeExcelBtn.clicked.connect(lambda: self.file_open_excel(self.rede))
        self.ui.redeTxtBtn.clicked.connect(self.open_save_dialog)
        self.ui.pagbankExcelBtn.clicked.connect(lambda: self.file_open_csv(self.pagbank))
        self.ui.pagbankTxtBtn.clicked.connect(self.open_save_dialog)
        # conecta o sinal currentIndexChanged do comboBox ao método handle_combobox_change

        self.ui.comboBoxCartao.currentIndexChanged.connect(self.handle_combobox_change_cartao)


        # CLOSE MENU CENTER WIDGET SIZE  

        #--------------------------------------------------------------------------#
        # Funções do comboBox aba Athenas                                             ###############################################
        #--------------------------------------------------------------------------#        
        # adiciona as opções no comboBox
        self.ui.comboBoxAthenas.addItem('Selecione uma empresa...')
        self.ui.comboBoxAthenas.addItem('Imobilizado')

        # cria as páginas e as adiciona ao stackedWidget
        self.pageHomeAthenas = QWidget()
        layout1 = QVBoxLayout(self.pageHomeAthenas)
        self.ui.stackedWidgetAthenas.addWidget(self.pageHomeAthenas)

        self.pageImobilizado = QWidget()
        layout2 = QVBoxLayout(self.pageImobilizado)
        self.ui.stackedWidgetAthenas.addWidget(self.pageImobilizado)
        
        #self.ui.comboBoxAthenas.currentIndexChanged.connect(self.handle_combobox_change)
        #self.handle_combobox_change(index, self.ui.stackedWidgetCartao)
        self.ui.comboBoxAthenas.currentIndexChanged.connect(lambda index: self.handle_combobox_changeX(index, self.ui.stackedWidgetAthenas))

        #--------------------------------------------------------------------------#
        # Funções na ABA LACOM do Athenas                                          #
        #--------------------------------------------------------------------------#
        self.ui.csvAthenasImob.clicked.connect(lambda: self.file_open_csv(self.athenas))
        self.ui.excelAthenasImob.clicked.connect(self.file_salve_excel)



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
    
    def eventFilter(self, obj, event):
        if obj == self.ui.entryParcelaEmp and event.type() == event.KeyPress:
            if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
                self.moverFoco()
                return True

        return super().eventFilter(obj, event)

    def moverFoco(self):
        self.focusNextChild()
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
        buttons_list = [self.ui.homeBtn, self.ui.appBtn, self.ui.cardBtn, self.ui.reportBtn, self.ui.athenasBtn]

        self.button_states[button] = True
        for btn in buttons_list:
            if btn != button:
                btn.setStyleSheet("background-color: transparent;")
                self.button_states[btn] = False
                if btn.isChecked():
                    btn.setChecked(False)
                if btn == self.ui.reportBtn:
                    if button.isChecked():
                        QMessageBox.warning(self, 'Info', 'Este módulo ainda está em desenvolvimento.')

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

        print(button.text())

        # Verifica se o botão reportBtn está selecionado
        if button.text() == '  Parcelados':
            print("chegou aqui o")
            QMessageBox.warning(self, 'Info', 'Este módulo ainda está em desenvolvimento. Por favor, aguarde atualizações futuras para acesso completo a esta funcionalidade.')

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
            buttons_list = [self.ui.settingsBtn, self.ui.infoBtn]
            for btn in buttons_list:
                btn.setChecked(False)
                btn.setStyleSheet("background-color: transparent;")
                btn.setStyleSheet("background-color: transparent;")
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
 
    def handle_combobox_change_cartao(self, index):
        self.ui.stackedWidgetCartao.setCurrentIndex(index)

    def handle_combobox_changeX(self, index, stacked_widget):
        stacked_widget.setCurrentIndex(index)


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
                    # Atualizar self.data_dict com os dados atualizados do Firebase
                    self.update_data_dict()
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
        
        # Atualizar self.data_dict com os dados atualizados do Firebase
        self.update_data_dict()
    
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

        # Atualizar self.data_dict com os dados atualizados do Firebase
        self.update_data_dict()

    def update_data_dict(self):
        self.data_dict = self.firebase_api.get()

##############################################################################
# EXECUÇÃO DA APLICAÇÃO                                                      #
##############################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


##############################################################################
# EXECUÇÃO DO PYINSTALLER                                                    #
##############################################################################

"""pyinstaller --onefile --noconsole --icon=icons/icon.ico --add-data "custom;custom" --add-data "cod;cod" --add-data "icons;icons" --add-data "img;img" --add-data "interface.py;." --add-data "Resources_rc.py;." --add-data "Resources.qrc;." integrAgir.py
"""