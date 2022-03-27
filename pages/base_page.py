from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import selenium.common.exceptions as ex


class BasePage:

    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

    def is_element_displayed(self, locator, timeout=0):
        """ Method should check displaying of something return True if it was displayed or False if not."""
        try:
            WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
            return True
        except ex.TimeoutException:
            return False

    def click(self, locator, timeout=0):
        """Check element visibility of element and click it."""
        if self.is_element_displayed(locator, timeout):
            self.driver.find_element(locator).click()
        else:
            raise ex.TimeoutException("Element not displayed")
