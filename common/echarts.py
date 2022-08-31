# -*- coding: utf-8 -*-
"""
Time:2022/8/30 10:08
Author:CAOZHENG
File:echarts.py
"""

import time
from config import path_cfg
from pyecharts.charts import Bar, Line, Pie
from snapshot_phantomjs import snapshot
from pyecharts.render import make_snapshot


class Echarts:

    def __init__(self):
        self.time_str = time.strftime("%Y_%m_%d_%H_%M_%S")

    def histogram(self, chart_name):
        """
        柱状图
        :param chart_name: 图片保存名称
        :return:
        """
        bar = Bar()
        version = ['1.0.0', '1.0.1', '1.1.0', '1.1.1', '1.1.2']
        bug_num = [4, 8, 10, 11, 16]
        bar.add_xaxis(version)
        bar.add_yaxis('xxx项目bug', bug_num)
        make_snapshot(snapshot, bar.render(), path_cfg.ECHARTS_PATH + chart_name + self.time_str + '.png')

    def line_chart(self, chart_name):
        """
        折线图(可用于一二轮测试 bug数对比)
        :param chart_name: 图片保存名称
        :return:
        """

        version = ['1.0.0', '1.0.1', '1.1.0', '1.1.1', '1.1.2']
        first_test = [4, 8, 10, 11, 16]
        last_test = [2, 3, 6, 5, 7]
        line = Line()
        line.add_xaxis(xaxis_data=version)
        line.add_yaxis(series_name='第一轮测试', y_axis=first_test, is_symbol_show=True)
        line.add_yaxis(series_name='第二轮测试', y_axis=last_test, is_symbol_show=True)
        make_snapshot(snapshot, line.render(), path_cfg.ECHARTS_PATH + chart_name + self.time_str + '.png')

    def pie_chart(self, chart_name):
        """
        饼图(可用于模块 bug占比)
        :param chart_name: 图片保存名称
        :return:
        """
        test_model = ['test1', 'test2', 'test3', 'test4']
        bug_num = [4, 1, 6, 8]
        pie = Pie()
        pie.add('饼图', [list(bug_num) for bug_num in zip(test_model, bug_num)])
        make_snapshot(snapshot, pie.render(), path_cfg.ECHARTS_PATH + chart_name + self.time_str + '.png')


if __name__ == "__main__":
    a = Echarts()
    a.histogram('bar_chart')
    a.line_chart('line_chart')
    a.pie_chart('pie_chart')
