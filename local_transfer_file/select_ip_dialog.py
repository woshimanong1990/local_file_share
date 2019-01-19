# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function


from PyQt5.QtWidgets import QDialog, QMessageBox, QRadioButton, QButtonGroup
from PyQt5.QtCore import pyqtSignal

from local_transfer_file.ui_files import UI_selectIPDialog


class SelectIPDialog(QDialog):
    show_again_signal = pyqtSignal(bool)

    def __init__(self, ip_list, parent=None):
        super().__init__(parent=parent)
        self.ip_list = ip_list
        self.ui = UI_selectIPDialog.Ui_Dialog()
        self.ui.setupUi(self)
        self.selected_ip = None
        self.init_ip_list()

    def init_ip_list(self):
        button_group = QButtonGroup(self)
        for i in self.ip_list:
            radio_button = QRadioButton(self)
            radio_button.setText(str(i))
            self.ui.verticalLayout.addWidget(radio_button)
            button_group.addButton(radio_button)
            button_group.buttonClicked.connect(self.ipContentChange)

    def selectIP(self):
        if not self.selected_ip:
            QMessageBox.critical(self, "请选择您的ip地址！", "ip地址为空")
            return
        self.accept()

    def get_selected_ip(self):
        pass

    def ipContentChange(self, button):
        self.selected_ip = button.text()

    def needShowAgain(self):
        sender = self.sender()
        self.show_again_signal.emit(sender.isChecked())
