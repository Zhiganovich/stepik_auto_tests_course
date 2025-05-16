from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/find_link_text"
number = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome() # задаем переменную browser
    browser.get("http://suninjuly.github.io/find_link_text") #открываем через переменную страницу браузера
    button1 = browser.find_element(By.PARTIAL_LINK_TEXT, number) #задаем переменную, которая ищет элемент в CSS
    button1.click() #кликаем на найденную переменную

    input1 = browser.find_element(By.TAG_NAME, "input")#ищем инпут
    input1.send_keys("Ivan") #сенд кейс типа прописывают текст в инпут
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла