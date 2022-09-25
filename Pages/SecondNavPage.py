from Pages.HomePage import HomePage
from Locators.Locators import SecondNav

class SecondNavPage(HomePage):
    def __init__(self, driver):
        self.locator =  SecondNav
        self.driver = driver
        super(SecondNavPage, self).__init__(driver)


    def click_on_home_button(self):
        self.find_element(*self.locator.click_home_Xpath).click()
    def click_products_button(self):
        self.find_element(*self.locator.click_products_Xpath).click()

    def click_on_stores_button(self):
        self.find_element(*self.locator.click_stores_Xpath).click()
    def click_on_blog_button(self):
        self.find_element(*self.locator.click_blog_Xpath).click()

    def click_on_downloadapp_button(self):
        self.find_element(*self.locator.click_app_Xpath).click()