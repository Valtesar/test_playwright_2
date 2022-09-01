from __future__ import unicode_literals
from distutils import dir_util
import os
import pytest
from playwright.sync_api import Page
from search_url import get_url_from_txt
from pages.search_engine.main_search_page import SearchPage
import logging


logger = logging.getLogger("tests")


@pytest.fixture()
def data_dir(tmpdir, request):
    filename = request.module.__file__
    test_dir, _ = os.path.splitext(filename)

    if os.path.isdir(test_dir):
        dir_util.copy_tree(test_dir, str(tmpdir))

        return tmpdir


@pytest.fixture()
def get_link_from_file(data_dir):
    file = data_dir.join('urls.txt')
    with open(file) as text_file:
        link = get_url_from_txt(text_file.read())
    return link


@pytest.fixture()
def main_search_page(page: Page, get_link_from_file):
    search_page = SearchPage(get_link_from_file, page)
    search_page.delete_cookies()
    search_page.open()
    return search_page


@pytest.mark.only_browser("chromium")
def test_check_result_of_search(main_search_page):
    """Тест выполняет запрос в поисковой строке используя необходимое ключевое слово.
        Затем находит в результатах выдачи необходимый сайт и переходит на него.
        Считывает кол-во найденных результатов и выводит их в консоль"""

    search_page = main_search_page
    search_page.search_text('Совкомбанк')
    search_page.get_stats()
    assert search_page.get_url_on_page()
    search_page.close_page()

