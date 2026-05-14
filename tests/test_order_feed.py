import allure
from urls import FEED_URL


class TestOrderFeed:
    
    @allure.title("Клик на заказ открывает окно с деталями")
    def test_order_details_modal_appears(self, driver, order_feed_page):
        driver.get(FEED_URL)
        order_feed_page.click_order_in_feed()
        
        with allure.step("Проверяем, что открылось окно с деталями заказа"):
            assert order_feed_page.is_order_details_displayed(), "Окно с деталями не появилось"

    @allure.title("Заказ пользователя отображается в ленте заказов")
    def test_feed_page_user_order_from_history_is_displayed_in_feed(self, driver, created_order, main_page, profile_page, order_feed_page):
        main_page.click_personal_account()
        profile_page.click_history()
        profile_page.wait_for_order_history()
        user_order_number = profile_page.get_last_history_order_number()
        
        driver.get(FEED_URL)
        order_feed_page.wait_for_order_feed_title()
        feed_numbers = order_feed_page.get_all_order_numbers()
        
        with allure.step("Проверяем, что заказ пользователя есть в ленте"):
            assert user_order_number in feed_numbers, f"Заказ пользователя {user_order_number} не найден в ленте заказов"
            
    @allure.title("При создании заказа счётчик 'Выполнено за всё время' увеличивается")
    def test_all_time_orders_counter_increases(self, driver, order_feed_page, authorized_main_page, main_page):
        driver.get(FEED_URL)  
        initial_count = order_feed_page.get_all_time_orders_count()
        
        main_page.click_constructor()
        authorized_main_page.create_order()
        
        driver.get(FEED_URL)
        new_count = order_feed_page.get_all_time_orders_count()
        
        with allure.step("Проверяем, что счётчик увеличился"):
            assert new_count > initial_count, f"Счётчик не увеличился: было {initial_count}, стало {new_count}"
            
    @allure.title("При создании заказа счётчик 'Выполнено за сегодня' увеличивается")
    def test_today_orders_counter_increases(self, driver, order_feed_page, main_page, authorized_main_page):
        driver.get(FEED_URL)
        initial_count = order_feed_page.get_today_orders_count()

        main_page.click_constructor()
        authorized_main_page.create_order()
        
        driver.get(FEED_URL)
        new_count = order_feed_page.get_today_orders_count()
        
        with allure.step("Проверяем, что счётчик увеличился"):
            assert new_count > initial_count, f"Счётчик не увеличился: было {initial_count}, стало {new_count}"

    
    @allure.title("После оформления заказа его номер появляется в разделе 'В работе'")
    def test_order_number_appears_in_progress(self, driver, order_feed_page, main_page, authorized_main_page):
        main_page.click_constructor()
        order_number = authorized_main_page.create_order()
        
        driver.get(FEED_URL)
        order_feed_page.wait_for_order_in_progress(order_number)
        orders_in_progress = order_feed_page.get_orders_in_progress()
        
        with allure.step(f"Проверяем, что заказ #{order_number} есть в разделе 'В работе'"):
            assert order_number in orders_in_progress, f"Заказ {order_number} не найден в разделе 'В работе'. Список: {orders_in_progress}"