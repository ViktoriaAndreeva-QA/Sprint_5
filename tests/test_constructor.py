from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Urls
from locators import MainPageLocators


def test_buns_section(driver):
    driver.get(Urls.main_page())

    wait = WebDriverWait(driver, 10)
    
    wait.until(EC.visibility_of_element_located(MainPageLocators.PAGE_TITLE))
    
    sauces_tab = wait.until(EC.element_to_be_clickable(MainPageLocators.SAUCES_SECTION))
    sauces_tab.click()
    
    buns_tab = wait.until(EC.element_to_be_clickable(MainPageLocators.BUNS_SECTION))
    buns_tab.click()
    
    assert "Булки" in driver.find_element(*MainPageLocators.ACTIVE_SECTION).text


def test_sauces_section(driver):
    driver.get(Urls.main_page())
    
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(MainPageLocators.PAGE_TITLE))
    
    sauces_tab = wait.until(EC.element_to_be_clickable(MainPageLocators.SAUCES_SECTION))
    sauces_tab.click()
    
    assert "Соусы" in driver.find_element(*MainPageLocators.ACTIVE_SECTION).text


def test_toppings_section(driver):
    driver.get(Urls.main_page())
    
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(MainPageLocators.PAGE_TITLE))
    
    toppings_tab = wait.until(EC.element_to_be_clickable(MainPageLocators.TOPPINGS_SECTION))
    toppings_tab.click()
    
    assert "Начинки" in driver.find_element(*MainPageLocators.ACTIVE_SECTION).text

