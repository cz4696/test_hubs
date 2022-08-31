# -*- coding: utf-8 -*-
"""
Time:2022/8/22 13:35
Author:CAOZHENG
File:log.py
"""

import logging
import os
import time

log_path = os.path.join(os.path.dirname(__file__), '../logs')

if not os.path.exists(log_path):
    os.mkdir(log_path)


class Log:
    def __init__(self):
        """
        日志记录
        """
        self.log_name = os.path.join(log_path, '{0}.log'.format(time.strftime('%Y-%m-%d')))

    def test_log(self, level, message):
        # 创建一个 logger
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        # 创建一个 handler，用于写入日志文件
        fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8')
        fh.setLevel(logging.DEBUG)

        # 再创建一个 handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义 handler 的输出格式
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给 logger 添加 handler
        logger.addHandler(fh)
        logger.addHandler(ch)

        if level == 'info':
            logger.info(message)
        elif level == 'debug':
            logger.debug(message)
        elif level == 'warning':
            logger.warning(message)
        elif level == 'error':
            logger.error(message)
        elif level == 'critical':
            logger.critical(message)
        logger.removeHandler(ch)
        logger.removeHandler(fh)
        fh.close()

    def debug(self, message):
        """
        所有日志

        :param message:
        :return:
        """
        self.test_log('debug', message)

    def info(self, message):
        """
        事件日志

        :param message:
        :return:
        """
        self.test_log('info', message)

    def warning(self, message):
        """
        警告日志

        :param message:
        :return:
        """
        self.test_log('warning', message)

    def error(self, message):
        """
        报错日志

        :param message:
        :return:
        """
        self.test_log('error', message)

    def critical(self, message):
        """
        严重日志

        :param message:
        :return:
        """
        self.test_log('critical', message)


if __name__ == '__main__':
    test_log = Log()
    test_log.debug('test debug')
    test_log.info('test info')
    test_log.warning('test warning')
    test_log.error('test error')
    test_log.critical('test critical')
