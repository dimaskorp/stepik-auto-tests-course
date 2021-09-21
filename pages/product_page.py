from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def add_to_shopping_cart(self):
        self.should_be_add_to_shopping_cart()
        button = self.browser.find_element_by_css_selector("button.btn-add-to-basket")
        button.click()
        time.sleep(1)
        self.solve_quiz_and_get_code()
        self.should_be_product_add_to_cart()

    def should_be_add_to_shopping_cart(self):
        # Проверка, что есть Кнопка
        assert self.is_element_present(*ProductPageLocators.BUTTON), "Button form is not presented"

    def should_be_product_add_to_cart(self):
        # Проверка, что есть сообщение о том, что товар добавлен в корзину.
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRODUCT_ADDED_TO_CART), "Message is not presented"
        # Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
        header = self.browser.find_element_by_css_selector("#content_inner > article > div.row > div.col-sm-6.product_main > h1")
        header_text = header.text
        product_name = self.browser.find_element_by_css_selector("#messages > div:nth-child(1) > div > strong")
        product_name_text = product_name.text
        assert header_text == product_name_text, "The product name in the message does not match the product that you added"

    def cost_basket_coincides_price_of_product(self):
        # Проверка, что есть сообщение со стоимостью корзины.
        assert self.is_element_present(*ProductPageLocators.MESSAGE_CAST_BASKET), "Message is not presented"
        # Стоимость корзины совпадает с ценой товара.
        cost_basket = self.browser.find_element_by_css_selector("#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
        cost_basket_text = cost_basket.text
        price_product = self.browser.find_element_by_css_selector("#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
        price_product_text = price_product.text
        assert cost_basket_text == price_product_text, "The cost of the basket does not match the price of the product"