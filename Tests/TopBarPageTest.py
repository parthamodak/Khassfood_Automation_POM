import time

from Pages.BasePage import BasePage
from Pages.TopBarPage import TopBarPage


class TopBarPageTest(BasePage):

    def subcribe_page_test(self):
        js = TopBarPage(self.driver)
        time.sleep(5)
        js.click_on_gift_button()
        time.sleep(5)
        js.click_on_order_button()
        time.sleep(5)
        js.click_on_FAQs_button()