# -*- coding: utf-8 -*-
"""
Time:2022/8/29 14:37
Author:CAOZHENG
File:log_test.py
"""

import requests
from nb_log import get_logger

get_logger('urllib3')
re = requests.get('https://www.baidu.com')
