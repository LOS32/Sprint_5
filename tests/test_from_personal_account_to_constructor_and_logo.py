from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import StellarBurgersLocators
from data import user_email, user_password

#переход из личногокабинета в конструктор
def test_click_on_constructor(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN).click()
    driver.find_element(*StellarBurgersLocators.LOGIN_NAME_FIELD).send_keys(user_email)
    driver.find_element(*StellarBurgersLocators.PASSWORD_NAME_FIELD).send_keys(user_password)
    driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN_FORM).click()
    #вход в личный кабинет
    driver.find_element(*StellarBurgersLocators.ACCOUNT_BUTTON).click()
    driver.find_element(*StellarBurgersLocators.CONSTRUCTOR_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[text()='Конструктор']")))
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[text()='Булки']")))
    assert driver.find_element(By.XPATH, "//span[text()='Булки']").text == 'Булки'

#переход из личногокабинета по логотипу Stellar Burgers
def test_click_on_logo(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN).click()
    driver.find_element(*StellarBurgersLocators.LOGIN_NAME_FIELD).send_keys(user_email)
    driver.find_element(*StellarBurgersLocators.PASSWORD_NAME_FIELD).send_keys(user_password)
    driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN_FORM).click()
    #вход в личный кабинет
    driver.find_element(*StellarBurgersLocators.ACCOUNT_BUTTON).click()
    driver.find_element(*StellarBurgersLocators.LOGO_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[text()='Булки']")))
    assert driver.find_element(By.XPATH, "//span[text()='Булки']").text == 'Булки'