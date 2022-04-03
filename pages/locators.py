from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LNIK = (By.CSS_SELECTOR, ".basket-mini a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    URL = "/basket/"
    BASKET_ITEMS_CONTAINER = (By.CSS_SELECTOR, ".basket-items")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")

class LoginPageLocators():
    URL = "/accounts/login/"
    LOGIN_FROM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL_INPUT = (By.CSS_SELECTOR, "[name=registration-email]")
    REGISTRATION_PASWORD_INPUT = (By.CSS_SELECTOR, "[name=registration-password1]")
    REGISTRATION_REPEAT_PASWORD_INPUT = (By.CSS_SELECTOR, "[name=registration-password2]")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name=registration_submit]")
    
class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    SUCCESS_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alert:first-child > .alertinner > strong")
    INFO_MESSAGE_PRODUCT_PRICE = (By.CSS_SELECTOR, "#messages .alert-info > .alertinner strong")