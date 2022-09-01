import pytest
from playwright.sync_api import Page
from pages.sovcombank.credits_page import CreditsPage
import logging


logger = logging.getLogger("tests")


@pytest.fixture()
def main_bank_page(page: Page):
    bank_page = CreditsPage('https://sovcombank.ru', page)
    bank_page.delete_cookies()
    bank_page.open()
    return bank_page


@pytest.mark.only_browser("chromium")
def test_download_credit_file(main_bank_page):
    """Тест с главной страницы сайта переходит в секцию кредиты. Затем скачивает файл путем клика по нему.
        Дожидается загрузки объекта. Затем проверяет является ли объект файлом и удаляет данный файл"""

    bank_page = main_bank_page
    bank_page.go_to_section('Кредиты')
    bank_page.download_file()
    assert bank_page.check_downloaded_files()
    assert bank_page.delete_downloaded_files()
