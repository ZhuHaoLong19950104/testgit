#!/usr/bin/python
#-*- coding;utf-8 -*_
#Author:朱浩龙
#明明你也最爱我,没理由爱不到结果,只要你敢不懦弱,凭什么我们要错过
from appium import webdriver
from time import sleep
a ={}
a['platformName'] = 'Android'
a['deviceName'] = '127.0.0.1:62001'
a['appPackage'] = 'com.baidu.input'
a['appActivity'] = 'ImeAppMainActivity'

driver =webdriver.Remote('http://localhost:4723/wd/hub',a)
sleep(2)
driver.find_element_by_id('com.baidu.input:id/setdefault').click()
sleep(2)
driver.find_element_by_class_name('android.widget.LinearLayout').click()
driver.find_element_by_id('com.baidu.input:id/finishsetting').click()
sleep(5)
driver.quit()