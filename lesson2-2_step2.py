from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = ("http://suninjuly.github.io/execute_script.html")

try:
    browser = webdriver.Chrome()
    browser.get(link)
# Запускаем браузер с нужной ссылкой из переменной link
    number = browser.find_element(By.ID, "input_value")
    x = number.text
    y = calc(x)
# Находим число, присваем ему формат .text, рассчитываем с ним функцию
    browser.find_element(By.CLASS_NAME, "form-control").send_keys(y)
# Отправляем полученное число в поле
    browser.find_element(By.ID, "robotCheckbox").click()
# Килкаем на чекбокс
    button = browser.find_element(By.ID, "robotsRule")
# Находим радиобатон и кладем его в переменную button, чтобы затем на него кликнуть после скролла
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
# Заставляем брузер пролистнуть страницу к радиобатону и кликнуть на него
    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()
# Кликаем на сабмит(отправка формы)
finally:
    time.sleep(10)
    browser.quit()
