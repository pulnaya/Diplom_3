import allure
from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators


class ProfilePage(BasePage):

    @allure.step("Ожидание загрузки страницы профиля")
    def wait_for_profile_page_loaded(self):
        self.wait_for_element_visible(ProfilePageLocators.PROFILE_HEADER)
    
    @allure.step("Клик на 'История заказов'")  
    def click_history(self):
        self.click_to_element(ProfilePageLocators.HISTORY_LINK)
    
    @allure.step("Клик на 'Выход'") 
    def click_logout(self):
        self.click_to_element(ProfilePageLocators.LOGOUT_BUTTON)

    @allure.step("Ожидание загрузки истории заказов")
    def wait_for_order_history(self):
        self.wait_for_element_visible(ProfilePageLocators.ORDER_IN_HISTORY)

    @allure.step("Получение номера последнего заказа в истории")
    def get_last_history_order_number(self):
        elements = self.find_elements_with_wait(ProfilePageLocators.ORDER_NUMBER_IN_HISTORY)
        if elements:
            return elements[-1].text
        return None
