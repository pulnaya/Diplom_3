import allure
from urls import MAIN_PAGE_URL, FEED_URL


class TestMainPage:
    
    @allure.title("Переход по клику на 'Конструктор'")
    def test_go_to_constructor(self, main_page):
        main_page.go_to_url(FEED_URL)
        main_page.click_constructor()
        
        with allure.step("Проверяем, что открылся конструктор"):
            assert main_page.get_current_url() == MAIN_PAGE_URL, f"Ожидали {MAIN_PAGE_URL}, получили {main_page.get_current_url()}"

    @allure.title("Переход по клику на 'Лента заказов'")
    def test_go_to_order_feed(self, main_page):
        main_page.go_to_url(MAIN_PAGE_URL)
        main_page.click_order_feed()
        
        with allure.step("Проверяем, что открылась лента заказов"):
            assert main_page.get_current_url() == FEED_URL, f"Ожидали {FEED_URL}, получили {main_page.get_current_url()}"
    
    @allure.title("Клик на ингредиент открывает окно с деталями")
    def test_ingredient_details_modal_appears(self, main_page):
        main_page.go_to_url(MAIN_PAGE_URL)
        main_page.click_ingredient()
        
        with allure.step("Проверяем, что появилось окно с деталями ингредиента"):
            assert main_page.is_ingredient_details_displayed(), "Окно с деталями не появилось"

    @allure.title("Окно с деталями закрывается кликом по крестику")
    def test_ingredient_details_modal_closes(self, main_page):
        main_page.go_to_url(MAIN_PAGE_URL)
        main_page.click_ingredient()
        main_page.close_ingredient_details()
        
        with allure.step("Проверяем, что окно с деталями закрылось"):
            assert main_page.is_ingredient_details_closed(), "Окно с деталями не закрылось"

    @allure.title("При добавлении ингредиента увеличивается каунтер")
    def test_ingredient_counter_increases(self, main_page):
        main_page.go_to_url(MAIN_PAGE_URL)
        initial_count = main_page.get_ingredient_counter()
        main_page.add_ingredient_to_order()
        
        with allure.step("Проверяем, что каунтер увеличился"):
            assert main_page.get_ingredient_counter() > initial_count, "Каунтер не увеличился после добавления ингредиента"

    @allure.title("Авторизованный пользователь может оформить заказ")
    def test_authorized_user_can_place_order(self, authorized_main_page):
        authorized_main_page.add_ingredient_to_order()
        authorized_main_page.place_order()
        
        with allure.step("Проверяем, что заказ оформлен"):
            assert authorized_main_page.is_order_placed(), "Заказ не оформился"



        
