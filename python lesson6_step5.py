from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.PARTIAL_LINK_TEXT, "224592")
    input1.click()
    input2 = browser.find_element(By.TAG_NAME, "input")
    input2.send_keys("Ivan")
    input3 = browser.find_element(By.NAME, "last_name")
    input3.send_keys("Petrov")
    input4 = browser.find_element(By.CSS_SELECTOR, '.form-control.city')
    input4.send_keys("Smolensk")
    input5 = browser.find_element(By.ID, "country")
    input5.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла