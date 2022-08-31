# -*- coding: utf-8 -*-
"""
Time:2022/8/23 13:57
Author:CAOZHENG
File:send_email.py
"""

import yamail
from config import email_cfg


def send_email(report_url):
    """
    发送邮件
    :param report_url: 测试报告地址
    :return:
    """
    try:
        yam = yamail.SMTP(user=email_cfg.SENDER_USERNAME, password=email_cfg.SENDER_PASSWORD, host=email_cfg.HOST)
        yam.send(to=email_cfg.RECIPIENT_USERNAME, subject=email_cfg.SUBJECT, contents=email_cfg.CONTENTS,
                 attachments=report_url)
        print('send success!')
        yam.close()
    except Exception as e:
        print('send fail!', e)
