from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

try:

    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    # price.click()
    button0 = browser.find_element(By.ID, "book")
    button0.click()

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(calc(x))

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
