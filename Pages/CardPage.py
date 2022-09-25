from Pages.HomePage import HomePage
from Locators.Locators import Card


class CardPage(HomePage):

    def __init__(self, driver):
        self.locator = Card
        self.driver = driver
        super(CardPage, self).__init__(driver)


    def click_on_card_button(self):
        self.find_element(*self.locator.click_card_button_Xpath).click()