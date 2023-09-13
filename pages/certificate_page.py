from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from .locators import CertificatePageLocators
import csv
import codecs
import pandas as pd

class CertificatePage():

    def __init__(self, browser, url, timeout=2):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def find_certificate(self):
        with codecs.open('pages/names.csv', 'r', "utf-8") as f:
            one = next(f)
            two = next(f)
            three = next(f)

            name = WebDriverWait(self.browser, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#certificates-text')))
            name.clear()
            name.send_keys(one)
            find = WebDriverWait(self.browser, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#certificates-button')))
            find.click()
            name_certificate = self.browser.find_element(*CertificatePageLocators.NAME_CERTIFICATE).text
            date_certificate = self.browser.find_element(*CertificatePageLocators.DATE_CERTIFICATE).text

            name = WebDriverWait(self.browser, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#certificates-text')))
            name.clear()
            name.send_keys(two)
            find = WebDriverWait(self.browser, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#certificates-button')))
            find.click()
            name_certificate = self.browser.find_element(*CertificatePageLocators.NAME_CERTIFICATE).text
            name_certificate_2 = self.browser.find_element(*CertificatePageLocators.NAME_CERTIFICATE_2).text
            name_certificate_3 = self.browser.find_element(*CertificatePageLocators.NAME_CERTIFICATE_3).text
            date_certificate = self.browser.find_element(*CertificatePageLocators.DATE_CERTIFICATE).text
            name = WebDriverWait(self.browser, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#certificates-text')))
            name.clear()
            name.send_keys(three)
            none = WebDriverWait(self.browser, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#text1 :first-child"))).text
            none = ''
            assert none != 'По данному запросу ничего не найдено', 'None certificate was found'

        rows = ([one]+[name_certificate]+[date_certificate],
         [two]+[name_certificate]+[date_certificate],
         [two]+[name_certificate_2]+[date_certificate],
         [two]+[name_certificate_3]+[date_certificate],
         [three]+[none]+[none,])
        
        with codecs.open('pages/result.csv', 'w', "utf-8") as a:
            writer = csv.writer(a, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            writer.writerows(rows)



            
        