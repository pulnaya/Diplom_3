import allure
from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedLocators



class OrderFeedPage(BasePage):

    @allure.step("Клик по заказу в ленте")
    def click_order_in_feed(self):
        self.click_to_element(OrderFeedLocators.ORDER_IN_FEED)

    @allure.step("Проверка отображения окна с деталями заказа")
    def is_order_details_displayed(self):
        return self.is_element_visible(OrderFeedLocators.ORDER_DETAILS_MODAL)

    @allure.step("Получение всех номеров заказов в ленте")
    def get_all_order_numbers(self):
        elements = self.find_elements_with_wait(OrderFeedLocators.ORDER_LINK_NUMBER)
        return [el.text for el in elements if el.text]

    @allure.step("Ожидание загрузки ленты заказов")
    def wait_for_order_feed_title(self):
        self.wait_for_element_visible(OrderFeedLocators.ORDER_FEED_TITLE)

    @allure.step("Получение количества заказов за всё время")
    def get_all_time_orders_count(self):
        element = self.find_element_with_wait(OrderFeedLocators.ALL_TIME_ORDERS_COUNTER)
        return int(element.text)

    @allure.step("Получение количества заказов за сегодня")
    def get_today_orders_count(self):
        element = self.find_element_with_wait(OrderFeedLocators.TODAY_ORDERS_COUNTER)
        return int(element.text)

    @allure.step("Получение списка заказов в работе")
    def get_orders_in_progress(self):
        elements = self.find_elements_with_wait(OrderFeedLocators.ORDER_IN_PROGRESS_NUMBER)
        return [el.text.lstrip('0') for el in elements if el.text]

    @allure.step("Ожидание появления заказа в разделе 'В работе'")
    def wait_for_order_in_progress(self, order_number):
        locator = (OrderFeedLocators.ORDER_IN_PROGRESS_BY_NUMBER[0], 
                OrderFeedLocators.ORDER_IN_PROGRESS_BY_NUMBER[1].format(order_number))
        self.wait_for_element_visible(locator)