from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()
        self.should_be_correct_price_in_info_message()
        self.should_be_correct_product_in_success_message()


    def should_be_correct_product_in_success_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        success_message_product_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME).text
        assert product_name == success_message_product_name, f"Product name '{product_name}'in success message is not correct - '{success_message_product_name}'"

    def should_be_correct_price_in_info_message(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        info_message_product_price = self.browser.find_element(*ProductPageLocators.INFO_MESSAGE_PRODUCT_PRICE).text
        assert product_price == info_message_product_price, f"Product price '{product_price}'in info message is not correct - '{info_message_product_price}'"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is present when it should not be"

    def should_dissappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message didn't dissapear when it should"