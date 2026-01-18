"""
Генераторы тестовых данных для регистрации
"""
import random
import string


def generate_email():
    name = "Viktoria"
    surname = "Andreeva"
    cohort = "39"
    
    random_digits = random.randint(100, 999)
    
    return f"{name}_{surname}_{cohort}_{random_digits}@yandex.ru"


def generate_password(length=10):
    if length < 6:
        length = 6
    
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))


# ФИКСИРОВАННЫЕ ДАННЫЕ ДЛЯ ТЕСТОВ
class TestData:
    TEST_NAME = "Виктория Андреева"         # Имя для регистрации
    VALID_PASSWORD = "Password123"          # Валидный пароль (10 символов)
    SHORT_PASSWORD = "12345"                # Невалидный пароль (5 символов)
    MIN_PASSWORD_LENGTH = 6                 # Минимальная длина пароля

