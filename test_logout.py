from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import StellarBurgersLocators

#заполнение формы входа для проверки регистрации
def test_successful_logout(driver, user_email, user_password):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN).click()
    driver.find_element(*StellarBurgersLocators.LOGIN_NAME_FIELD).send_keys(user_email)
    driver.find_element(*StellarBurgersLocators.PASSWORD_NAME_FIELD).send_keys(user_password)
    driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN_FORM).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[text()='Личный Кабинет']")))
    #вход в личный кабинет
    driver.find_element(*StellarBurgersLocators.ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Выход']")))
    driver.find_element(*StellarBurgersLocators.LOGOUT_BUTTON).click()
    #проверка, что после выхода отображается элемент, указывающий на успешный выход
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Войти']")))
    assert driver.find_element(By.XPATH, "//button[text()='Войти']").text == 'Войти'