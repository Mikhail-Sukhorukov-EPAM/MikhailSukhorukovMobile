from selenium.webdriver.common.by import By

BASE_SELECTOR_PATH = 'com.example.android.contactmanager:'
ADD_CONTACT = (By.ID, f'{BASE_SELECTOR_PATH}id/addContactButton')
CONTACT_NAME = (By.ID, f'{BASE_SELECTOR_PATH}id/contactNameEditText')
MESSAGE_TEXT_FIELD = (By.ID, 'android:id/message')
OK_BUTTON = (By.ID, 'android:id/button1')
