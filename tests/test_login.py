from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import (
    MainPageLocators,
    RegisterPageLocators,
    ForgotPasswordPageLocators
)
from constants import Urls


def test_login_from_main_button(driver):
    driver.get(Urls.main_page())
    
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON_MAIN)).click()
    
    wait.until(EC.url_contains("login"))
    
    assert "login" in driver.current_url

def test_login_from_account_button(driver):
    driver.get(Urls.main_page())
    
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
    
    wait.until(EC.url_contains("login"))
    
    assert "login" in driver.current_url


def test_login_from_register_page(driver):
    driver.get(Urls.register_page())
    
    wait = WebDriverWait(driver, 10)
    
    wait.until(EC.visibility_of_element_located(RegisterPageLocators.NAME_INPUT))
    
    wait.until(EC.element_to_be_clickable(RegisterPageLocators.LOGIN_LINK)).click()
    
    wait.until(EC.url_contains("login"))
    
    assert "login" in driver.current_url


def test_login_from_forgot_password_page(driver):
    driver.get(Urls.forgot_password_page())
    
    wait = WebDriverWait(driver, 10)
    
    wait.until(EC.element_to_be_clickable(ForgotPasswordPageLocators.LOGIN_LINK)).click()
    
    wait.until(EC.url_contains("login"))
    
    assert "login" in driver.current_url

