from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import StellarBurgersLocators
from data import URLs, user_email, user_password

class TestLoginByLoginAccountButton:
#заполнение формы входа для проверки регистрации
    def test_successful_login_from_main_page(self, driver):
        driver.get(URLs.BASE_URL)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_NAME_FIELD).send_keys(user_email)
        driver.find_element(*StellarBurgersLocators.PASSWORD_NAME_FIELD).send_keys(user_password)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN_FORM).click()
        #вход в личный кабинет
        driver.find_element(*StellarBurgersLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGOUT_BUTTON))
        assert driver.find_element(*StellarBurgersLocators.LOGOUT_BUTTON).text == 'Выход'

    #заполнение формы входа через кнопку личный кабинет
    def test_successful_login_from_personal_account(self, driver):
        driver.get(URLs.BASE_URL)
        driver.find_element(*StellarBurgersLocators.ACCOUNT_BUTTON).click()
        #заполнение формы входа
        driver.find_element(*StellarBurgersLocators.LOGIN_NAME_FIELD).send_keys(user_email)
        driver.find_element(*StellarBurgersLocators.PASSWORD_NAME_FIELD).send_keys(user_password)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN_FORM).click()
        #вход в личный кабинет
        driver.find_element(*StellarBurgersLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGOUT_BUTTON))
        assert driver.find_element(*StellarBurgersLocators.LOGOUT_BUTTON).text == 'Выход'

    #заполнение формы входа со страницы регистрации
    def test_successful_login_from_button_registration_form(self, driver):
        #переходим на главную страницу
        driver.get(URLs.BASE_URL)
        #нажимаем кнопку войти в аккаунт на главной странице
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN).click()
        #нажимаем на ссылку зарегистрироваться под формой входа в аккаунт
        driver.find_element(*StellarBurgersLocators.LINK_TO_REGISTRATION_FORM).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_REGISTRATION_FORM).click()
        # заполнение формы входа
        driver.find_element(*StellarBurgersLocators.LOGIN_NAME_FIELD).send_keys(user_email)
        driver.find_element(*StellarBurgersLocators.PASSWORD_NAME_FIELD).send_keys(user_password)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN_FORM).click()
        # вход в личный кабинет
        driver.find_element(*StellarBurgersLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGOUT_BUTTON))
        assert driver.find_element(*StellarBurgersLocators.LOGOUT_BUTTON).text == 'Выход'

    #заполнение формы входа со страницы восстановления пароля
    def test_successful_login_from_password_recovery(self, driver):
        driver.get(URLs.BASE_URL)
        #нажатие кнопки Войти в аккаунт на главной странице
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN).click()
        #нажатие на кнопку восстановление пароля
        driver.find_element(*StellarBurgersLocators.RECOVERY_PASSWORD_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_RECOVERY_FORM).click()
        # заполнение формы входа
        driver.find_element(*StellarBurgersLocators.LOGIN_NAME_FIELD).send_keys(user_email)
        driver.find_element(*StellarBurgersLocators.PASSWORD_NAME_FIELD).send_keys(user_password)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN_FORM).click()
        # вход в личный кабинет
        driver.find_element(*StellarBurgersLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGOUT_BUTTON))
        assert driver.find_element(*StellarBurgersLocators.LOGOUT_BUTTON).text == 'Выход'
