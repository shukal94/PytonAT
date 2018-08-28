from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest
import time

class Test:

    basic_url = "https://www.google.com"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.basic_url)

    def test_01(self):
        driver = self.driver
        input_field = driver.find_element_by_id('lst-ib')
        input_field.send_keys('python')
        input_field.send_keys(Keys.ENTER)
        time.sleep(22)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
