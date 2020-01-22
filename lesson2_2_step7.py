import time
import os
from selenium import webdriver


def mk_file_path(filename):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(current_dir, filename)
    return path


try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector('[name = "firstname"]').send_keys('Peter')
    browser.find_element_by_css_selector('[name = "lastname"]').send_keys('Kariba')
    browser.find_element_by_css_selector('[name = "email"]').send_keys('tre@myml.com')
    file_path = mk_file_path('temp.txt')
    browser.find_element_by_css_selector('[type = "file"]').send_keys(file_path)
    browser.find_element_by_css_selector('.btn').click()
finally:
    time.sleep(30)
    browser.quit()
