# -*- coding:utf-8 -*-

import re
""""
文件操作与处理
"""


class ReadLogs:
    def __init__(self, filepath):
        self.file = filepath

    """"
    读取日志文件
    """
    def readlogsfile(self):
        try:
            r = open(self.file, 'r', encoding='UTF-8')
            lines = r.readlines()
            l2 = []
            for line in lines:
                line = line.strip('\n')
                p = re.compile(r'\s')
                l1 = p.split(line)
                l2.append(l1)
        except ZeroDivisionError as e:
            print('except:', e)
        finally:
            r.close()
            return l2


"""
从列表提取工作流，开始时间，结束时间s
"""
class ProcFile:
    def __init__(self, filearray):
        self.arry = filearray

    def procfile(self):
        li = self.arry
        del li[0:8]
        lenli = len(li)
        i = 0
        list1 =[]
        while i < lenli:
            list2 = []
            del li[i][0]
            del li[i][0]
            del li[i][1]
            del li[i][3]
            name = li[i][0]
            begintime = li[i][1]+' '+li[i][2]
            endtime = li[i][3]+' '+li[i][4]
            list2.append(name)
            list2.append(begintime)
            list2.append(endtime)
            list1.append(list2)
            i = i + 1

        return list1


#测试
if __name__ == '__main__':
    filepath = '../file/etl_logs.txt'
    ll = ReadLogs(filepath)
    print(ll.readlogsfile())
    ll2 = ProcFile(ll.readlogsfile())
    print(ll2.procfile())
