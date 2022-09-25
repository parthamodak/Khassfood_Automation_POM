import time

from Pages.BasePage import BasePage
from Pages.SearchProduct import SearchProduct


class SearchProductTest(BasePage):

    def search_product_test(self):
        js = SearchProduct(self.driver)
        time.sleep(3)
        js.enter_product_name_text("products")
        time.sleep(3)
        js.click_search_button()