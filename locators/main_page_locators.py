from selenium.webdriver.common.by import By


class MainPageLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[.//p[text()='Личный Кабинет']]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")

    INGREDIENT = (By.XPATH, "//a[p[text()='Краторная булка N-200i']]")  # Первый ингредиент
    INGREDIENT_DETAILS_MODAL = (By.XPATH, "//h2[text()='Детали ингредиента']")
    INGREDIENT_DETAILS_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'modal__close')]")

    INGREDIENT_COUNTER = (By.XPATH, "//a[p[text()='Краторная булка N-200i']]//p[contains(@class, 'counter')]")

    ORDER_CONSTRUCTOR = (By.XPATH, "//section[contains(@class, 'BurgerConstructor')]")

    PLACE_ORDER_BUTTON = (By.XPATH,"//button[.//text()[contains(.,'Оформить заказ')]]")
    ORDER_NUMBER = (By.XPATH, "//div[contains(@class, 'modal')]//h2[contains(@class, 'text')]")
    ORDER_DETAILS_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'modal__close')]")