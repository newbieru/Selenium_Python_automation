import time
import math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_tag_name('button').click()
    new_window = browser.window_handles[2]
    # time.sleep(1)
    browser.switch_to.window(new_window)

    value = browser.find_element_by_id('input_value')
    browser.find_element_by_id('answer').send_keys(calc(value.text))
    browser.find_element_by_css_selector('.btn').click()

finally:
    time.sleep(20)
    browser.quit()
