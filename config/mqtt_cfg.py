# -*- coding: utf-8 -*-
"""
Time:2022/8/22 18:06
Author:CAOZHENG
File:mqtt_cfg.py
"""

import random

# mqtt代理服务器地址
HOST = '192.168.233.235'
# 代理端口
PORT = 2883
# 与代理通信之间允许的最长时间段（以秒为单位）
KEEPALIVE = 60
# 消息主题
TOPIC = "up/cmd/#"
# 不能重复的 id
CLIENT_ID = f'python-mqtt-{random.randint(0, 1000)}'
# mqtt账号
USERNAME = 'yele'
# mqtt密码
PASSWORD = 'admin'
