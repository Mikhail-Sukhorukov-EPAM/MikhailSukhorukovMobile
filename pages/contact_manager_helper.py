from pages.contact_manager_locators import ADD_CONTACT, CONTACT_NAME, MESSAGE_TEXT_FIELD, OK_BUTTON
from pages.base_page import BasePage


class CMHelper(BasePage):
    WARNING_TEXT = "This app was built for an older version of Android and may not work properly. " \
                   "Try checking for updates, or contact the developer."
    TIMEOUT = 5

    def get_warning_message(self):
        return self.driver.find_element(MESSAGE_TEXT_FIELD).text

    def click_ok_button(self):
        self.click(OK_BUTTON, CMHelper.TIMEOUT)

    def add_contact(self):
        self.click(ADD_CONTACT, CMHelper.TIMEOUT)

    def contact_name_edit_text_selectable(self, text):
        self.driver.find_element(CONTACT_NAME).send_keys(text)
