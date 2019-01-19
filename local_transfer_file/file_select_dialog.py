# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
import os
import json
import traceback
import logging

from PyQt5.QtWidgets import QMainWindow,  QMessageBox, QFileDialog
import qrcode


from local_transfer_file.ui_files.UI_fileSelectDialog import Ui_MainWindow
from local_transfer_file.select_ip_dialog import SelectIPDialog
from local_transfer_file.utils import FileMode, get_auth_code
from local_transfer_file.show_qr_code_dialog import ShowQRCodeDialog

logger = logging.getLogger()


class FileSelectQtWidget(QMainWindow):
    def __init__(self, port, hosts, parent=None):
        super().__init__(parent)
        self.file_path = None
        self.file_mode = FileMode.FILEMODE
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.server_port = port
        self.hosts = hosts
        self.need_show_again = True
        self.select_ip = None
        self.init_menu_action()

    def softwareDetail(self):
        QMessageBox.information(self, "软件说明", "1. 需要手机和电脑在一个网络中，wifi同处一个网段中。\n 2. 尽量不要分享文件夹\n 3. 注意保护个人隐私，造成的法律后果由使用者承担\n 4. 仅供学习使用，请勿商用")

    def sotfwareVersion(self):
        QMessageBox.information(self, "软件版本", "版本号：0.0.1")

    def aboutMe(self):
        QMessageBox.information(self, "关于", "一个会点编程的小蚂蚁")

    def init_menu_action(self):
        self.ui.action.triggered.connect(self.softwareDetail)
        self.ui.action_2.triggered.connect(self.sotfwareVersion)
        self.ui.action_3.triggered.connect(self.aboutMe)

    def set_config(self, code, file_path):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        config_file = os.path.join(current_dir, "service/config.json")
        data = {
                "file_path": file_path,
                "code": code
        }
        try:
            with open(config_file, 'a+') as f:
                f.seek(0, 0)
                old_content = f.read()
                old_data = {}
                if old_content:
                    old_data = json.loads(old_content)
                    f.truncate(0)
                old_data.update(data)
                json.dump(old_data, f, indent=4, sort_keys=True)
                return True
        except PermissionError as e:
            QMessageBox.critical(self, "保存配置失败！ 权限不足，无法写入文件")
            return False
        except Exception as e:

            QMessageBox.information(self, "保存配置失败！未知错误")
            return False

    def generateQRCode(self):
        try:
            button = QMessageBox.warning(self, "警告！", "新产生的二维码将导致之前的失效，确定继续吗？", QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Ok)
            if button == QMessageBox.Cancel:
                return
            if not self.file_path:
                QMessageBox.critical(self,"错误", "文件（夹） 为空")
                return
            if not self.hosts:
                QMessageBox.critical("无法获取IP地址，请确认您的设备是否联网")
                return
            if len(self.hosts) > 1 and self.need_show_again:
                dialog = SelectIPDialog(self.hosts)
                dialog.show_again_signal.connect(self.setShowAgain)
                dialog.exec_()
                self.select_ip = dialog.selected_ip
            else:
                self.select_ip = self.hosts[0]
            auth_code = get_auth_code()
            show_content = "http://{}:{}/download_file?file_path={}&code={}".format(self.select_ip, self.server_port, self.file_path, auth_code)
            result = self.set_config(auth_code, self.file_path)
            if not result:
                return
            self.ui.showUrlText.setText(show_content)
            img = qrcode.make(show_content)
            dialog = ShowQRCodeDialog(self)
            dialog.set_image(img)
            dialog.exec_()
        except:
            logger.error("generate code error", exc_info=True)
            traceback.print_exc()

    def selectFilePath(self):
        if self.file_mode == FileMode.FILEMODE:
            file_name, _ = QFileDialog.getOpenFileName(self, "请选择文件")
            self.file_path = file_name
        else:
            self.file_path = QFileDialog.getExistingDirectory(self, "请选择文件夹")

        self.ui.showFilePath.setText(self.file_path)

    def closeWindow(self):
        self.close()

    def selectFileMode(self):
        sender = self.sender()
        button = sender.checkedButton()
        object_name = button.objectName()
        self.file_mode = FileMode.FILEMODE if object_name == "fileMode" else FileMode.DIRECTORMODE
        if self.file_mode == FileMode.DIRECTORMODE:
            QMessageBox.warning(self, "警告", "出于安全考虑，请尽量不要分享文件夹，可以打包后分享或者下载！")
        self.ui.showFilePath.clear()

    def setShowAgain(self, isNotShowAgain):
        self.need_show_again = not isNotShowAgain

