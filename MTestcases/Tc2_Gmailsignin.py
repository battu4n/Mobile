
import unittest
from appium import webdriver
from time import sleep



class gmail(unittest.TestCase):
    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        #desired_caps['platformVersion'] = '8.1.0'
        desired_caps['deviceName'] = 'Android Emulator'
        # Returns abs path relative to this file and not cwd
        #desired_caps['app'] = os.path.abspath(
            #os.path.join(os.path.dirname(__file__), '/Users/battun/Downloads/gmail.apk'))
        desired_caps['appPackage'] = 'com.google.android.gm'
        desired_caps['appActivity'] = '.ConversationListActivityGmail'
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(10)
        if (self.driver.find_element_by_xpath("//android.widget.TextView[@text ='GOT IT']").is_displayed()):
            self.driver.find_element_by_xpath("//android.widget.TextView[@text ='GOT IT']").click()
        elif (self.driver.find_element_by_xpath("//android.widget.TextView[@text ='got it']").is_displayed()):
            self.driver.find_element_by_xpath("//android.widget.TextView[@text ='got it']").click()
        sleep(10)
        if (self.driver.find_element_by_xpath("//android.widget.TextView[@text ='TAKE ME TO GMAIL']")).is_displayed():
            self.driver.find_element_by_xpath("//android.widget.TextView[@text ='TAKE ME TO GMAIL']").click()
        elif (self.driver.find_element_by_xpath("//android.widget.TextView[@text ='take me to gmail']")).is_displayed():
            self.driver.find_element_by_xpath("//android.widget.TextView[@text ='take me to gmail']").click()
        """if (self.driver.find_element_by_xpath("//android.widget.Button[@text ='Next']")).is_displayed():
            self.driver.find_element_by_xpath("//android.widget.Button[@text ='Next']").click()
        elif (self.driver.find_element_by_xpath("//android.widget.Button[@text ='OK']")).is_displayed():
             self.driver.find_element_by_xpath("//android.widget.Button[@text ='OK']").click()"""

    def tearDown(self):
        self.driver.quit()

    def test_gmail_compose(self):
        sleep(10)
        """if (self.driver.find_element_by_xpath("//android.widget.TextView[@text ='GOT IT']").is_displayed()):
            self.driver.find_element_by_xpath("//android.widget.TextView[@text ='GOT IT']").click()
        elif (self.driver.find_element_by_xpath("//android.widget.TextView[@text ='got it']").is_displayed()):
            self.driver.find_element_by_xpath("//android.widget.TextView[@text ='got it']").click()
        sleep(10)
        if (self.driver.find_element_by_xpath("//android.widget.TextView[@text ='TAKE ME TO GMAIL']")).is_displayed():
            self.driver.find_element_by_xpath("//android.widget.TextView[@text ='TAKE ME TO GMAIL']").click()
        elif (self.driver.find_element_by_xpath("//android.widget.TextView[@text ='take me to gmail']")).is_displayed():
            self.driver.find_element_by_xpath("//android.widget.TextView[@text ='take me to gmail']").click()
        if (self.driver.find_element_by_xpath("//android.widget.Button[@text ='Next']")).is_displayed():
            self.driver.find_element_by_xpath("//android.widget.Button[@text ='Next']").click()
        elif (self.driver.find_element_by_xpath("//android.widget.Button[@text ='OK']")).is_displayed():
             self.driver.find_element_by_xpath("//android.widget.Button[@text ='OK']").click()"""

        sleep(5)
        compose = self.driver.find_element_by_xpath("//android.widget.ImageButton[contains(@resource-id,'compose_button')]").click()

        sleep(5)
        got_it = self.driver.find_element_by_xpath("//android.widget.Button[@text ='Got it']").click()
        sleep(5)
        to_mail = self.driver.find_element_by_xpath("//android.widget.MultiAutoCompleteTextView[contains(@resource-id,'to')]").send_keys("battu4n@gmail.com")
        compose_mail = self.driver.find_element_by_xpath("//android.widget.EditText[@text = 'Compose email']")
        compose_mail.send_keys("Narendra learning mobile testing with pycharm")
    def test_gmail_reply(self):
        sleep(10)
        """gotit = self.driver.find_element_by_xpath("//android.widget.TextView[@text ='GOT IT']").click()
        sleep(10)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text ='TAKE ME TO GMAIL']").click()
        self.driver.find_element_by_xpath("//android.widget.Button[@text ='Next']").click()
        self.driver.find_element_by_xpath("//android.widget.Button[@text ='OK']").click()"""
        sleep(10)
        reply = self.driver.find_element_by_id("snippet").click()

        sleep(15)
        #self.driver.find_element_by_xpath("//android.widget.ImageView[@content-desc ='Reply']").click()
        self.driver.find_element_by_id("reply").click()
        sleep(15)
        if (self.driver.find_element_by_xpath("//android.widget.Button[@text ='Got it']")).is_displayed():
            self.driver.find_element_by_xpath("//android.widget.Button[@text ='Got it']").click()
        else:
            self.driver.find_element_by_xpath("//android.widget.Button[@text ='GOT IT']").click()
        sleep(10)
        self.driver.find_element_by_id("wc_body").send_keys("Narendra learning mobile testing with pycharm")
        self.driver.find_element_by_id("send").click()
        if (self.driver.find_element_by_id("delete")).is_displayed():
            print("Reply message sent successfully to request mail id ")

# ---START OF SCRIPT
if __name__ == '__main__':
    #suite = unittest.TestLoader().loadTestsFromTestCase(gmail)
    #unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()