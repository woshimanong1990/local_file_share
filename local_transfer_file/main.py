# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
import sys
from PyQt5 import QtWidgets
from local_transfer_file.file_select_dialog import FileSelectQtWidget
from local_transfer_file.run_server_thread import CustomServerThread

from local_transfer_file.utils import get_local_ip, setup_logging


def main():
    setup_logging()
    thread = CustomServerThread()
    thread.start()
    app = QtWidgets.QApplication(sys.argv)
    main_window = FileSelectQtWidget(thread.server_port, get_local_ip())
    main_window.show()
    app.exec_()


if __name__ == '__main__':
    main()
