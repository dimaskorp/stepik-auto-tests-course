from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    VIEW_CART = (
    By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")


class LoginPageLocators():
    LOGIN_USERNAME = (By.NAME, "login-username")
    REGISTRATION_EMAIL = (By.NAME, "registration-email")


class ProductPageLocators():
    BUTTON = (By.CLASS_NAME, "btn")
    MESSAGE_PRODUCT_ADDED_TO_CART = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    MESSAGE_CAST_BASKET = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    PRODUCTS_IN_SHOPPING_CART = (By.CSS_SELECTOR, "#content_inner > div.basket-title.hidden-xs > div > h2")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")



