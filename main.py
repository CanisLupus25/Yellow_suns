import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from Yellow_suns import Ui_MainWindow


class Yellow_sun(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Yellow_sun()
    window.show()
    exit(app.exec())
