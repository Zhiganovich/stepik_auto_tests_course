from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = ("http://suninjuly.github.io/explicit_wait2.html")

try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
#Сравниваем 100 с тем, что ожидаем
    browser.find_element(By.ID, "book").click()
    number_x = browser.find_element(By.ID, "input_value")
    browser.execute_script("return arguments[0].scrollIntoView(true);", number_x)
#Скроллим страницу к элементу number_x(НЕ СКРОЛЛИТСЯ, ЕСЛИ ПЕРЕМЕННУЮ СРАЗУ ПЕРЕВОДИМ в .text!!!
    y = number_x.text
    x = calc(y)
    input_number = browser.find_element(By.CLASS_NAME, "form-control").send_keys(x)
#Скроллим страницу к элементу input_number
    browser.find_element(By.ID, "solve").click()
    #ЕСЛИ ХОТИМ СРАЗУ ЧТО ТО СДЕЛАТЬ - КЛИК ИЛИ ОТПРАВИТЬ ЗНАЧЕНИЕ - НЕ НАЗЫВАЕМ ПЕРЕМЕННОЙ

finally:
    time.sleep(5)
    browser.quit()
