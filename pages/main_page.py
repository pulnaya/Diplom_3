import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.common.exceptions import TimeoutException


class MainPage(BasePage):

    @allure.step("Клик по кнопке 'Личный кабинет'")
    def click_personal_account(self):
        self.click_to_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Клик по кнопке 'Конструктор'")
    def click_constructor(self):
        """Клик по кнопке 'Конструктор'"""
        self.click_to_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Клик по кнопке 'Лента заказов'")
    def click_order_feed(self):
        """Клик по кнопке 'Лента заказов'"""
        self.click_to_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Клик на ингредиент")
    def click_ingredient(self):
        """Клик по ингредиенту для открытия деталей"""
        self.click_to_element(MainPageLocators.INGREDIENT)

    @allure.step("Проверка отображения окна с деталями ингредиента")
    def is_ingredient_details_displayed(self):
        """Проверить, что открылось окно с деталями ингредиента"""
        return self.is_element_visible(MainPageLocators.INGREDIENT_DETAILS_MODAL)

    @allure.step("Закрытие окна с деталями ингредиента")
    def close_ingredient_details(self):
        """Закрыть окно с деталями ингредиента"""
        self.click_to_element(MainPageLocators.INGREDIENT_DETAILS_CLOSE_BUTTON)

    @allure.step("Проверка, что окно с деталями закрылось")
    def is_ingredient_details_closed(self):
        """Ожидать, что окно с деталями закрылось (возвращает True/False)"""
        try:
            self.wait_for_element_invisible(MainPageLocators.INGREDIENT_DETAILS_MODAL)
            return True
        except TimeoutException:
            return False

    @allure.step("Получение каунтера ингредиента")
    def get_ingredient_counter(self):
        """Получить значение каунтера ингредиента"""
        element = self.find_element_with_wait(MainPageLocators.INGREDIENT_COUNTER)
        return int(element.text)

    @allure.step("Добавление ингредиента в заказ")
    def add_ingredient_to_order(self):
        """Добавить ингредиент в заказ (перетаскиванием)"""
        self.drag_and_drop_element(MainPageLocators.INGREDIENT, MainPageLocators.ORDER_CONSTRUCTOR)

    @allure.step("Оформление заказа")
    def place_order(self):
        """Оформить заказ"""
        self.click_to_element(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step("Проверка, что заказ оформлен")
    def is_order_placed(self):
        """Проверить, что заказ оформлен (появился номер)"""
        return self.is_element_visible(MainPageLocators.ORDER_NUMBER)

    @allure.step("Получение номера заказа")
    def get_order_number(self):
        """Получить номер заказа из модального окна"""
        element = self.find_element_with_wait(MainPageLocators.ORDER_NUMBER)
        return element.text

    @allure.step("Ожидание реального номера заказа")
    def wait_for_order_number_to_appear(self):
        """Ожидать, когда появится реальный номер заказа (не 9999)"""
        self.wait.until(lambda driver: self.get_order_number() != '9999')

    @allure.step("Закрытие модального окна с заказом")
    def close_order_modal(self):
        """Закрыть модальное окно с заказом"""
        self.click_to_element(MainPageLocators.ORDER_DETAILS_CLOSE_BUTTON)

    @allure.step("Создание заказа")
    def create_order(self):
        """Создать заказ: добавить ингредиент, оформить, дождаться номера и закрыть модалку"""
        self.add_ingredient_to_order()
        self.place_order()
        self.wait_for_order_number_to_appear()
        order_number = self.get_order_number()
        self.close_order_modal()
        return order_number
