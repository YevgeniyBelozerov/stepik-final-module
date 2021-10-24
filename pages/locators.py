from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, 'a[class="btn btn-default"]')
    PRODUCT_IN_BASKET_PRESENCE = (By.CSS_SELECTOR, '#basket_formset')
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, '#content_inner>p')


class CartLocators:
    ADD_CART_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    BOOK_NAME = (By.CSS_SELECTOR, '.breadcrumb .active')
    BOOK_NAME_IN_MESSAGE = (By.CSS_SELECTOR, '.alert-success:nth-child(1) strong')
    BOOK_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    BOOK_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, '.alert-info strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert:nth-child(1)')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_NEW_USER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_NEW_USER_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_NEW_USER_PASSWORD_CONFIRM = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_NEW_USER_BUTTON_SUBMIT = (By.CSS_SELECTOR, 'button[name="registration_submit"]')


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
