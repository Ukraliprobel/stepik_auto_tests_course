from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element(By.ID, "submit_button")



assert expected_result == actual_result,\
    f"expected {expected_result}, got {actual_result}"

assert substring in full_string,\
    f"expected '{substring}' to be substring of '{full_string}'"