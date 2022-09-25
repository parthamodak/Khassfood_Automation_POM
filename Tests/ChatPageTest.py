import time

from Pages.BasePage import BasePage
from Pages.ChatPage import ChatPage


class ChatPageTest(BasePage):

    def cart_page_test(self):
        js = ChatPage(self.driver)
        time.sleep(5)
        js.click_on_chatbox_button()
        time.sleep(5)
        js.iframe_cilck()

        js.click_chatbox_name_enter("Partha Modak")
        time.sleep(5)
        js.click_chatbox_Pnumber_enter("+8801521314162")
        time.sleep(5)
        js.click_chatbox_letusknow_enter("this is for testing and automation")
        time.sleep(5)
        js.click_on_start_chat_button()
