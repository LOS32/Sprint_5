from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import StellarBurgersLocators

def test_successful_registration(user_name, user_email, user_password):
    print("Запуск теста на успешную регистрацию")
    driver = webdriver.Chrome()
    #переходим на главную страницу
    driver.get("https://stellarburgers.nomoreparties.site/")
    #нажимаем кнопку войти в аккаунт на главной странице
    driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN).click()
    #нажимаем на ссылку зарегистрироваться под формой входа в аккаунт
    driver.find_element(*StellarBurgersLocators.LINK_TO_REGISTRATION_FORM).click()
    #заполнение формы валидными данными
    driver.find_element(*StellarBurgersLocators.REGISTRATION_NAME_FIELD).send_keys(user_name)
    driver.find_element(*StellarBurgersLocators.REGISTRATION_EMAIL_FIELD).send_keys(user_email)
    driver.find_element(*StellarBurgersLocators.REGISTRATION_PASSWORD_FIELD).send_keys(user_password)
    #нажатие кнопки зарегистрироваться в форме
    driver.find_element(*StellarBurgersLocators.BUTTON_SUBMIT_REGISTRATION).click()

    try:
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
        print("Тест успешной регистрации завершен. Регистрация прошла успешно.")
    except:
        print("Ошибка: регистрация не удалась.")
        raise

    driver.quit()

if __name__ == "__main__":
    test_successful_registration("Dmitrii", "Dmitrii_Losunov_15_222@yandex.ru", "123456")
