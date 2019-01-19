# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
import os
import logging
from http.server import  HTTPServer

from .request_handler import CustomRequestHanlder




def run(port):
    httpd = HTTPServer(("0.0.0.0", port), CustomRequestHanlder)
    # print(httpd.server_port, httpd.server_name)
    httpd.serve_forever()
