from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestWelcome(unittest.TestCase):

    def test_welcome_text1(self):
        try:
            link1 = "http://suninjuly.github.io/registration1.html"
            browser1 = webdriver.Chrome()
            browser1.get(link1)

            # Ваш код, который заполняет обязательные поля
            input1 = browser1.find_element(By.CSS_SELECTOR, 'div.first_block div .first')
            input1.send_keys("Ivan")
            input2 = browser1.find_element(By.CSS_SELECTOR, 'div.first_block div .second')
            input2.send_keys("Petrov")
            input3 = browser1.find_element(By.CSS_SELECTOR, 'div.first_block div .third')
            input3.send_keys("123@123.ru")

            # Отправляем заполненную форму
            button = browser1.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser1.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser1.quit()

    def test_welcome_text2(self):
        try:
            link2 = "http://suninjuly.github.io/registration2.html"
            browser2 = webdriver.Chrome()
            browser2.get(link2)

            # Ваш код, который заполняет обязательные поля
            input1 = browser2.find_element(By.CSS_SELECTOR, 'div.first_block div .first')
            input1.send_keys("Ivan")
            input2 = browser2.find_element(By.CSS_SELECTOR, 'div.first_block div .second')
            input2.send_keys("Petrov")
            input3 = browser2.find_element(By.CSS_SELECTOR, 'div.first_block div .third')
            input3.send_keys("123@123.ru")

            # Отправляем заполненную форму
            button = browser2.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser2.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser2.quit()

if __name__ == "__main__":
    unittest.main()
