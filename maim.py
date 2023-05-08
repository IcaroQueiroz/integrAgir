from interface import *
from PyQt5.QtWidgets import QApplication, QMainWindow
import os
import sys
# IMPORT Custom widgets
from Custom_Widgets.Widgets import *

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
        self.ui.infoBtn.clicked.connect(lambda: self.ui.centerMenuContainer.slideMenu())
        self.ui.helpBtn.clicked.connect(lambda: self.ui.centerMenuContainer.slideMenu())
        # CLOSE MENU CENTER WIDGET SIZE
        self.ui.closeMenuCenterBtn.clicked.connect(lambda: self.ui.centerMenuContainer.collapseMenu())

                # CLOSE MENU CENTER WIDGET SIZE
        self.ui.notificationBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.slideMenu())


#--------------------------------------------------------#
# EXECUÇÃO DA APLICAÇÃO                                  #
#--------------------------------------------------------#
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
