# -*- coding: utf-8 -*-
"""
Time:2022/8/26 14:10
Author:CAOZHENG
File:read_yaml.py
"""

import yaml
from config import ddt_cfg


def read_yaml(filename):
    """
    解析.yaml文件
    :return:
    """
    file = open(ddt_cfg.FILEPATH + filename, 'r', encoding=ddt_cfg.ENCODING)
    data = yaml.load(file, Loader=yaml.FullLoader)
    print(data)
    file.close()
    return data


if __name__ == '__main__':
    read_yaml('data.yml')
