from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegisterPageLocators
from constants import Urls
from data import TestData, generate_email


class TestRegistration:
    def test_successful_registration(self, driver):
        
        driver.get(Urls.register_page())

        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(RegisterPageLocators.NAME_INPUT))
        
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(TestData.TEST_NAME)
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(TestData.VALID_PASSWORD)

        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
        
        wait.until(EC.url_contains("login"))
        
        assert "login" in driver.current_url

    def test_invalid_password_error(self, driver):
        driver.get(Urls.register_page())
        
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(RegisterPageLocators.NAME_INPUT))
        
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(TestData.TEST_NAME)
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(TestData.SHORT_PASSWORD)

        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
        
        wait.until(EC.url_to_be(Urls.register_page()))
        
        assert "register" in driver.current_url
