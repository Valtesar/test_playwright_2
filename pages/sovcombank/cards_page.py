from playwright.sync_api import Page
from pages.sovcombank.main_bank_page import MainBankPage


class CardsPage(MainBankPage):

    def order_halva_card(self):
        """Нажимаем на клавишу заказать карту, переключаемся на новую вкладку"""
        pass

    def edit_check_box_order(self):
        """Убираем из чек бокса галочку"""
        pass

    def get_check_box_error(self):
        """Получаем уведомление об ошибке, если оно есть - возвращаем 1, нет 0"""
        pass

    def get_fields_and_warnings(self):
        """Нажимаем на кнопку получить карту, собираем название полей и тексты ошибок, если все ошибки собраны
            возвращаем 1, нет 0"""
        pass
