from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = ("http://suninjuly.github.io/alert_accept.html")

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()

    confirm = browser.switch_to.alert
    confirm.accept()
# Переключаемся на модалку
    number = browser.find_element(By.ID, 'input_value').text
    y = calc(number)
# Рассчитываем по формуле функцию
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()

finally:
    time.sleep(10)
    browser.quit()