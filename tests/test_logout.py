from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import (
    MainPageLocators, 
    PersonalAccountLocators, 
    LoginPageLocators
)
from constants import Urls


def test_logout_from_account(driver):
    REAL_EMAIL = "ivanivanov13234@yandex.ru"
    REAL_PASSWORD = "password123"
    
    driver.get(Urls.login_page())
    
    wait = WebDriverWait(driver, 10)
    
    wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
    
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(REAL_EMAIL)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(REAL_PASSWORD)

    wait.until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)).click()
    
    wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
    
    wait.until(EC.element_to_be_clickable(PersonalAccountLocators.LOGOUT_BUTTON)).click()

    wait.until(EC.url_contains("login"))

    assert "login" in driver.current_url
