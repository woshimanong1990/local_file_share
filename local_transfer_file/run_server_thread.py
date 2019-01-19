# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function

import socket
from contextlib import closing

from PyQt5.QtCore import QThread

from local_transfer_file.service import app


class CustomServerThread(QThread):
    def __init__(self):
        self.server_port = 5000
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def get_free_port(self):
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        # print("Hostname :  ", host_name, host_ip)
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
                s.bind(('', 0))
                return s.getsockname()[1]

    def run(self):
        self.server_port = self.get_free_port()
        app.run(self.server_port)
