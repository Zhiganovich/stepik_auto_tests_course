from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = ("https://suninjuly.github.io/get_attribute.html")

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)

    browser.find_element(By.ID, 'answer').send_keys(y)
    time.sleep(1)
    browser.find_element(By.ID, "robotCheckbox").click()
    time.sleep(1)
    browser.find_element(By.ID, "robotsRule").click()
    time.sleep(1)
    browser.find_element(By.CLASS_NAME, "btn.btn-default").click()
    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()

