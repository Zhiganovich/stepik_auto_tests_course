from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_link_text")
    che_eto = str(math.ceil(math.pow(math.pi, math.e) * 10000))


    button = browser.find_element(By.LINK_TEXT, che_eto) #224592
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла