

from Pages.HomePage import HomePage
from Locators.Locators import TopBar


class TopBarPage(HomePage):

    def __init__(self, driver):
        self.locator = TopBar
        self.driver = driver
        super(TopBarPage, self).__init__(driver)

    def click_on_gift_button(self):
        self.find_element(*self.locator.click_gift_card_Xpath).click()
    def click_on_order_button(self):
        self.find_element(*self.locator.click_howto_order_Xpath).click()
    def click_on_FAQs_button(self):
        self.find_element(*self.locator.click_faqs_Xpath).click()