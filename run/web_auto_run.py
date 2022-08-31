# -*- coding: utf-8 -*-
"""
Time:2022/8/23 13:40
Author:CAOZHENG
File:web_auto_run.py
"""

from tools.XTestRunner import HTMLTestRunner
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
    test_dirs = path_cfg.WEB_TEST_DIRS
    suite = unittest.TestSuite()
    for item in test_dirs:
        case_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), item).replace('\\', '/')
        discover = unittest.TestLoader().discover(start_dir=case_path, pattern="test_*.py",
                                                  top_level_dir=None)
        suite.addTest(discover)
    # HTMLTestRunner
    filename = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                            path_cfg.WEB_TEST_REPORT).replace('\\', '/')

    with(open(filename, 'wb')) as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title='Automation Test Report',
            tester=tester,
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
    # 执行前修改 tester为自己
    tester = 'cao zheng'
    run_case()
