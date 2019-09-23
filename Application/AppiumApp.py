from appium import webdriver
from Page.CMPage import CMHelper
from Application.Properties import test_data

class App:

    def __init__(self):
        desired_caps = test_data.ANDROID_EMULATOR

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.ap = CMHelper(self)


    def destroy(self):
        print("closed")
        self.driver.quit()
