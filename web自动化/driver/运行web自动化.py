#!/usr/bin/python
#-*- coding;utf-8 -*_
#Author:朱浩龙
#明明你也最爱我,没理由爱不到结果,只要你敢不懦弱,凭什么我们要错过
import unittest
import HTMLTestRunnertest
from web自动化.test.建立snat策略 import 新建策略1

if __name__=='__main__':
    suit=unittest.TestSuite()
    suit.addTest(unittest.makeSuite(新建策略1))
    f = open(r'e:/demo/web自动化/report/ab.html','wb')
    runner=HTMLTestRunnertest.HTMLTestRunner(tester='朱浩龙',description='结果如下',title='防火墙web自动化',stream=f)
    runner.run(suit)
    f.close()
