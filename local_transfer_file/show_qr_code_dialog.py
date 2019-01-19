# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
import logging

from PyQt5.QtWidgets import QDialog, QMessageBox, QFileDialog
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5 import QtGui
from PyQt5 import QtCore
from PIL.ImageQt import ImageQt

from local_transfer_file.ui_files.UI_showQRCode import Ui_Dialog

logger = logging.getLogger()


class ShowQRCodeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.qr_image = None

    def set_image(self, image):
        qim = ImageQt(image)
        pix = QtGui.QPixmap.fromImage(qim)
        self.qr_image = pix.scaled(400, 400, QtCore.Qt.KeepAspectRatio)
        screen = QGraphicsScene()
        screen.addPixmap(self.qr_image)
        self.ui.graphicsView.setScene(screen)

    def savePicture(self):
        try:
            if not self.qr_image:
                QMessageBox.critical(self, "错误", "不能保存文件")
                return
            file_path, _ = QFileDialog.getSaveFileName(self, "请选择保存位置", "qrcode.png", "Images (*.png *.xpm *.jpg)")
            # print(file_path)
            if not file_path:
                QMessageBox.critical(self, "警告", "请选择保存路径")
                return
            self.qr_image.save(file_path, "PNG")
            QMessageBox.information(self, "保存成功", "保存路径：{}".format(file_path))
        except:
            logger.error("save error", exc_info=True)
