import pytest
from .pages.certificate_page import CertificatePage
from .pages.locators import CertificatePageLocators

#pytest -s test_certificate.py

def test_find_certificate(browser):
    link = "https://www.megaputer.ru/produkti/sertifikat/"
    page = CertificatePage(browser, link)
    page.open()
    #page.find_is_clickable()
    page.find_certificate()
    #page.write_csv()
