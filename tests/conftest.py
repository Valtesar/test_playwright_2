import pytest
from distutils import dir_util
import os
from playwright.sync_api import Page
from search_url import get_url_from_txt
from pages.search_engine.main_search_page import SearchPage


def pytest_addoption(parser):
    parser.addoption("--my_test_dump", action="store", default=None,
        help="Print test items in my custom format")


def pytest_collection_finish(session):
    if session.config.option.my_test_dump is not None:
        for item in session.items:
            print('{}::{}'.format(item.fspath, item.name))
        pytest.exit('Done!')


@pytest.mark.onlytest("test_check_result_of_search")
@pytest.fixture()
def data_dir(tmpdir, request):
    filename = request.module.__file__
    test_dir, _ = os.path.splitext(filename)

    if os.path.isdir(test_dir):
        dir_util.copy_tree(test_dir, str(tmpdir))

    return tmpdir


@pytest.mark.onlytest("test_check_result_of_search")
@pytest.fixture()
def get_link_from_file(data_dir):
    file = data_dir.join('urls.txt')
    with open(file) as text_file:
        link = get_url_from_txt(text_file.read())
    return link


@pytest.mark.onlytest("test_check_result_of_search")
@pytest.fixture()
def main_search_page(page: Page, get_link_from_file):
    search_page = SearchPage(get_link_from_file, page)
    search_page.delete_cookies()
    search_page.open()
    return search_page
