import sys, os
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow
)





class MainUi_Form(object):
    def setupUI(self, MainWindow):
        pass


class Main(QMainWindow, MainUi_Form):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent) 
        self.setupUI(self)       


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(resource_path('pictures/spotiApp.ico')))
    ex = Main()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()