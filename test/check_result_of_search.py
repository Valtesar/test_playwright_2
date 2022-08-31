import pytest
from playwright.sync_api import Page
from search_url import get_url_from_txt
from pages.search_engine.main_search_page import SearchPage
import logging


logger = logging.getLogger("test")


@pytest.mark.only_browser("chromium")
def test_check_result_of_search(page: Page):
    search_page = SearchPage('https://google.com', page)
    search_page.delete_cookies()
    search_page.open()
    search_page.search_text('Совкомбанк')
    search_page.get_stats()
    assert search_page.get_url_on_page()
