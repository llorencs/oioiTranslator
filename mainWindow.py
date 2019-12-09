# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QFileDialog, qApp, QWidget
from PyQt5 import QtWidgets
from Ui_mainWindow import Ui_MainWindow

from wdTableView import tvEditor
from pathlib import Path

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.file = None
        self.actionQuit.triggered.connect(qApp.quit)
        self.open_tabs =list()
        self.tabWidget.tabCloseRequested.connect(self.close_tab)
    
    @pyqtSlot()
    def on_actionOpen_triggered(self):
        """
        Slot documentation goes here.
        """
        files_filter = 'JSON (*.json);;Translation files (*.pik)'
        self.file, filter_set = QFileDialog.getOpenFileName(self, 'Open JSON/pik file', filter=files_filter)
        file_tab = QWidget()
        file_name = Path(self.file).name
        tveditor = tvEditor(self.tabWidget, self.file)
        self.open_tabs.append(tveditor)
        self.tabWidget.addTab(file_tab, str(file_name))
        tab_layout = QtWidgets.QVBoxLayout(file_tab)
        tab_layout.addWidget(tveditor)
        file_tab.setLayout(tab_layout)
    
    @pyqtSlot()
    def on_actionCleanup_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_actionSave_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

    def close_tab(self, current_idx: int):
        """
        """
        current_widget = self.tabWidget.widget(current_idx)
        current_widget.deleteLater()
        self.tabWidget.removeTab(current_idx)
        
        
        
