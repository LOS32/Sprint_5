import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import StellarBurgersLocators

@pytest.mark.usefixtures("user_name", "user_email", "user_password")
def test_successful_registration(driver, user_name, user_email, user_password):
    print("Запуск теста на успешную регистрацию")
    #переходим на главную страницу
    driver.get("https://stellarburgers.nomoreparties.site/")
    #нажимаем кнопку войти в аккаунт на главной странице
    driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN).click()
    #нажимаем на ссылку зарегистрироваться под формой входа в аккаунт
    driver.find_element(*StellarBurgersLocators.LINK_TO_REGISTRATION_FORM).click()
    #заполнение формы регистрации валидными данными
    driver.find_element(*StellarBurgersLocators.REGISTRATION_NAME_FIELD).send_keys(user_name)
    driver.find_element(*StellarBurgersLocators.REGISTRATION_EMAIL_FIELD).send_keys(user_email)
    driver.find_element(*StellarBurgersLocators.REGISTRATION_PASSWORD_FIELD).send_keys(user_password)
    #нажатие кнопки зарегистрироваться в форме
    driver.find_element(*StellarBurgersLocators.BUTTON_SUBMIT_REGISTRATION).click()

    #заполнение формы входа для проверки регистрации
@pytest.mark.usefixtures("user_name", "user_email", "user_password")
def test_successful_login(driver, user_name, user_email, user_password):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN).click()
    driver.find_element(*StellarBurgersLocators.LOGIN_NAME_FIELD).send_keys(user_email)
    driver.find_element(*StellarBurgersLocators.PASSWORD_NAME_FIELD).send_keys(user_password)
    driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN_FORM).click()
    #вход в личный кабинет
    driver.find_element(*StellarBurgersLocators.ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Выход']")))
    #print("Тест успешной регистрации завершен. Регистрация прошла успешно.")

    profile_element = driver.find_element(By.XPATH, "//button[text()='Выход']")
    assert profile_element.is_displayed()
    print("Элемент 'Профиль' найден. Тест пройден.")



