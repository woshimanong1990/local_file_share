# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
import sys
from PyQt5 import QtWidgets
from file_select_dialog import FileSelectQtWidget


def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = FileSelectQtWidget()
    main_window.show()
    app.exec_()


if __name__ == '__main__':
    main()
