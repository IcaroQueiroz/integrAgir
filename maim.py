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





        self.ui.settingsBtn.clicked.connect(lambda: self.ui.centerMenuContainer.slideMenu())
        self.ui.infoBtn.clicked.connect(lambda: self.toggle_button_color(self.ui.infoBtn))
        self.ui.helpBtn.clicked.connect(lambda: self.ui.centerMenuContainer.slideMenu())
        # CLOSE MENU CENTER WIDGET SIZE
        self.ui.closeMenuCenterBtn.clicked.connect(lambda: self.ui.centerMenuContainer.collapseMenu())
        
                # CLOSE MENU CENTER WIDGET SIZE
        self.ui.pushButton_6.clicked.connect(lambda: self.show_error_notification('Teste de msg notificação', self))

    def toggle_button_color(self, button):
        self.ui.centerMenuContainer.slideMenu()
        self.ui.infoBtn.setStyleSheet("background-color: #fff; color: #000")
        if button.isChecked():
            self.ui.infoBtn.setStyleSheet("background-color: #fff; color: #000")
        else:
            self.ui.infoBtn.setStyleSheet("background-color: #16191d; color: #fff")
        self.ui.infoBtn.update()







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
