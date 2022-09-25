import time

from Pages.BasePage import BasePage
from Pages.SecondNavPage import SecondNavPage


class SecondNavPageTest(BasePage):

    def second_nav_page_test(self):
        js = SecondNavPage(self.driver)
        time.sleep(5)
        js.click_on_home_button()
        time.sleep(5)
        js.click_products_button()
        time.sleep(5)
        js.click_on_stores_button()
        time.sleep(5)
        js.click_on_blog_button()
        time.sleep(5)
        js.click_on_downloadapp_button()