import pytest
import logging


logger = logging.getLogger("tests")


class TestDownloadCreditFile:
    @pytest.mark.only_browser("chromium")
    def test_download_credit_file(self, main_bank_page):
        """Тест с главной страницы сайта переходит в секцию кредиты. Затем скачивает файл путем клика по нему.
            Дожидается загрузки объекта. Затем проверяет является ли объект файлом и удаляет данный файл"""

        bank_page = main_bank_page
        bank_page.go_to_section('Кредиты')
        bank_page.download_file()
        assert bank_page.check_downloaded_files()
        assert bank_page.delete_downloaded_files()
