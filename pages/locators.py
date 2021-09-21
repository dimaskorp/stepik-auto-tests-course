from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_USERNAME = (By.NAME, "login-username")
    REGISTRATION_EMAIL = (By.NAME, "registration-email")


class ProductPageLocators():
    BUTTON = (By.CLASS_NAME, "btn")
    MESSAGE_PRODUCT_ADDED_TO_CART = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    MESSAGE_CAST_BASKET = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div")
