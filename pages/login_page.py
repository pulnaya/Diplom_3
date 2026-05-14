import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginLocators
from locators.main_page_locators import MainPageLocators


class LoginPage(BasePage):

    @allure.step("Ожидание загрузки страницы логина")
    def wait_for_login_page_loaded(self):
        self.wait_for_element_visible(LoginLocators.LOGIN_HEADER)

    @allure.step("Клик по ссылке 'Восстановить пароль")
    def click_forgot_password_link(self):
        self.click_to_element(LoginLocators.FORGOT_PASSWORD_LINK)

    @allure.step("Вход в аккаунт")
    def login(self, email, password):
        self.text_input_to_element(LoginLocators.EMAIL_INPUT, email)
        self.text_input_to_element(LoginLocators.PASSWORD_INPUT, password)
        self.click_to_element(LoginLocators.LOGIN_BUTTON)
        self.wait_for_element_visible(MainPageLocators.PLACE_ORDER_BUTTON)
