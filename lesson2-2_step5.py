from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = ("https://suninjuly.github.io/redirect_accept.html")

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CLASS_NAME, "trollface.btn.btn-primary").click()
# Находим кнопку и кликаем на нее
    second_window = browser.window_handles[1]
# Тк открылась новая вкладка, задаем переменную для второго окна (значение в квадр скобках = номер окна, нумерация начинается с 0)
    browser.switch_to.window(second_window)
# Говорим скрипту, что нужно переключиться на другую вкладку
    number = browser.find_element(By.ID, "input_value").text
    x = calc(number)
    browser.find_element(By.ID, "answer").send_keys(x)
    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()

finally:
    time.sleep(10)
    browser.quit()
