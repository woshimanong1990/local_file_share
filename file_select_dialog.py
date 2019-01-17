# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
from PyQt5.QtWidgets import QWidget, QMainWindow,  QMessageBox, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets

from UI_fileSelectDialog import Ui_MainWindow


class FileSelectQtWidget(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.file_path = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def generateQRCode(self):
        if not self.file_path:
            button = QMessageBox.critical(self,"错误", "文件（夹） 为空")
            print(button)
            return

    def selectFilePath(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                "All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files)

    def closeWindow(self):
        self.close()