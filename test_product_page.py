from pages.product_page import ProductPage
from selenium import webdriver



def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу

    page.add_to_shopping_cart()
    page.should_be_add_to_shopping_cart()
    page.cost_basket_coincides_price_of_product()

#
# if __name__ == '__main__':
#     browser = webdriver.Chrome()
#     browser.get("http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear")
#     test_guest_can_add_product_to_basket(browser)