# -*- coding:utf-8 -*-
from src.Readlogs import ReadLogs
from src.InputExcel import DateController

if __name__  ==  '__main__':
    filepath = './file/etl_logs.txt'
    ll = ReadLogs.readlogsfile(filepath)
    DateController.excelInput(ll)
