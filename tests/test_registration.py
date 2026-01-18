from locators import RegisterPageLocators


class TestRegistration:
    def test_successful_registration(self, driver, test_user):
        
        driver.get("https://stellarburgers.education-services.ru/register")

        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(test_user['name'])
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(test_user['email'])
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(test_user['password'])

        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        import time
        time.sleep(3)

        assert "login" in driver.current_url

    def test_invalid_password_error(self, driver, test_user):
        driver.get("https://stellarburgers.education-services.ru/register")

        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(test_user['name'])
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(test_user['email'])
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(test_user['short_password'])

        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        import time
        time.sleep(3)

        assert "register" in driver.current_url
