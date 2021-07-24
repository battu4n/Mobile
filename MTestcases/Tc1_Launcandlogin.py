from appium import webdriver

import time

"""
Desired capabilities
"""
desired_cap={
    "deviceName": "Galaxy M01 Core",
    "appActivity": "com.google.android.gm.welcome.WelcomeTourActivity",
    "appPackage": "com.google.android.gm",
     "platformVersion": "10",
    "platformName":"Android"


}


#Create the driver instance



