from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import StellarBurgersLocators

class TestSectionConstructor:
    # Переход на вкладку соусы
    def test_successful_jumps_to_section_sauces(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[text()='Соусы']")))
        driver.find_element(*StellarBurgersLocators.SAUCES_SECTION).click()
        element = driver.find_element(By.XPATH, "//span[text()='Соусы']/ancestor::div[contains(@class, 'tab_tab__1SPyG')]")
        is_active = 'tab_tab_type_current__2BEPc' in element.get_attribute('class')
        assert is_active, "Вкладка 'Соусы' не активна"
        print("Вкладка 'Соусы' активна.")

    def test_successful_jumps_to_section_fillings(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[text()='Начинки']")))
        driver.find_element(*StellarBurgersLocators.FILLINGS_SECTION).click()
        element = driver.find_element(By.XPATH, "//span[text()='Начинки']/ancestor::div[contains(@class, 'tab_tab__1SPyG')]")
        is_active = 'tab_tab_type_current__2BEPc' in element.get_attribute('class')
        assert is_active, "Вкладка 'Начинки' не активна"
        print("Вкладка 'Начинки' активна.")

    def test_successful_jumps_to_section_buns(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[text()='Начинки']")))
        driver.find_element(*StellarBurgersLocators.FILLINGS_SECTION).click()
        driver.find_element(*StellarBurgersLocators.BUNS_SECTION).click()
        element = driver.find_element(By.XPATH, "//span[text()='Булки']/ancestor::div[contains(@class, 'tab_tab__1SPyG')]")
        is_active = 'tab_tab_type_current__2BEPc' in element.get_attribute('class')
        assert is_active, "Вкладка 'Булки' не активна"
        print("Вкладка 'Булки' активна.")