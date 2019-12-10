# -*- coding: utf-8 -*-

"""
Module implementing tvEditor.
"""

from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QWidget, QFrame, QTextBrowser, QTextEdit
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QPixmap

from Ui_wdTableView import Ui_tvEditor
from translate_json import FileTranslator

from pathlib import Path

class tvEditor(QWidget, Ui_tvEditor):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None, file: str=''):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(tvEditor, self).__init__(parent)
        self.setupUi(self)
        self.translator = FileTranslator(file)
        
        self.model = QStandardItemModel()
        self.tvHead = ['Key', 
                        'Source', 
                        'Target', 
                        'Status', 
                        'row']
        self.model.setColumnCount(len(self.tvHead))
        self.model.setHorizontalHeaderLabels(self.tvHead)
        self.tableView.setModel(self.model)
        self.tableView.setColumnHidden(4, True)
        self.tableView.resizeColumnsToContents()
        self.load_contents()

    def load_contents(self):
        """
        """
        nrow = self.model.rowCount()
        for row in self.translator.rows:
            for segment in row.segments:
                key = row.key
                source = segment.source
                target = segment.target
                is_translated = segment.is_translated
                source_browser = QTextBrowser()
                target_edit = QTextEdit()
                source_browser.setFrameShape(QFrame.NoFrame)
                source_browser.setText(source)
                target_edit.setText(target)
                target_edit.setFrameShape(QFrame.NoFrame)
                self.model.insertRow(nrow)
                # Alias for self.model.index
                idx_model = self.model.index
                self.model.setData(idx_model(nrow, 0), key)
                self.tableView.setIndexWidget(idx_model(nrow, 1), source_browser)
                self.tableView.setIndexWidget(idx_model(nrow, 2), target_edit)
                if is_translated:
                    self.model.setData(idx_model(nrow, 3), QPixmap(':/icons/Oxygen-Icons.org-Oxygen-Actions-games-endturn.ico'))
                else:
                    pass
                self.model.setData(idx_model(nrow, 4), segment)
                self.tableView.resizeColumnsToContents()
                self.tableView.resizeRowsToContents()

