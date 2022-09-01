from playwright.sync_api import Page
from pages.sovcombank.main_bank_page import MainBankPage
from time import sleep


class CardsPage(MainBankPage):

    def order_halva_card(self):
        with self.page.context.expect_page() as new_page_info:
            self.page.evaluate(f"""() => {{
            const link = document.querySelector('#__next>div>div>main>section.container.py-14>a');
            link.dispatchEvent(new MouseEvent('click', {{
                bubbles: true,
                cancelable: true,
                view: window
            }}));
        }}""")
        self.new_page = new_page_info.value
        self.new_page.wait_for_selector('//*[@id="app"]/div/div/div[5]/fieldset/div/label/span[1]/span[1]/input')
        return self

    def edit_check_box_order(self):
        """Убираем из чек бокса галочку"""
        self.new_page.uncheck('//*[@id="app"]/div/div/div[5]/fieldset/div/label/span[1]/span[1]/input')
        sleep(5)

    def get_check_box_error(self):
        """Получаем уведомление об ошибке, если оно есть - возвращаем 1, нет 0"""
        if not self.new_page.is_checked('//*[@id="app"]/div/div/div[5]/fieldset/div/label/span[1]/span[1]/input') and \
                self.new_page.is_visible('//*[@id="app"]/div/div/div[5]/fieldset/p'):
            return True
        else:
            return False

    def get_fields_and_warnings(self):
        """Нажимаем на кнопку получить карту, собираем название полей и тексты ошибок, если все ошибки собраны
            возвращаем 1, нет 0"""
        self.new_page.click('')

        pass
