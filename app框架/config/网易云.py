#!/usr/bin/python
#-*- coding;utf-8 -*_
#Author:朱浩龙
#明明你也最爱我,没理由爱不到结果,只要你敢不懦弱,凭什么我们要错过
from appium import webdriver
from time import sleep
from app框架.config.日志 import Logger
class wangyiyun():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    # desired_caps['platformVersion'] = '5'
    desired_caps['deviceName'] = '127.0.0.1:62001'
    # desired_caps ['devicesname']  = '127.0.0.1:62001'
    desired_caps['appPackage'] = 'com.netease.cloudmusic'
    desired_caps['appActivity'] = 'activity.LoadingActivity'
    def denglu(self,wenjian):
        driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)

        sleep(2)
        driver.find_element_by_id('com.netease.cloudmusic:id/mc').click()
        sleep(2)
        driver.find_element_by_id('com.netease.cloudmusic:id/pa').click()
        sleep(2)
        driver.find_element_by_id('com.netease.cloudmusic:id/i3').send_keys(wenjian[0])
        driver.find_element_by_id('com.netease.cloudmusic:id/i1').send_keys(wenjian[1])
        driver.find_element_by_id('com.netease.cloudmusic:id/pa').click()
        print(wenjian[2])
        if wenjian[2] == '1':
            mm=driver.find_element_by_id('com.netease.cloudmusic:id/pa').text
            driver.quit()
            return mm
        elif wenjian[2] == '2':
            mm = driver.find_element_by_id('com.netease.cloudmusic:id/pa').text
            driver.quit()
            return mm
        else:
            sleep(2)
            driver.find_element_by_id('com.netease.cloudmusic:id/pf').click()
            sleep(2)
            wd = driver.find_element_by_id('com.netease.cloudmusic:id/aar').text
            driver.quit()
            return wd
import uiautomator2
uiautomator2.connect('127.0.0.1')