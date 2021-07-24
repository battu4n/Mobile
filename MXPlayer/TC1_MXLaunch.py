import os
import unittest

from appium import webdriver
from time import sleep

class MXPlayer(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['platformVersion']='10.0'
        desired_caps['deviceName']='Galaxy M01 Core'
        desired_caps['appPackage'] = 'com.mxtech.videoplayer.ad'
        desired_caps['appActivity'] = '.ActivityWelcomeMX'
        desired_caps['autoAcceptAlerts']='true'
        self.driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
        sleep(10)
    def tearDown(self):
        self.driver.quit()
    def test_mxplayerlaunch(self):
        self.driver.find_element_by_xpath(".//android.widget.Button[@text='Allow']").click()
        sleep(5)
        if (self.driver.find_element_by_id('toolbar')).is_displayed():
            print("MX player launches successfully")
        else:
            print("MX player launch failed")

if __name__=='__main__':
    unittest.main()
