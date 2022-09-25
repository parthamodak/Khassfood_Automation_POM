from Pages.HomePage import HomePage
from Locators.Locators import Subscribe


class SubscribePage(HomePage):

    def __init__(self, driver):
        self.locator = Subscribe
        self.driver = driver
        super(SubscribePage, self).__init__(driver)

    def enter_subscribe_email(self, semail):
        self.find_element(*self.locator.enter_subcribe_email_Xpath).send_keys(semail)
    def click_subscribe_button(self):
        self.find_element(*self.locator.click_subcribe_button_Xpath).click()