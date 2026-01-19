from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators
from constants import Urls


def test_go_from_account_to_constructor(driver):
    driver.get(Urls.login_page())

    wait = WebDriverWait(driver, 10)

    wait.until(EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)).click()
    
    assert "stellarburgers" in driver.current_url and "login" not in driver.current_url


def test_go_from_account_to_constructor_by_logo(driver):
    driver.get(Urls.login_page())
    
    wait = WebDriverWait(driver, 10)
    
    wait.until(EC.element_to_be_clickable(MainPageLocators.LOGO_BUTTON)).click()
    
    assert "stellarburgers" in driver.current_url and "login" not in driver.current_url