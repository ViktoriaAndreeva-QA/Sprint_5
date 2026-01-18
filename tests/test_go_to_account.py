from locators import MainPageLocators
import time


def test_go_to_personal_account(driver):
    driver.get("https://stellarburgers.education-services.ru/")

    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    
    time.sleep(2)

    assert "login" in driver.current_url