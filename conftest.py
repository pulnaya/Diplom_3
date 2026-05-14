import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.order_feed_page import OrderFeedPage
from urls import LOGIN_PAGE_URL
from data import EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD



@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
        
    yield driver

    driver.quit()

@pytest.fixture
def login_page(driver):
    page = LoginPage(driver)
    return page

@pytest.fixture
def forgot_password_page(driver):
    page = ForgotPasswordPage(driver)
    return page

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    return page


@pytest.fixture
def profile_page(driver):
    page = ProfilePage(driver)
    return page

@pytest.fixture
def order_feed_page(driver):
    page = OrderFeedPage(driver)
    return page

@pytest.fixture
def authorized_main_page(driver, login_page):
    """Фикстура для авторизации пользователя"""
    driver.get(LOGIN_PAGE_URL)
    login_page.login(EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD)
    return MainPage(driver)

@pytest.fixture
def created_order(driver, authorized_main_page):
    """Фикстура для создания заказа и получения его номера"""
    return authorized_main_page.create_order()
