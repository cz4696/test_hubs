# -*- coding: utf-8 -*-
"""
Time:2022/8/29 15:37
Author:CAOZHENG
File:read_excel.py
"""

import time
import xlrd
import xlutils.copy
from config import ddt_cfg


class ReadExcel:
    def __init__(self, filename, sheet=0):
        self.filename = filename
        workbook = xlrd.open_workbook((ddt_cfg.FILEPATH + self.filename))
        self.table = workbook.sheets()[sheet]

    def get_rows(self, row):
        rows = self.table.row_values(row)

        print(rows)
        return rows

    def get_cell(self, row, col):
        """
        获取单元格数据
        :param row: 行
        :param col: 列
        :return:
        """
        cell_data = self.table.cell(row, col).value
        print(cell_data)
        return cell_data

    def get_col(self, col):
        """
        获取整列数据
        :param col: 列
        :return:
        """
        col_data = self.table.col_values(col)
        print(col_data)
        return col_data


class WriteExcel:
    def __init__(self, filename, sheet=0):
        """

        :param sheet: 默认为0
        :param filename:
        """
        self.filename = filename
        self.workbook = xlrd.open_workbook(ddt_cfg.FILEPATH + self.filename)
        self.wf = xlutils.copy.copy(self.workbook)
        self.ws = self.wf.get_sheet(sheet)

    def set_cell(self, row, col, value):
        """
        写数据到表格
        :param row: 行
        :param col: 列
        :param value: 输入的值
        :return:
        """
        self.ws.write(row, col, value)
        self.wf.save(ddt_cfg.FILEPATH + self.filename)

    def save_excel(self, filename, format):
        # 获取当前时间
        self.time = time.strftime("%Y%m%d%H%M%S", time.localtime())
        # 生成文件的文件名及格式
        self.report = filename + '_' + self.time + format
        # 保存文件
        self.wf.save(self.report)


if __name__ == "__main__":
    read = ReadExcel('test_data.xls')
    # read.get_col(1)
    # read.get_rows(1)
    write = WriteExcel('test_data.xls')
    write.set_cell(3, 4, 'hello,world')
    read.get_cell(3, 4)
