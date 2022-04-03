from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    
    def should_be_basket_page(self):
        self.should_be_basket_url()

    def should_have_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), "No Basket is empty message"

    def should_not_have_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS_CONTAINER), "Basket is not empty, but should be"

    def should_be_basket_url(self):
        assert BasketPageLocators.URL in self.browser.current_url, "Login page URL is not correct"
