from selenium.webdriver.common.by import By


class OrderFeedLocators:
    ORDER_IN_FEED = (By.XPATH, "//a[contains(@class, 'OrderHistory_link')]")
    ORDER_DETAILS_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_orderBox')]")

    ORDER_FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    ORDER_LINK_NUMBER = (By.XPATH, "//a[contains(@class, 'OrderHistory_link')]//p[contains(@class, 'text_type_digits-default')]")

    ALL_TIME_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    ORDER_IN_PROGRESS_NUMBER = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]//li")
    ORDER_IN_PROGRESS_BY_NUMBER = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]//li[text()='{}']")
      