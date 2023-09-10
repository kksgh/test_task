from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import random
import time

class CertificatePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def find_certificate(self):
        SEND_NUMBER = self.browser.find_element(By.CSS_SELECTOR, "#certificates-text")
        NUMBER = random.randint(0, 10000000000)
        SEND_NUMBER.send_keys(NUMBER)
        BUTTON_FIND = self.browser.find_element(By.CSS_SELECTOR, "#certificates-button")
        BUTTON_FIND.click()
        SUCCESS_OR_NOT = self.browser.find_element(By.CSS_SELECTOR, "#text1 :first-child").text
        time.sleep(4)
        assert SUCCESS_OR_NOT != "По данному запросу ничего не найдено", "No certificate found"
        #assert SUCCESS_OR_NOT == "Сертификат не найден", "No certificate found"