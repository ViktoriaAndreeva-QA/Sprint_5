"""
Локаторы для сайта Stellar Burgers
https://stellarburgers.education-services.ru/
"""


from selenium.webdriver.common.by import By

# ==================== ГЛАВНАЯ СТРАНИЦА (Главное меню) ====================
class MainPageLocators:
    # 1. Кнопка «Войти в аккаунт» на главной странице
    LOGIN_BUTTON_MAIN = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    
    # 2. Кнопка «Личный Кабинет» в хедере
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    
    # 3. Кнопка «Конструктор» в хедере
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
    
    # 4. Логотип Stellar Burgers в хедере
    LOGO_BUTTON = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")
    
    # 5. Раздел «Булки» в конструкторе
    BUNS_SECTION = (By.XPATH, ".//span[text()='Булки']")
    
    # 6. Раздел «Соусы» в конструкторе
    SAUCES_SECTION = (By.XPATH, ".//span[text()='Соусы']")
    
    # 7. Раздел «Начинки» в конструкторе
    TOPPINGS_SECTION = (By.XPATH, ".//span[text()='Начинки']")
    
    # 8. Активный раздел в конструкторе (для проверки)
    ACTIVE_SECTION = (By.CLASS_NAME, "tab_tab_type_current__2BEPc")

    # 9. Заголовок страницы "Соберите бургер"
    PAGE_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")

# ==================== СТРАНИЦА РЕГИСТРАЦИИ ====================
class RegisterPageLocators:
    # 1. Поле ввода «Имя» в форме регистрации
    NAME_INPUT = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")
    
    # 2. Поле ввода «Email» в форме регистрации
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    
    # 3. Поле ввода «Пароль» в форме регистрации
    PASSWORD_INPUT = (By.XPATH, ".//input[@type='password']")
    
    # 4. Кнопка «Зарегистрироваться»
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    
    # 5. Сообщение об ошибке для некорректного пароля
    PASSWORD_ERROR = (By.CLASS_NAME, "input__error")
    
    # 6. Ссылка «Войти» под формой регистрации
    LOGIN_LINK = (By.XPATH, ".//a[text()='Войти']")

# ==================== СТРАНИЦА ВХОДА (Логин) ====================
class LoginPageLocators:
    # 1. Поле ввода «Email» на странице входа
    EMAIL_INPUT = (By.XPATH, ".//input[@name='name']")
    
    # 2. Поле ввода «Пароль» на странице входа
    PASSWORD_INPUT = (By.XPATH, ".//input[@name='Пароль']")
    
    # 3. Кнопка «Войти» на странице входа
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    
    # 4. Заголовок «Вход» на странице входа
    LOGIN_TITLE = (By.XPATH, ".//h2[text()='Вход']")

# ==================== СТРАНИЦА ВОССТАНОВЛЕНИЯ ПАРОЛЯ ====================
class ForgotPasswordPageLocators:
    # 1. Поле ввода «Email» на странице восстановления пароля
    EMAIL_INPUT = (By.XPATH, ".//input[@name='name']")
    
    # 2. Кнопка «Восстановить» на странице восстановления пароля
    RECOVER_BUTTON = (By.XPATH, ".//button[text()='Восстановить']")
    
    # 3. Ссылка «Войти» на странице восстановления пароля
    LOGIN_LINK = (By.XPATH, ".//a[text()='Войти']")

    # 4. Заголовок страницы восстановления пароля (для ожидания загрузки)
    PAGE_TITLE = (By.XPATH, "//h2[contains(text(), 'Восстановление пароля')]")

# ==================== ЛИЧНЫЙ КАБИНЕТ ====================
class PersonalAccountLocators:
    # 1. Текст «В этом разделе вы можете изменить свои персональные данные» в ЛК
    PROFILE_TEXT = (By.XPATH, ".//p[text()='В этом разделе вы можете изменить свои персональные данные']")
    
    # 2. Кнопка «Выход» в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")
    
    # 3. Вкладка «Профиль» в личном кабинете
    PROFILE_LINK = (By.XPATH, ".//a[text()='Профиль']")

# ==================== ОБЩИЕ ЭЛЕМЕНТЫ ====================
class CommonLocators:
    # 1. Сообщение об успешной регистрации
    SUCCESS_MESSAGE = (By.XPATH, ".//div[contains(text(), 'Вы успешно зарегистрировались!')]")
    
    # 2. Индикатор загрузки (лоадер)
    LOADING_SPINNER = (By.CLASS_NAME, "loader")