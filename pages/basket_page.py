from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_empty(self):
        self.should_not_be_product_into_basket()
        self.should_be_text_about_empty_basket()

    def should_not_be_product_into_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET_PRESENCE), 'there are products in ' \
                                                                                            'the basket, ' \
                                                                                            'but they should not be '

    def should_be_text_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), 'There is no empty bucket message'
