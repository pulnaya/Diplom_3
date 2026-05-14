import allure
from pages.base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordLocators


class ForgotPasswordPage(BasePage):

    @allure.step("Ожидание загрузки формы восстановления пароля")
    def wait_for_load_forgot_password_form(self):
        self.wait_for_element_visible(ForgotPasswordLocators.HEADER)

    @allure.step("Ввод email")
    def enter_email(self, email):
        self.text_input_to_element(ForgotPasswordLocators.EMAIL_INPUT, email)

    @allure.step("Клик по кнопке 'Восстановить'")
    def click_restore_button(self):
        self.click_to_element(ForgotPasswordLocators.RESTORE_BUTTON)

    @allure.step("Ожидание загрузки формы сброса пароля")
    def wait_for_load_reset_password_form(self):
        self.wait_for_element_visible(ForgotPasswordLocators.PASSWORD_INPUT)

    @allure.step("Клик по кнопке показать/скрыть пароль")
    def click_show_password_button(self):
        self.click_to_element(ForgotPasswordLocators.SHOW_PASSWORD_BUTTON)

    @allure.step("Проверка активности поля пароля")
    def is_password_field_active(self):
        return self.is_element_visible(ForgotPasswordLocators.PASSWORD_INPUT_ACTIVE)
        