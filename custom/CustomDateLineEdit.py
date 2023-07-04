from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QLineEdit
from datetime import datetime


class CustomDateLineEdit(QLineEdit):
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
            day, month, year = 0, 0, 0 
            try:
                day, month, year = map(int, (text[:2], text[2:4], text[4:]))
                if len(text) == 6:  # Verifica se o ano possui 6 dígitos
                    if year >=35:
                        year = 1900 + year  # Supõe que os dois primeiros dígitos são 19XX
                    else:
                        year = 2000 + year  # Supõe que os dois primeiros dígitos são 20XX
                date_string = f"{day:02d}/{month:02d}/{year:04d}"
                datetime.strptime(date_string, "%d/%m/%Y")
                self.setText(date_string)                
            except (ValueError, TypeError):
                self.clear()
