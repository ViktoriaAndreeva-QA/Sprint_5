from locators import MainPageLocators
import time


def test_go_from_account_to_constructor(driver):
    driver.get("https://stellarburgers.education-services.ru/login")
    time.sleep(2)

    driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()
    time.sleep(2)
    
    assert "stellarburgers" in driver.current_url and "login" not in driver.current_url


def test_go_from_account_to_constructor_by_logo(driver):
    driver.get("https://stellarburgers.education-services.ru/login")
    time.sleep(2)
    
    driver.find_element(*MainPageLocators.LOGO_BUTTON).click()
    time.sleep(2)
    
    assert "stellarburgers" in driver.current_url and "login" not in driver.current_url