from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = ("http://suninjuly.github.io/file_input.html")

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.NAME, "firstname").send_keys("Eren")
    browser.find_element(By.NAME, "lastname").send_keys("Yeger")
    browser.find_element(By.NAME, "email").send_keys("ErenYeger@gmail.com")
    element = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'selenium.txt')           # добавляем к этому пути имя файла
    element.send_keys(file_path)

    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()

finally:
    time.sleep(10)
    browser.quit()
