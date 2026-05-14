from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    HEADER = (By.XPATH, "//h2[text()='Восстановление пароля']")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    SHOW_PASSWORD_BUTTON = (By.CSS_SELECTOR, ".input__icon-action")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    PASSWORD_INPUT_ACTIVE = (By.CSS_SELECTOR, ".input_status_active")