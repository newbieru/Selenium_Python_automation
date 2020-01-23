import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class LessonOneTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_page_1(self):
        link = 'http://suninjuly.github.io/registration1.html'
        browser = self.driver
        browser.get(link)

        first_name = browser.find_element(By.CSS_SELECTOR, "input.first[required]")
        first_name.send_keys("Peter")
        last_name = browser.find_element(By.CSS_SELECTOR, "input.second[required]")
        last_name.send_keys("Kariba")
        email = browser.find_element(By.CSS_SELECTOR, "input.third[required]")
        email.send_keys("try@mmymail.com")
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         'Oops! Smthing goes wrong!')

    def test_page_2(self):
        link = 'http://suninjuly.github.io/registration2.html'
        browser = self.driver
        browser.get(link)

        first_name = browser.find_element(By.CSS_SELECTOR, "input.first[required]")
        first_name.send_keys("Peter")
        last_name = browser.find_element(By.CSS_SELECTOR, "input.second[required]")
        last_name.send_keys("Kariba")
        email = browser.find_element(By.CSS_SELECTOR, "input.third[required]")
        email.send_keys("try@mmymail.com")
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         'Oops! Smthing goes wrong!')


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
