from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit


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