#!/usr/bin/python
#-*- coding;utf-8 -*_
#Author:朱浩龙
#明明你也最爱我,没理由爱不到结果,只要你敢不懦弱,凭什么我们要错过
from appium import webdriver
import unittest
from app框架.data.读取 import duqu
from app框架.config.网易云 import wangyiyun
c=wangyiyun()
a=duqu()
b=a.du()
class app测试(unittest.TestCase):
    def test_1(self):
        self.assertEqual(c.denglu(b[0]),b[0][3])
    def test_2(self):
        self.assertEqual(c.denglu(b[1]),b[1][3])
    def test_3(self):
        self.assertEqual(c.denglu(b[2]),b[2][3])
