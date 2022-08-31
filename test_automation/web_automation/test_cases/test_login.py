# -*- coding: utf-8 -*-
"""
Time:2022/8/22 14:04
Author:CAOZHENG
File:test_login.py
"""

import unittest
import warnings
from selenium import webdriver
from common import log
from test_automation.web_automation.test_page.login_page import LoginPage


class Login(unittest.TestCase):
    def setUp(self) -> None:
        self.logs = log.Log()
        self.logs.info("-------------------- 执行用例：%s --------------------" % self.__class__.__name__)
        warnings.simplefilter('ignore', ResourceWarning)
        self.driver = webdriver.Chrome()

    def tearDown(self) -> None:
        self.logs.info("-------------------- 用例完成：%s --------------------" % self.__class__.__name__)
        self.driver.close()

    def test_login(self):
        self.login = LoginPage(self.driver)
        self.login.open_browser()
        self.login.input(msg='selenium')
        self.login.click_element()
        # self.login.web_wait()
        self.login.implicitly_wait()
        # sleep(3)
        try:
            self.assertEqual('selenium_百度搜索', self.driver.title)
        except Exception as e:
            self.logs.error("-------------------- 用例执行失败：%s --------------------" % self.__class__.__name__)
            # images runner中需要向 images 列表中加入截图 base64 信息
            self.images.append(self.login.screenshots_base())
            raise AssertionError(e)


if __name__ == '__main__':
    unittest.main()
