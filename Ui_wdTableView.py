# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\PyProjects\gon_json\wdTableView.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tvEditor(object):
    def setupUi(self, tvEditor):
        tvEditor.setObjectName("tvEditor")
        tvEditor.resize(747, 586)
        self.gridLayout = QtWidgets.QGridLayout(tvEditor)
        self.gridLayout.setObjectName("gridLayout")
        self.tableView = QtWidgets.QTableView(tvEditor)
        self.tableView.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.tableView.setFrameShape(QtWidgets.QFrame.VLine)
        self.tableView.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 1)

        self.retranslateUi(tvEditor)
        QtCore.QMetaObject.connectSlotsByName(tvEditor)

    def retranslateUi(self, tvEditor):
        _translate = QtCore.QCoreApplication.translate
        tvEditor.setWindowTitle(_translate("tvEditor", "Editor"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tvEditor = QtWidgets.QWidget()
    ui = Ui_tvEditor()
    ui.setupUi(tvEditor)
    tvEditor.show()
    sys.exit(app.exec_())
