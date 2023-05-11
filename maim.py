from interface import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget , QSizePolicy, QStackedWidget, QLabel, QVBoxLayout

import iconify as ico
from iconify.qt import QtGui, QtWidgets, QtCore
from PyQt5 import uic, QtCore
from PySide2.QtCore import *

import os
import sys
# IMPORT Custom widgets
from Custom_Widgets.Widgets import *


class ErrorNotification(QCustomSlideMenu):
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


#--------------------------------------------------------#
# CLASS MAIN WINDOWS                                    #
#--------------------------------------------------------#
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui)

        self.show()

        # Define a política de redimensionamento da janela
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Define o tamanho mínimo da janela
        self.setMinimumSize(400, 300)

        # Define o tamanho máximo da janela
        self.setMaximumSize(800, 600)


        # EXPAND MENU CENTER WIDGET SIZE

        self.current_theme = self.styleSheet()
        self.ui.temaBtn.clicked.connect(self.change_theme)
        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        self.ui.settingsBtn.clicked.connect(lambda: self.toggle_button_color(self.ui.settingsBtn))
        self.ui.infoBtn.clicked.connect(lambda: self.toggle_button_color(self.ui.infoBtn))
        self.ui.closeCenterBtnSettings.clicked.connect(lambda: self.toggle_button_color(self.ui.closeCenterBtnSettings))
        self.ui.closeCenterBtnInfo.clicked.connect(lambda: self.toggle_button_color(self.ui.closeCenterBtnInfo))
        #################################################
        # adiciona as opções no comboBox
        self.ui.comboBoxApp.addItem('Home')
        self.ui.comboBoxApp.addItem('Eaj')

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
        
        # conecta o sinal currentIndexChanged do comboBox ao método handle_combobox_change
        self.ui.comboBoxApp.setStyleSheet('font-size: 16px; color: #fff; font-family: Arial; border-radius:\
                                             10px; border: 2px solid white; padding-left: 5px;')
        self.ui.comboBoxApp.currentIndexChanged.connect(self.handle_combobox_change)
         
        # CLOSE MENU CENTER WIDGET SIZE
        
                # CLOSE MENU CENTER WIDGET SIZE
        #self.ui.pushButton_6.clicked.connect(lambda: self.show_error_notification('Teste de msg notificação', self))

    def toggle_button_color(self, button):
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
                button.setStyleSheet("background-color: #004d61;")
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
                    background-color: #348498;
                }
                #leftMenuSubContainer QPushButton{
                    background-color: #348498;
                    text-align: left;
                    padding:3px 10px;
                }
                #frame_3 QPushButton{
                    background-color: #348498;
                    text-align: left;
                    padding:3px 10px;
                    border-top-left-radius:10px;
                    border-bottom-left-radius:10px;
                }
                #centerMenuSubContainer{
                    background-color: #004d61;
                }
                #centerMenuSubContainer QLabel{
                    color: #ffffff;
                }
                #widgetInfo, #widgetSettings, #popupNotificationContantContainer{
                    background-color: #348498;
                    border-radius:10px;
                }
                #headerContainer, #footerContainer{
                    background-color: #004d61;
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
                    btn.setStyleSheet("background-color: #004d61;")




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
