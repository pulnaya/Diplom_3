import allure
from urls import LOGIN_PAGE_URL, FORGOT_PASSWORD_URL, RESET_PASSWORD_URL
import data


class TestForgotPasswordPage:

    @allure.title("Переход на страницу восстановления пароля")
    def test_go_to_forgot_password_page(self, login_page):
        login_page.go_to_url(LOGIN_PAGE_URL)
        login_page.click_forgot_password_link()
        
        with allure.step(f"Проверяем редирект на страницу восстановления пароля"):
            assert login_page.get_current_url() == FORGOT_PASSWORD_URL , f'Страница "{FORGOT_PASSWORD_URL}" не открылась'
    
    @allure.title("Ввод почты и клик по кнопке 'Восстановить'")
    def test_enter_email_and_click_restore(self, forgot_password_page):
        forgot_password_page.go_to_url(FORGOT_PASSWORD_URL)
        forgot_password_page.enter_email(data.EXISTING_USER_EMAIL)
        forgot_password_page.click_restore_button()
        forgot_password_page.wait_for_load_reset_password_form()
       
        with allure.step(f"Проверяем редирект на страницу сброса пароля"):
            assert forgot_password_page.get_current_url() == RESET_PASSWORD_URL, f'Страница "{RESET_PASSWORD_URL}" не открылась'

    @allure.title("Кнопка показать/скрыть пароль подсвечивает поле")
    def test_show_password_button_highlights_field(self, forgot_password_page):
        forgot_password_page.go_to_url(FORGOT_PASSWORD_URL)
        forgot_password_page.wait_for_load_forgot_password_form()
        forgot_password_page.enter_email(data.EXISTING_USER_EMAIL)
        forgot_password_page.click_restore_button()
        forgot_password_page.wait_for_load_reset_password_form()
        forgot_password_page.click_show_password_button()    
        
        with allure.step("Проверяем, что поле пароля подсветилось"):
            assert forgot_password_page.is_password_field_active(), "Поле пароля не подсветилось после клика по кнопке"