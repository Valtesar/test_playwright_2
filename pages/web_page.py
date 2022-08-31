from playwright.sync_api import Page


class WebPage(object):
    def __init__(self, page: Page):
        self.page = page

    def delete_cookies(self):
        self.page.context.clear_cookies()

    def reload(self):
        self.page.reload(wait_until="load")

    def close_page(self):
        self.page.close()
