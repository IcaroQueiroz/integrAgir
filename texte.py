from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QWidget
from PyQt5.QtCore import Qt


class CustomLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.focusNextChild()
            self.formatarTexto()
        else:
            super().keyPressEvent(event)

    def formatarTexto(self):
        text = self.text()
        if text:
            try:
                value = float(text.replace('.', '').replace(',', '.'))
                formatted_text = f"{value:,.2f}".replace(',', '*').replace('.', ',').replace('*', '.')
                self.setText(formatted_text)
            except ValueError:
                pass


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.lineEdit1 = CustomLineEdit(self)
        self.lineEdit2 = CustomLineEdit(self)

        self.setupUI()

    def setupUI(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Exemplo")

        self.lineEdit1.setGeometry(50, 50, 200, 30)
        self.lineEdit2.setGeometry(50, 100, 200, 30)


app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
