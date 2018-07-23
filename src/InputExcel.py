# -*- coding:utf-8 -*-

"""
将数据重新整理到一维数组
"""

import re
from openpyxl import load_workbook



class DateController(object):
    def excelInput(filearray):
        lenlist = len(filearray)
        i = []
        m = 0
        n = 1
        excel = load_workbook('./file/1.xlsx')
        sheet = excel['Sheet1']

        for i in filearray:
            sheet.append(i)
            excel.save('./file/2.xlsx')




