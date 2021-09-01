import time

def test_items(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_css_selector("button.btn")
    assert button, "Кнопка не найдена"
