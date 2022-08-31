# -*- coding: utf-8 -*-
"""
Time:2022/8/22 13:25
Author:CAOZHENG
File:path_cfg.py
"""
import time

time_str = time.strftime("%Y_%m_%d_%H_%M_%S")

# 图片本地地址
GET_IMAGE = r'C:\\Users\OKAI\Pictures\\test\\' + time_str + '.png'
# 画图保存地址
ECHARTS_PATH = r'E:\test_hubs\screenshots\chart\\'
# WEB自动化用例地址
WEB_TEST_DIRS = "test_automation/web_automation/test_cases"
# WEB自动化报告地址
WEB_TEST_REPORT = "report/web_auto_report/Test_Report_%s.html" % time_str
# API自动化用例地址
API_TEST_DIRS = "test_automation/api_automation/test_cases"
# API自动化报告地址
API_TEST_REPORT = "report/api_auto_report/Test_Report_%s.html" % time_str
