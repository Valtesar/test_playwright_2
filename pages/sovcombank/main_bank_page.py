from playwright.sync_api import Page
from pages.web_page import WebPage


class MainBankPage(WebPage):
    def __init__(self, base_url, page: Page):
        super().__init__(page)
        self.base_url = base_url
        self.sections = ['Карты']

    def open(self):
        self.page.goto(self.base_url, wait_until="load")
        return self

    def go_to_section(self, search_section):
        for page_section in self.sections:
            if page_section == search_section:
                self.page.click(f'//a[@class="dark:link-text-tertiary link  py-5 " and text()="{page_section}"]')
                self.page.wait_for_selector('//*[@id="__next"]')
