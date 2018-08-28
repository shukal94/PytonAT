from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class StartPage:

    input_field = (By.CLASS_NAME, 'fast-search__input')
    logo = (By.CLASS_NAME, 'onliner_logo')

    def __init__(self, driver):
        self.driver = driver

    def is_opened(self):
        try:
            self.driver.find_element(*self.logo)
        except NoSuchElementException:
            return False
        return True

    def input_text(self, text):
        self.driver.find_element(*self.input_field).send_keys(text)
