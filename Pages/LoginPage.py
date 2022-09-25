from Pages.HomePage import HomePage
from Locators.Locators import LogIn

class LoginPage(HomePage):
    def __init__(self, driver):
        self.locator =  LogIn
        self.driver = driver
        super(LoginPage, self).__init__(driver)

    def click_on_login_button(self):
        self.find_element(*self.locator.click_login_buton_xpath).click()



    def enter_email(self, email):
        self.find_element(*self.locator.email_enter_xpath).send_keys(email)



    def enter_password(self, password):
        self.find_element(*self.locator.password_enter_xpath).send_keys(password)

    def click_login(self):
        self.find_element(*self.locator.login_button_Xpath).click()

