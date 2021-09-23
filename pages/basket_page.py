from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_no_products_in_basket(self):
        # Проверка, что в корзине нет товаров
        assert self.is_not_element_present(
            *BasketPageLocators.PRODUCTS_IN_SHOPPING_CART), "There is an item in the basket"

    def should_be_text_basket_is_empty(self):
        # Проверка, что есть текст о том что корзина пуста
        assert self.is_element_present(
            *BasketPageLocators.BASKET_IS_EMPTY), "No text stating that the trash is empty"

