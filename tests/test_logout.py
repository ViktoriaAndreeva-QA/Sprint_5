from locators import (
    MainPageLocators, 
    PersonalAccountLocators, 
    LoginPageLocators
)
import time


def test_logout_from_account(driver):
    REAL_EMAIL = "ivanivanov13234@yandex.ru"
    REAL_PASSWORD = "password123"
    
    driver.get("https://stellarburgers.education-services.ru/login")
    time.sleep(3)
    
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(REAL_EMAIL)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(REAL_PASSWORD)
    time.sleep(2)

    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    time.sleep(2)

    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    time.sleep(3)
    
    logout_button = driver.find_element(*PersonalAccountLocators.LOGOUT_BUTTON)
    logout_button.click()
    time.sleep(2)

    assert "login" in driver.current_url
