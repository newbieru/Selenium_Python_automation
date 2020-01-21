import time
import math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_tag_name('button').click()
    browser.switch_to.alert.accept()
    value = browser.find_element_by_id('input_value')
    browser.find_element_by_id('answer').send_keys(calc(value.text))
    browser.find_element_by_css_selector('.btn').click()

finally:
    time.sleep(20)
    browser.quit()
