from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    URL = "/accounts/login/"
    LOGIN_FROM = (By.CSS_SELECTOR, "#login_form_not")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form_not")