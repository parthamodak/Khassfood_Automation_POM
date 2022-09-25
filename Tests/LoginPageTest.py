import time

from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage


class LoginPageTest(BasePage):

    def login_page_test(self):
        js = LoginPage(self.driver)
        time.sleep(5)
        js.click_on_login_button()
        time.sleep(5)
        js.enter_email("mm.partho@gmail.com")
        time.sleep(5)
        js.enter_password("53PMM80@")
        time.sleep(5)
        js.click_login()
