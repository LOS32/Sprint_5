import pytest

@pytest.fixture
def user_name():
    return "Dmitrii"

@pytest.fixture
def user_email():
    return "Dmitrii_Losunov_15_222@yandex.ru"

@pytest.fixture
def user_password():
    return "123456"