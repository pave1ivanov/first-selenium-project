import time
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert LoginPageLocators.URL in self.browser.current_url, "Login page URL is not correct"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FROM), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"

    def regester_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_INPUT)
        password_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASWORD_INPUT)
        password_repeat_imput = self.browser.find_element(*LoginPageLocators.REGISTRATION_REPEAT_PASWORD_INPUT)
        submit_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)

        email_input.send_keys(email)
        password_input.send_keys(password)
        password_repeat_imput.send_keys(password)
        submit_button.click()

