# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
from enum import Enum
import socket
import uuid
import os
import logging
import logging.config
import json
import sys

import psutil


class FileMode(Enum):
    FILEMODE = 1
    DIRECTORMODE = 2


def get_local_ip():
    info = psutil.net_if_addrs()
    ip_list = []
    for k, v in info.items():
        for item in v:
            if item.family == socket.AddressFamily.AF_INET:
                ip_list.append(item.address)
    ip_list.remove("127.0.0.1")
    return ip_list


def get_auth_code():
    return str(uuid.uuid1()).replace("-", "")


def setup_logging(
    default_path=None,
    default_level=logging.INFO,
    env_key='LOG_CFG'
):
    """Setup logging configuration

    """
    if default_path is None:
        if getattr(sys, 'frozen', False):
            bundle_dir = sys._MEIPASS
            default_path = os.path.join(bundle_dir, "logging.json")
        else:
            bundle_dir = os.path.dirname(os.path.abspath(__file__))

            default_path = os.path.join(bundle_dir, "logging.json")
        # default_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logging.json")
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)





