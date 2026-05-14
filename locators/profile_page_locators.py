from selenium.webdriver.common.by import By


class ProfilePageLocators:
    HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    PROFILE_HEADER = (By.XPATH, "//a[text()='Профиль']")

    ORDER_IN_HISTORY = (By.XPATH, "//a[contains(@class, 'OrderHistory_link')]")
    ORDER_NUMBER_IN_HISTORY = (By.XPATH, "//a[contains(@class, 'OrderHistory_link')]//p[contains(@class, 'text_type_digits-default')]")