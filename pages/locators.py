from selenium.webdriver.common.by import By

class CertificatePageLocators():
    ENTER_NAME = (By.CSS_SELECTOR, "#certificates-text")
    BUTTON_FIND = (By.CSS_SELECTOR, "#certificates-button")
    #NAME_PERSON = (By.CSS_SELECTOR, "tr:first-of-type td:first-of-type")
    NAME_CERTIFICATE = (By.CSS_SELECTOR, '#text1 td:nth-of-type(even)')
    NAME_CERTIFICATE_2 = (By.CSS_SELECTOR, 'tr:nth-of-type(2) td:nth-of-type(1)')
    NAME_CERTIFICATE_3 = (By.CSS_SELECTOR, 'tr:nth-of-type(3) td:nth-of-type(1)')
    DATE_CERTIFICATE = (By.CSS_SELECTOR, '#text1 :nth-child(3)')
    DATE_CERTIFICATE_2 = (By.CSS_SELECTOR, 'tr:nth-of-type(2) td:nth-of-type(2)')
    DATE_CERTIFICATE_3 = (By.CSS_SELECTOR, 'tr:nth-of-type(3) td:nth-of-type(2)')
    ERROR = (By.CSS_SELECTOR, "#text1 :first-child")
