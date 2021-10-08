from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class CartLocators:
    ADD_CART_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    BOOK_NAME = (By.CSS_SELECTOR, '.breadcrumb .active')
    BOOK_NAME_IN_MESSAGE = (By.CSS_SELECTOR, '.alert-success:nth-child(1) strong')
    BOOK_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    BOOK_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, '.alert-info strong')

