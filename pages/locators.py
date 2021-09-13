from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_USERNAME = (By.NAME, "login-username")
    REGISTRATION_EMAIL = (By.NAME, "registration-email")
