# -*- coding: utf-8 -*-
"""
Time:2022/8/22 18:12
Author:CAOZHENG
File:login_page.py
"""

from common.read_yaml import read_yaml
from test_automation.web_automation.test_page.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    """
    登录页面
    """

    input_msg = (By.ID, 'kw')
    click_btn = (By.ID, 'su')
    data = read_yaml('data.yml')

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def open_browser(self):
        self.driver.get("https://www.baidu.com")

    def input(self, msg):
        self.send_keys(*self.data['By.id']['kw'], text=msg)

    def click_element(self):
        self.click(*self.click_btn)

    def web_wait(self):
        self.webdriver_wait().until(self.find_element(*self.click_btn))
