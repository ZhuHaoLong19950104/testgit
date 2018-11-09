#!/usr/bin/python
#-*- coding;utf-8 -*_
#Author:朱浩龙
#明明你也最爱我,没理由爱不到结果,只要你敢不懦弱,凭什么我们要错过
import xlrd
class duqu():
    def du(self):
        d=[]
        f = xlrd.open_workbook(r'e:\demo\web自动化\data\web自动化.xlsx')
        sheet = f.sheets()[0]
        a = sheet.nrows
        for i in range(a):
            b = sheet.row_values(i)
            d.append(b)
        return d
