from selenium import webdriver
import pytest

@pytest.fixture
def user_name():
    return "Dmitrii"

@pytest.fixture
def user_email():
    return "Dmitrii_Losunov_15_230@yandex.ru"

@pytest.fixture
def user_password():
    return "123456"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()