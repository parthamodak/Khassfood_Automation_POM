import time
import unittest
from selenium import webdriver


class BasePage(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\POM\Drivers\chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.get("https://www.bdjobs.com/")
        print("Test Started")

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.quit()
        print("Test Complete")