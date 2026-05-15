import allure
from urls import MAIN_PAGE_URL, LOGIN_PAGE_URL, ORDER_HISTORY_URL, PROFILE_URL


class TestProfilePage:
    
    @allure.title("Переход в личный кабинет неавторизованным пользователем")
    def test_go_to_profile_unauthorized(self, main_page):
        main_page.go_to_url(MAIN_PAGE_URL)
        main_page.click_personal_account()
        
        with allure.step("Проверяем редирект на страницу входа"):
            assert main_page.get_current_url() == LOGIN_PAGE_URL, f"Ожидали {LOGIN_PAGE_URL}, получили {profile_page.get_current_url()}"
    
    @allure.title("Переход в личный кабинет авторизованным пользователем")
    def test_go_to_profile_authorized(self, authorized_main_page, profile_page):
        authorized_main_page.click_personal_account() 
        profile_page.wait_for_profile_page_loaded()
    
        with allure.step("Проверяем, что открылась страница профиля"):
            assert profile_page.get_current_url() == PROFILE_URL, f"Ожидали {PROFILE_URL}, получили {profile_page.get_current_url()}"

    @allure.title("Переход в раздел 'История заказов'")
    def test_go_to_order_history(self, authorized_main_page, profile_page):
        authorized_main_page.click_personal_account()
        profile_page.click_history()
        
        with allure.step("Проверяем, что открылась история заказов"):
            assert profile_page.get_current_url() == ORDER_HISTORY_URL, f"Ожидали {ORDER_HISTORY_URL}, получили {profile_page.get_current_url()}"

    @allure.title("Выход из аккаунта")
    def test_logout(self, authorized_main_page, profile_page, login_page):
        authorized_main_page.click_personal_account()
        profile_page.click_logout()
        login_page.wait_for_login_page_loaded()

        with allure.step("Проверяем, что произошёл выход из аккаунта"):
            assert profile_page.get_current_url() == LOGIN_PAGE_URL, f"Ожидали {LOGIN_PAGE_URL}, получили {profile_page.get_current_url()}"