from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = ("https://suninjuly.github.io/selects1.html")

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1")
    num2 = browser.find_element(By.ID, "num2")
    x = num1.text
    y = num2.text
    z = int(x) + int(y)
    z1 = str(z)
    #Строки сверху верные - считает правильно
    browser.find_element(By.ID, "dropdown").click() # тоже верно - кликает
    select = Select(browser.find_element(By.ID, "dropdown")) # здесь через селект выбираем список
    select.select_by_visible_text(z1) # здесь через селект выбираем число, которое рассчитали в переменной z1

    browser.find_element(By.CLASS_NAME, "btn.btn-default").click() # здесь клик на кнопку сабмит 

finally:
    time.sleep(10)
    browser.quit()
