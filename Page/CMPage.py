from selenium.webdriver.common.by import By
import time

class CMHelper():
    global warning_text
    warning_text = "This app was built for an older version of Android and may not work properly. " \
               "Try checking for updates, or contact the developer."

    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

    def warning(self):
        assert warning_text in self.driver.find_element_by_id('android:id/message').text
        print("I assert")
        self.driver.find_element_by_id('android:id/button1').click()
        print("I click OK")

    def add_contact(self):
        time_of_wait = 0
        for i in range(200):
            if self.driver.find_elements_by_id('com.example.android.contactmanager:id/addContactButton')==[]:
                time.sleep(1)
                time_of_wait +=1
            else:
                print(time_of_wait)
        self.driver.find_element_by_id('com.example.android.contactmanager:id/addContactButton').click()
        print("I click Add button")


    def contact_name_edit_text_selectable(self, text):
        print('input '+str(text)+' in Name field')
        self.driver.find_element_by_id('com.example.android.contactmanager:id/contactNameEditText').send_keys(text)
