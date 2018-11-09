#!/usr/bin/python
#-*- coding;utf-8 -*_
#Author:朱浩龙
#明明你也最爱我,没理由爱不到结果,只要你敢不懦弱,凭什么我们要错过
import xlrd
class duqu():
    def du(self):
        d=[]
        a =xlrd.open_workbook(r'E:\demo\app框架\data\app.xlsx')
        sheet =a.sheets()[0]
        b=sheet.nrows
        for i in range(b):
           f = sheet.row_values(i)
           d.append(f)
        return d
