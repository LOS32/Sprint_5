from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import StellarBurgersLocators
from data import URLs, user_name, user_email
from helpers import GenerateCustomData

class TestRegistrationForm:

    def test_successful_registration(self, driver):
        data_generator = GenerateCustomData()
        user_email = data_generator.generate_custom_emale()
        user_password = data_generator.generate_custom_password()
        #переходим на главную страницу
        driver.get(URLs.BASE_URL)
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
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGIN_BUTTON_MAIN_FORM))
        assert driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN_FORM).text == 'Войти'

    def test_registration_with_invalid_password(self, driver):
        #переходим на главную страницу
        driver.get(URLs.BASE_URL)
        #нажимаем кнопку войти в аккаунт на главной странице
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN).click()
        #нажимаем на ссылку зарегистрироваться под формой входа в аккаунт
        driver.find_element(*StellarBurgersLocators.LINK_TO_REGISTRATION_FORM).click()
        #заполнение формы регистрации данными
        driver.find_element(*StellarBurgersLocators.REGISTRATION_NAME_FIELD).send_keys(user_name)
        driver.find_element(*StellarBurgersLocators.REGISTRATION_EMAIL_FIELD).send_keys(user_email)
        driver.find_element(*StellarBurgersLocators.REGISTRATION_PASSWORD_FIELD).send_keys("123")
        #нажатие кнопки зарегистрироваться в форме
        driver.find_element(*StellarBurgersLocators.BUTTON_SUBMIT_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.ERROR_MSSAGE))
        #проверка отображения сообщения об ошибке
        assert driver.find_element(*StellarBurgersLocators.ERROR_MSSAGE).text == 'Некорректный пароль'





