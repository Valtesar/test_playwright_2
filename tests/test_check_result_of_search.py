import pytest
import logging


logger = logging.getLogger("tests")


class TestCheckResultsOfSearch:
    @pytest.mark.only_browser("chromium")
    def test_check_result_of_search(self, main_search_page):
        """Тест выполняет запрос в поисковой строке используя необходимое ключевое слово.
            Затем находит в результатах выдачи необходимый сайт и переходит на него.
            Считывает кол-во найденных результатов и выводит их в консоль"""

        search_page = main_search_page
        search_page.search_text('Совкомбанк')
        search_page.get_stats()
        assert search_page.get_url_on_page()
        search_page.close_page()

