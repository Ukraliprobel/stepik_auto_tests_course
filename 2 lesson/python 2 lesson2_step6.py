from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:

    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text

    input1 = browser.find_element(By.CLASS_NAME, 'form-control')
    input1.send_keys(calc(x))

    check1 = browser.find_element(By.CSS_SELECTOR, '[type="checkbox"]')
    check1.click()
    radio1 = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio1)
    radio1.click()

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
