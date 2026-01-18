"""
conftest.py - все фикстуры pytest
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from data import generate_email, generate_password, TEST_NAME, SHORT_PASSWORD


@pytest.fixture
def driver():
    """Фикстура драйвера Chrome"""
    options = Options()
    options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    
    yield driver
    driver.quit()


@pytest.fixture
def test_user():
    """Фикстура тестового пользователя"""
    return {
        'name': TEST_NAME,
        'email': generate_email(),
        'password': generate_password(10),
        'short_password': SHORT_PASSWORD
    }
