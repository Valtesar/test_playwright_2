from playwright.sync_api import Page
from pages.web_page import WebPage


class SearchPage(WebPage):

    def __init__(self, base_url, page: Page):
        super().__init__(page)
        self.base_url = base_url

    def open(self):
        self.page.goto(self.base_url, wait_until="load")
        return self

    def search_text(self, text):
        self.page.locator('//*[@title="Поиск"]').fill(text)
        self.page.locator('//*[@title="Поиск"]').press('Enter')
        self.page.wait_for_selector('//*[@id="rso"]')
        return self

    def get_stats(self):
        value = self.page.locator('//*[@id="result-stats"]').all_inner_texts()
        value = str(value).split()[2]
        print('Примерное кол-во найденных результатов: ', end='')
        for num in value:
            if num.isdigit():
                print(num, sep='', end='')

        return self

    def get_url_on_page(self):
        urls = self.page.locator('//cite[contains(@role, "text")]').all_text_contents()
        for url in urls:
            if url == 'https://sovcombank.ru':
                self.page.locator(f'//cite[@role="text" and text()="{url}"]').first.click()
                return True

