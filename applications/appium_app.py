from appium import webdriver
from pages.contact_manager_helper import CMHelper
from applications.properties import Properties as Pr
from config import BASE_URL


class App:

    def __init__(self):
        desired_caps = Pr.ANDROID_EMULATOR

        self.driver = webdriver.Remote(BASE_URL, desired_caps)
        self.ap = CMHelper(self)

    def destroy(self):
        print("closed")
        self.driver.quit()
