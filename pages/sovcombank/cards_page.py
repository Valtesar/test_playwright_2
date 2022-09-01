
from playwright.sync_api import expect

from pages.sovcombank.main_bank_page import MainBankPage
from time import sleep


class CardsPage(MainBankPage):

    def order_halva_card(self):


        """Функция кликает на кнопку заказать карту используя джаваскрипт скрипт.
            Далее переключается на новую вкладку"""

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
        self.new_page.wait_for_selector('//*[@id="app"]')

        return self

    def edit_check_box_order(self):
        """Убираем из чек бокса галочку"""

        locator = self.new_page.locator('//input[@type="checkbox"]')
        expect(locator).to_be_checked()
        self.new_page.uncheck('//input[@type="checkbox"]')

    def get_check_box_error(self):
        """Функция проверяет наличие уведомления об ошибке если чекбокс снят.
            Возвращает True если уведомление имеется, иначе False."""

        if not self.new_page.is_checked('//input[@type="checkbox"]') and \
                self.new_page.is_visible('//*[contains(@class, "Mui-required")]'):
            return True
        else:
            return False

    def get_fields_and_warnings(self):
        """Функция кликает на кнопку заказать карту. Собирает сообщения об ошибках и названия полей.
            На их основе создает словаь и выводит его в консоль.
            В случае успешной работы возвращает True, иначе False"""

        self.new_page.click('//*[contains(@class,"MuiButton-fullWidth")]')
        fields = self.new_page.locator('//*[contains(@class, "MuiInputLabel-outlined")]').all_text_contents()
        errors = self.new_page.locator('//*[contains(@class, "MuiFormHelperText-contained")]').all_text_contents()
        if len(fields) == len(errors):
            dictionary = dict(zip(fields, errors))
            print(dictionary)
            return True
        elif len(fields) != len(errors):
            return False

