import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    book_button = browser.find_element_by_id('book')
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    book_button.click()

    value = browser.find_element_by_id('input_value')
    browser.find_element_by_id('answer').send_keys(calc(value.text))
    browser.find_element_by_id('solve').click()

finally:
    time.sleep(20)
    browser.quit()
