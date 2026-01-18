from locators import (
    MainPageLocators,
    RegisterPageLocators,
    ForgotPasswordPageLocators
)


def test_login_from_main_button(driver):
    driver.get("https://stellarburgers.education-services.ru/")
    
    driver.find_element(*MainPageLocators.LOGIN_BUTTON_MAIN).click()
    
    import time
    time.sleep(2)
    
    assert "login" in driver.current_url

def test_login_from_account_button(driver):
    driver.get("https://stellarburgers.education-services.ru/")
    
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    
    import time
    time.sleep(2)
    
    assert "login" in driver.current_url


def test_login_from_register_page(driver):
    driver.get("https://stellarburgers.education-services.ru/register")
    
    driver.find_element(*RegisterPageLocators.LOGIN_LINK).click()
    
    import time
    time.sleep(2)
    
    assert "login" in driver.current_url


def test_login_from_forgot_password_page(driver):
    driver.get("https://stellarburgers.education-services.ru/forgot-password")
    
    driver.find_element(*ForgotPasswordPageLocators.LOGIN_LINK).click()
    
    import time
    time.sleep(2)
    
    assert "login" in driver.current_url

