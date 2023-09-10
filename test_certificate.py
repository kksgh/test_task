import pytest
from .pages.certificate_page import CertificatePage

def test_find_certificate(browser):
    link = "https://www.megaputer.ru/produkti/sertifikat/"
    page = CertificatePage(browser, link)
    page.open()
    page.find_certificate()