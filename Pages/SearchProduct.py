from Pages.HomePage import HomePage
from Locators.Locators import Search


class SearchProduct(HomePage):

    def __init__(self, driver):
        self.locator = Search
        self.driver = driver
        super(SearchProduct, self).__init__(driver)






    def enter_product_name_text(self, product):
        self.find_element(*self.locator.enter_serach_product_name_Xpath).send_keys(product)

    def click_search_button(self):
        self.find_element(*self.locator.click_search_button_Xpath).click()

