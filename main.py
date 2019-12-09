__author__ = 'Llorenç Suau Cànaves'
__copyright__ = 'Copyright (c) 2019. All rights are reserved.'
__license__ = 'GPL 3 or better'

from PyQt5 import QtWidgets
from mainWindow import MainWindow

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dlMain = MainWindow()
    dlMain.show()
    sys.exit(app.exec_())
