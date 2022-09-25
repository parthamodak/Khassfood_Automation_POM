import time

from Pages.BasePage import BasePage
from Pages.SocaialMediaPage import SocialMediaPage


class SocialMediaPageTest(BasePage):

    def social_media_page_test(self):
        js = SocialMediaPage(self.driver)
        time.sleep(5)
        js.click_top_facebook_button()
        js.click_top_instagram_button()
        js.click_top_youtube_button()
        js.click_top_linkdin_button()

        js.click_down_facebook_button()
        js.click_down_instagram_button()
        js.click_down_youtube_button()
        js.click_down_linkdin_button()
