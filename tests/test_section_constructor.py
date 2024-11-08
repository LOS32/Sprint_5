from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import StellarBurgersLocators
from data import URLs

class TestSectionConstructor:
    # Переход на вкладку соусы
    def test_successful_jumps_to_section_sauces(self, driver):
        driver.get(URLs.BASE_URL)
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.SAUCES_SECTION))
        driver.find_element(*StellarBurgersLocators.SAUCES_SECTION).click()
        element = driver.find_element(*StellarBurgersLocators.SAUCES_TAB)
        is_active = StellarBurgersLocators.TAB_ACTIVE_CLASS in element.get_attribute('class')
        assert is_active

    def test_successful_jumps_to_section_fillings(self, driver):
        driver.get(URLs.BASE_URL)
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.FILLINGS_SECTION))
        driver.find_element(*StellarBurgersLocators.FILLINGS_SECTION).click()
        element = driver.find_element(*StellarBurgersLocators.FILLINGS_TAB)
        is_active = StellarBurgersLocators.TAB_ACTIVE_CLASS in element.get_attribute('class')
        assert is_active

    def test_successful_jumps_to_section_buns(self, driver):
        driver.get(URLs.BASE_URL)
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.FILLINGS_SECTION))
        driver.find_element(*StellarBurgersLocators.FILLINGS_SECTION).click()
        driver.find_element(*StellarBurgersLocators.BUNS_SECTION).click()
        element = driver.find_element(*StellarBurgersLocators.BUNS_TAB)
        is_active = StellarBurgersLocators.TAB_ACTIVE_CLASS in element.get_attribute('class')
        assert is_active
