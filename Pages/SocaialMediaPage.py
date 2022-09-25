from Pages.HomePage import HomePage
from Locators.Locators import SocialMedia


class SocialMediaPage(HomePage):

    def __init__(self, driver):
        self.locator = SocialMedia
        self.driver = driver
        super(SocialMediaPage, self).__init__(driver)


    def click_top_facebook_button(self):
        self.find_element(*self.locator.click_facebook_top_Xpath)
    def click_top_instagram_button(self):
        self.find_element(*self.locator.click_instagram_top_Xpath)
    def click_top_youtube_button(self):
        self.find_element(*self.locator.click_youtube_top_Xpath)
    def click_top_linkdin_button(self):
        self.find_element(*self.locator.click_linkdin_top_Xpath)


    def click_down_facebook_button(self):
        self.find_element(*self.locator.click_facebook_down_Xpath)
    def click_down_instagram_button(self):
        self.find_element(*self.locator.click_instagram_down_Xpath)
    def click_down_youtube_button(self):
        self.find_element(*self.locator.click_youtube_down_Xpath)
    def click_down_linkdin_button(self):
        self.find_element(*self.locator.click_linkdin_down_Xpath)


