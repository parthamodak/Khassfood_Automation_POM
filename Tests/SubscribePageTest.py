import time

from Pages.BasePage import BasePage
from Pages.SubscribePage import SubscribePage


class SubscribePageTest(BasePage):

    def subcribe_page_test(self):
        js = SubscribePage(self.driver)
        time.sleep(5)
        js.enter_subscribe_email("mm.partho@gmail.com")
        time.sleep(5)
        js.click_subscribe_button()