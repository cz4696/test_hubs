# -*- coding: utf-8 -*-
"""
Time:2022/8/22 14:45
Author:CAOZHENG
File:base_page.py
"""

import os
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from config import automation_cfg


class BasePage(object):
    """
    基础页面元素封装
    """

    def __init__(self, driver):
        self.driver = driver

    def webdriver(self, browser):
        """
        选择浏览器
        :param browser: 浏览器
        :return:
        """
        if browser.lower() == "chrome":
            self.driver = webdriver.Chrome()
        elif browser.lower() == "firefox":
            self.driver = webdriver.Firefox()
        elif browser.lower() == "edge":
            self.driver = webdriver.Edge()
        elif browser.lower() == "ie":
            self.driver = webdriver.Ie()

    def maximize(self):
        """
        最大化窗口，maximize_windows()会造成 driver超时
        :return:
        """
        # self.driver.maximize_windows()
        self.driver.set_window_size(800, 1000)

    def find_element(self, *loc):
        """
        定位方法
        :param loc:
        :return:
        """
        return self.driver.find_element(*loc)

    def send_keys(self, *loc, text):
        """
        send_keys
        :return:
        """
        self.driver.find_element(*loc).send_keys(text)

    def click(self, *loc):
        """
        单击操作
        :return:
        """
        self.driver.find_element(*loc).click()

    def doubleclick(self, *loc):
        """
        双击操作
        :return:
        """
        self.driver.find_element(*loc).doubleclick()

    def switch_frame(self, *loc):
        """
        进入frame
        :return:
        """
        iframe = self.driver.find_element(*loc)
        self.driver.switch_to.frame(iframe)

    def back_frame(self, *loc):
        """
        退出 frame
        :return:
        """
        iframe = self.driver.find_element(*loc)
        self.driver.switch_to.default_content(iframe)

    def current_handle(self):
        """
        获取当前窗口句柄
        :return:
        """
        self.driver.current_window_handle()

    def all_handle(self):
        """
        获取所有窗口句柄
        :return:
        """
        return self.driver.window_handles()

    def switch_handle(self):
        """
        切换句柄
        :return:
        """
        all_handle = self.driver.window_handles()
        self.driver.switch_to.window(all_handle[0])

    def forword(self):
        """
        浏览器前进
        :return:
        """
        self.driver.forword()

    def back(self):
        """
        浏览器后退
        :return:
        """
        self.driver.back()

    def refresh(self):
        """
        浏览器刷新
        :return:
        """
        self.driver.refresh()

    def title(self):
        """
        获取浏览器标题
        :return:
        """
        return self.driver.title()

    def close(self):
        """
        关闭当前 tab
        :return:
        """
        self.driver.close()

    def quit(self):
        """
        关闭整个浏览器
        :return:
        """
        self.driver.quit()

    def webdriver_wait(self):
        """
        显式等待
        :return:
        """
        return WebDriverWait(5, 0.5)

    def implicitly_wait(self):
        """
        隐式等待
        :return:
        """
        return self.driver.implicitly_wait(5)

    def screenshots(self):
        """
        截图,保存在 screenshots文件下
        :return:
        """

        time_str = time.strftime("%Y_%m_%d_%H_%M_%S")
        path = automation_cfg.SAVE_PATH
        screenshots_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                        path % time_str)
        self.driver.save_screenshot(screenshots_path)

    def screenshots_base(self):
        """
        base64,用于测试报告中显示截图
        :return:
        """
        return self.driver.get_screenshot_as_base64()
