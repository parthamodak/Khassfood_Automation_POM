from selenium.webdriver.common.by import By


class LogIn():
    click_login_buton_xpath = (By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div/div[3]/div[2]/a")
    email_enter_xpath = (By.XPATH,"//input[@placeholder='Email Address']")
    password_enter_xpath = (By.XPATH,"//input[@placeholder='Password']")
    login_button_Xpath = (By.XPATH,"//button[@class='btn btn-color-primary btn-shape-semi-round btn-size-default btn-full-width'][normalize-space()='Login']")
class TopBar():
    click_gift_card_Xpath =(By.XPATH,"//a[@href='https://www.khaasfood.com/gift-card/']")
    click_howto_order_Xpath=(By.XPATH,"//span[normalize-space()='How to order']")
    click_faqs_Xpath=(By.XPATH,"//span[normalize-space()='FAQs']")
class SecondNav():
    click_home_Xpath=(By.XPATH,"//*[@id='menu-item-405']/a/span")
    click_products_Xpath = (By.XPATH, "/html/body/div[1]/header/div/div[2]/div/div/div[2]/div/div/ul/li[1]/a/span")
    click_stores_Xpath = (By.XPATH, "/html/body/div[1]/header/div/div[2]/div/div/div[2]/div/div/ul/li[3]/a/span")
    click_blog_Xpath = (By.XPATH, "//*[@id='menu-item-44665']/a/span")
    click_app_Xpath = (By.XPATH, "//*[@id='menu-item-48419']/a/span")


class ChatBox():
    click_chatbox_icon_Xpath=(By.XPATH,".//*[@id='webchat']/div[2]/div")
    iframe=(By.XPATH,"//*[@id='webchat']/div[2]/iframe")
    enter_chatbox_name_Xpath=(By.XPATH,"//input[@placeholder='Name*']")
    enter_chatbox_Pnumber_Xpath=(By.XPATH,"//input[@placeholder='Phone Number*']")
    enter_chatbox_letusknow_Xpath=(By.XPATH,"//textarea[@placeholder='Let us know what is in your mind…']")
    click_startchat_Xpath=(By.XPATH,"//button[@type='button']")

class SocialMedia():
    click_facebook_top_Xpath=(By.XPATH,"//div[@class='woodmart-social-icons text-center icons-design-colored icons-size-small color-scheme-dark social-follow social-form-square']//a[contains(@class,'woodmart-social-icon social-facebook')]")
    click_instagram_top_Xpath=(By.XPATH,"//div[@class='woodmart-social-icons text-center icons-design-colored icons-size-small color-scheme-dark social-follow social-form-square']//a[@class=' woodmart-social-icon social-instagram']")
    click_youtube_top_Xpath=(By.XPATH,"//div[@class='woodmart-social-icons text-center icons-design-colored icons-size-small color-scheme-dark social-follow social-form-square']//a[contains(@class,'woodmart-social-icon social-youtube')]//i")
    click_linkdin_top_Xpath=(By.XPATH,"//div[@class='woodmart-social-icons text-center icons-design-colored icons-size-small color-scheme-dark social-follow social-form-square']//a[contains(@class,'woodmart-social-icon social-linkedin')]")

    click_facebook_down_Xpath = (By.XPATH,"//div[@class='woodmart-social-icons text-left icons-design- icons-size-default color-scheme-light social-follow social-form-circle']//a[@class=' woodmart-social-icon social-facebook']//i")
    click_instagram_down_Xpath = (By.XPATH,"//div[@class='woodmart-social-icons text-left icons-design- icons-size-default color-scheme-light social-follow social-form-circle']//a[contains(@class,'woodmart-social-icon social-instagram')]")
    click_youtube_down_Xpath = (By.XPATH,"//div[@class='woodmart-social-icons text-left icons-design- icons-size-default color-scheme-light social-follow social-form-circle']//a[@class=' woodmart-social-icon social-youtube']//i")
    click_linkdin_down_Xpath = (By.XPATH,"//div[@class='woodmart-social-icons text-left icons-design- icons-size-default color-scheme-light social-follow social-form-circle']//a[contains(@class,'woodmart-social-icon social-linkedin')]")

class Card():
    click_card_button_Xpath=(By.XPATH,"/html/body/div[1]/header/div/div[3]/div/div/div[3]/div[3]/a")
class Subscribe():
    enter_subcribe_email_Xpath=(By.XPATH,"//input[@placeholder='Enter your email']")
    click_subcribe_button_Xpath=(By.XPATH,"//input[@id='es_subscription_form_submit_6320460624184']")

class Search():
    enter_serach_product_name_Xpath=(By.XPATH,"/html/body/div[1]/header/div/div[3]/div/div/div[2]/div/form/input[1]")
    click_search_button_Xpath=(By.XPATH,"/html/body/div[1]/header/div/div[3]/div/div/div[2]/div/form/button")

