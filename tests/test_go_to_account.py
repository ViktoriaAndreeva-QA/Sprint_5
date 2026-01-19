from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators
from constants import Urls


def test_go_to_personal_account(driver):
    driver.get(Urls.main_page())
    
    wait = WebDriverWait(driver, 10)

    wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
    
    wait.until(EC.url_contains("login"))

    assert "login" in driver.current_url