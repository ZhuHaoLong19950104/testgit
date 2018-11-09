#!/usr/bin/python
#-*- coding;utf-8 -*_
#Author:朱浩龙
#明明你也最爱我,没理由爱不到结果,只要你敢不懦弱,凭什么我们要错过
import HTMLTestRunnertest
from app框架.test.app用例 import app测试
import unittest
if __name__=='__main__':
    suit =unittest.TestSuite()
    suit.addTest(unittest.makeSuite(app测试))
    f = open(r'E:\demo\app框架\report\a.html','wb')
    runner = HTMLTestRunnertest.HTMLTestRunner(tester='朱浩龙', description='结果如下', title='网易云登录测试', stream=f)
    runner.run(suit)
    f.close()

