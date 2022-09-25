from Pages.HomePage import HomePage
from Locators.Locators import ChatBox


class ChatPage(HomePage):
    def __init__(self, driver):
        self.locator = ChatBox
        self.driver = driver
        super(ChatPage, self).__init__(driver)

    def click_on_chatbox_button(self):
        self.find_element(*self.locator.click_chatbox_icon_Xpath).click()

    def iframe_cilck(self,iframe):
        self.find_element(*self.locator.iframe).click()
        self.switch_to.frame(iframe)

    def click_chatbox_name_enter(self, name):
        self.find_element(*self.locator.enter_chatbox_name_Xpath).send_keys(name)

    def click_chatbox_Pnumber_enter(self, Pnumber):
        self.find_element(*self.locator.enter_chatbox_Pnumber_Xpath).send_keys(Pnumber)

    def click_chatbox_letusknow_enter(self, know):
        self.find_element(*self.locator.enter_chatbox_letusknow_Xpath).send_keys(know)

    def click_on_start_chat_button(self):
        self.find_element(*self.locator.click_startchat_Xpath).click()