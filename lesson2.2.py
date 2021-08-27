from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


def calc(x1, x2):
    return str(x1 + x2)


try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()





    #browser.execute_script("document.title='Script executing';alert('Robots at work');")
    browser.get("http://suninjuly.github.io/selects2.html")

    x1_element = browser.find_element_by_id('num1')
    x2_element = browser.find_element_by_id('num2')
    x1 = x1_element.text
    x2 = x2_element.text
    y = calc(int(x1), int(x2))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
