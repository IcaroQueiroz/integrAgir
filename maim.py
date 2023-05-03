from interface import *
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
#--------------------------------------------------------#
# CLASS MAIN WINDOWS                                    #
#--------------------------------------------------------#
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
#--------------------------------------------------------#
# EXECUÇÃO DA APLICAÇÃO                                  #
#--------------------------------------------------------#
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
