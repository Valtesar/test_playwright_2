import pytest
from playwright.sync_api import Page
from pages.sovcombank.cards_page import CardsPage
import logging


logger = logging.getLogger("tests")


@pytest.fixture()
def main_bank_page(page: Page):
    bank_page = CardsPage('https://sovcombank.ru', page)
    bank_page.delete_cookies()
    bank_page.open()
    return bank_page


@pytest.mark.only_browser("chromium")
def check_validation_message_is_visible(main_bank_page):
    bank_page = main_bank_page
    bank_page.go_to_section('Карты')
    bank_page.order_halva_card()
    bank_page.edit_check_box_order()
    assert bank_page.get_check_box_error()
    assert bank_page.get_fields_and_warnings()

