from .base_page import BasePage
from .locators import CartLocators


class ProductPage(BasePage):
    def should_be_correct_addition_cart(self):
        self.should_be_add_item_into_cart()
        self.solve_quiz_and_get_code()
        self.should_be_message_added_cart()
        self.should_be_message_cart_price()

    def should_be_add_item_into_cart(self):
        add_cart_button = self.browser.find_element(*CartLocators.ADD_CART_BUTTON)
        add_cart_button.click()

    def should_be_message_added_cart(self):
        book_name = self.browser.find_element(*CartLocators.BOOK_NAME).text
        book_name_in_message = self.browser.find_element(*CartLocators.BOOK_NAME_IN_MESSAGE).text
        assert book_name == book_name_in_message, 'No message about adding to the cart, or the product name ' \
                                                  'in the message is incorrect '

    def should_be_message_cart_price(self):
        book_price = self.browser.find_element(*CartLocators.BOOK_PRICE).text
        book_price_in_message = self.browser.find_element(*CartLocators.BOOK_PRICE_IN_MESSAGE).text
        assert book_price == book_price_in_message, 'No message about the cost of the price, or the price is incorrect'
