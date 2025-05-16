from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = ("https://suninjuly.github.io/registration1.html")

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Andrei")
    input2 = browser.find_element(By.CLASS_NAME, "form-control.second")
    input2.send_keys("Cherevichki")
    input3 = browser.find_element(By.CSS_SELECTOR, 'div:nth-child(3) .form-control')
    input3.send_keys("asfa@yandex.ru")
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    time.sleep(5)
    button.click()
    time.sleep(5)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text # записываем в переменную welcome_text текст из элемента welcome_text_elt
    assert welcome_text == "Congratulations! You have successfully registered!" # типа утверждение, что переменная содержит то, что в скобках. Булево

finally:
    time.sleep(10)
    browser.quit()
