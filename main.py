import sys
from random import randint

from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QMainWindow, QApplication

from Yellow_suns import Ui_MainWindow


class Yellow_sun(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.drawIt)
        self.x, self.y = 50, 50
        self.r = 50

    def drawIt(self):
        self.x, self.y = randint(0, 800), randint(0, 600)
        self.r = randint(5, 200)
        self.update()

    def paintEvent(self, event: QPainter):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(255, 255, 20))
        qp.drawEllipse(QPointF(self.x, self.y), self.r, self.r)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Yellow_sun()
    window.show()
    exit(app.exec())
