import allure
from urls import MAIN_PAGE_URL, LOGIN_PAGE_URL, ORDER_HISTORY_URL, PROFILE_URL


class TestProfilePage:
    
    @allure.title("Переход в личный кабинет неавторизованным пользователем")
    def test_go_to_profile_unauthorized(self, driver, main_page):
        driver.get(MAIN_PAGE_URL)
        main_page.click_personal_account()
        
        with allure.step("Проверяем редирект на страницу входа"):
            assert driver.current_url == LOGIN_PAGE_URL, f"Ожидали {LOGIN_PAGE_URL}, получили {driver.current_url}"
    
    @allure.title("Переход в личный кабинет авторизованным пользователем")
    def test_go_to_profile_authorized(self, driver, authorized_main_page, profile_page):
        authorized_main_page.click_personal_account() 
        profile_page.wait_for_profile_page_loaded()
    
        with allure.step("Проверяем, что открылась страница профиля"):
            assert driver.current_url == PROFILE_URL, f"Ожидали {PROFILE_URL}, получили {driver.current_url}"

    @allure.title("Переход в раздел 'История заказов'")
    def test_go_to_order_history(self, driver, authorized_main_page, profile_page):
        authorized_main_page.click_personal_account()
        profile_page.click_history()
        
        with allure.step("Проверяем, что открылась история заказов"):
            assert driver.current_url == ORDER_HISTORY_URL, f"Ожидали {ORDER_HISTORY_URL}, получили {driver.current_url}"

    @allure.title("Выход из аккаунта")
    def test_logout(self, driver, authorized_main_page, profile_page, login_page):
        authorized_main_page.click_personal_account()
        profile_page.click_logout()
        login_page.wait_for_login_page_loaded()

        with allure.step("Проверяем, что произошёл выход из аккаунта"):
            assert driver.current_url == LOGIN_PAGE_URL, f"Ожидали {LOGIN_PAGE_URL}, получили {driver.current_url}"