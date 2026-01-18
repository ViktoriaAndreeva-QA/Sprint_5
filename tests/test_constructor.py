from selenium.webdriver.common.by import By
import time


def test_buns_section(driver):
    driver.get("https://stellarburgers.education-services.ru/")
    time.sleep(2)
    
    driver.find_element(By.XPATH, "//span[text()='Соусы']").click()
    time.sleep(1)
    
    driver.find_element(By.XPATH, "//span[text()='Булки']").click()
    time.sleep(1)
    
    assert "Булки" in driver.find_element(By.CLASS_NAME, "tab_tab_type_current__2BEPc").text


def test_sauces_section(driver):
    driver.get("https://stellarburgers.education-services.ru/")
    time.sleep(2)
    
    driver.find_element(By.XPATH, "//span[text()='Соусы']").click()
    time.sleep(1)
    
    assert "Соусы" in driver.find_element(By.CLASS_NAME, "tab_tab_type_current__2BEPc").text


def test_toppings_section(driver):
    driver.get("https://stellarburgers.education-services.ru/")
    time.sleep(2)
    
    driver.find_element(By.XPATH, "//span[text()='Начинки']").click()
    time.sleep(1)
    
    assert "Начинки" in driver.find_element(By.CLASS_NAME, "tab_tab_type_current__2BEPc").text

