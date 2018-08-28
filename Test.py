from selenium import webdriver
import unittest
import time

from pages.StartPage import StartPage

class Test(unittest.TestCase):

    basic_url = 'https://www.onliner.by/'

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.fullscreen_window()
        self.driver.get(Test.basic_url)

    def test_01(self):
        driver = self.driver
        start_page = StartPage(driver)
        self.assertTrue(start_page.is_opened(), 'Start page isn\'t opened!')
        start_page.input_text('fsdfs')
        time.sleep(3)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
