# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot, QModelIndex
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
        self.open_tabs = list()
        self.tabWidget.tabCloseRequested.connect(self.close_tab)
    
    @pyqtSlot()
    def on_actionOpen_triggered(self):
        """
        Slot documentation goes here.
        """
        files_filter = 'JSON (*.json);;Translation files (*.pik)'
        self.file, filter_set = QFileDialog.getOpenFileName(self, 'Open JSON/pik file', filter=files_filter)
        #file_tab = QWidget()
        file_name = Path(self.file).name
        tveditor = tvEditor(self.tabWidget, self.file)
        self.open_tabs.append(tveditor)
        self.tabWidget.addTab(tveditor, str(file_name))
        self.actionCleanup.setEnabled(True)
        self.actionSave.setEnabled(True)
        self.tabWidget.setCurrentIndex(-1)
        #self.tabWidget.setLayout(QtWidgets.QVBoxLayout(self.tabWidget))
        #tab_layout = QtWidgets.QVBoxLayout(file_tab)
        #tab_layout.addWidget(tveditor)
        #file_tab.setLayout(tab_layout)
    
    @pyqtSlot()
    def on_actionCleanup_triggered(self):
        """
        Slot documentation goes here.
        """
        for tab in self.open_tabs:
            tab.translator.cleanup_translation()
    
    @pyqtSlot()
    def on_actionSave_triggered(self):
        """
        Slot documentation goes here.
        """
        for table in self.open_tabs:
            
            for nrow in range(table.model.rowCount()):
                target_idx = table.tableView.model().index(nrow, 2)
                segment = table.tableView.model().index(nrow, 4).data()
                segment.target = table.tableView.indexWidget(target_idx).toPlainText()
                print(segment.target)
            table.translator.save_changes()
#            with open(table.translator.translation_file, 'rb') as fout:
#                import pickle
#                contents = pickle.load(fout, encoding='utf-8')
#                for row in contents:
#                    for segment in row.segments:
#                        print(segment.source, segment.target)

    def close_tab(self, current_idx: int):
        """
        """
        current_widget = self.tabWidget.widget(current_idx)
        current_widget.deleteLater()
        self.tabWidget.removeTab(current_idx)
        
        
        
