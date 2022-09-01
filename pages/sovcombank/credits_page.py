from pages.sovcombank.main_bank_page import MainBankPage
from pathlib import Path


class CreditsPage(MainBankPage):
    def download_file(self):
        """Функция кликает на файл находящийся на странице, дожидается его скачивания.
            Для наглядности выводит путь файла на компьютере."""

        with self.page.expect_download() as download_info:
            self.page.locator('(//div[@class="font-medium group-hover:text-brand-blue"])[2]').click()
        self.download = download_info.value
        print(self.download.path())

    def check_downloaded_files(self):
        """Функция проверяет тип скаченного объекта.
            Если объект является файлом возвращает True, иначе False"""

        path = Path(self.download.path())
        return True if path.is_file() else False

    def delete_downloaded_files(self):
        """Функция удаляет скаченный файл. Если файл удален возвращает True, иначе False"""

        path = Path(self.download.path())
        try:
            path.unlink()
            return True
        except FileNotFoundError:
            return False
