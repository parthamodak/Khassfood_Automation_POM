import time

from Pages.BasePage import BasePage
from Pages.CardPage import CardPage


class CardPageTest(BasePage):

    def Card_page_test(self):
        js = CardPage(self.driver)
        time.sleep(5)
        js.click_on_card_button()