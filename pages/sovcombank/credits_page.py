from playwright.sync_api import Page
from pages.sovcombank.main_bank_page import MainBankPage


class CreditsPage(MainBankPage):
    def download_file(self):
        # Click to download file
        # Check that files downloaded -> 1, no -> 0
        pass

    def check_downloaded_files(self):
        # check type of files
        # delete files
        # -> return true if deleted -> else false
        pass
