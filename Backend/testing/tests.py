import unittest

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import bs4
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

#
# class MainPage(unittest.TestCase):
#     def setUp(self):
#         self.firefox_options = webdriver.FirefoxOptions()
#         self.firefox_options.add_argument("-private")
#         self.driver = webdriver.Firefox(options=self.firefox_options)
#         self.driver.maximize_window()
#
#     def test_main_page(self):
#         self.driver.get("http://svitla.com")
#         assert "Svitla" in self.driver.title
#
#     def test_blog(self):
#         self.driver.get("http://svitla.com/blog")
#         logo = self.driver.find_element_by_class_name('header__logo-icon')
#         print(logo)
#         time.sleep(10)
#         logo.click()
#         assert "Svitla" in self.driver.title
#
#     def test_contacts(self):
#         self.driver.get("http://svitla.com/contacts")
#         name = self.driver.find_element_by_id('ctaformtype5-name')
#         print(name)
#         name.send_keys("John Smith")
#         assert "Contacts" in self.driver.title
#
#     def tearDown(self):
#         time.sleep(10)
#         self.driver.close()
from selenium.webdriver.support.wait import WebDriverWait

if __name__ == "__main__":
    # unittest.main()
    # print()
    driver = webdriver.Edge('msedgedriver.exe')
    driver.get("http://localhost:8080/")
    timeout = 15
    try:
        element_present = EC.presence_of_element_located((By.ID, 'element_id'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")

    # search_bar = driver.find_element_by_name("q")
    # search_bar.clear()
    # search_bar.send_keys("getting started with python")
    # search_bar.send_keys(Keys.RETURN)
    # print(driver.current_url)
    driver.close()
