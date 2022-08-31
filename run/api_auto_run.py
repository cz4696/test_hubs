# -*- coding: utf-8 -*-
"""
Time:2022/8/25 9:21
Author:CAOZHENG
File:api_auto_run.py
"""

from XTestRunner import HTMLTestRunner
import os
import time
import unittest
from common.send_email import send_email
from config import path_cfg


def run_case():
    """
    自动化用例主函数
    :return:
    """
    test_dirs = path_cfg.API_TEST_DIRS
    suite = unittest.TestSuite()
    time_str = time.strftime("%Y_%m_%d_%H_%M_%S")
    for item in test_dirs:
        case_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), item).replace('\\', '/')
        discover = unittest.TestLoader().discover(start_dir=case_path, pattern="test_*.py",
                                                  top_level_dir=None)
        suite.addTest(discover)
    # HTMLTestRunner
    filename = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                            path_cfg.API_TEST_REPORT).replace('\\', '/')

    with(open(filename, 'wb')) as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title='Automation Test Report',
            description=' ',
            language='en',
        )
        runner.run(
            testlist=suite,
            rerun=0,
            save_last_run=False
        )
        send_email(filename)


if __name__ == "__main__":
    run_case()
