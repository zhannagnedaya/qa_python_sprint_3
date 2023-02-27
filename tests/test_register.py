from conftest import *
import random
from locators import Locators


class TestRegister:

    def test_register_success(self, driver):  # успешная регистрация
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.profile_button).click()
        driver.find_element(By.XPATH, Locators.register_link).click()
        driver.find_element(By.NAME, Locators.name_field).send_keys('zhanna')
        driver.find_element(By.XPATH, Locators.email_field).send_keys('zhannagnedaya60931@ya.ru')
        driver.find_element(By.XPATH, Locators.password_field).send_keys('666666')
        driver.find_element(By.XPATH, Locators.register_button).click()
        login_button = driver.find_element(By.XPATH, Locators.login_button).text
        assert login_button == 'Войти'

    def test_register_incorrect_password(self, driver):   # ошибка для некорректного пароля
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.profile_button).click()
        driver.find_element(By.XPATH, Locators.register_link).click()
        driver.find_element(By.NAME, Locators.name_field).send_keys('zhanna')
        driver.find_element(By.XPATH, Locators.email_field).send_keys('zhannagnedaya60932@ya.ru')
        driver.find_element(By.XPATH, Locators.password_field).send_keys('666')
        driver.find_element(By.XPATH, Locators.register_button).click()
        incorrect_password_message = driver.find_element(By.XPATH, Locators.incorrect_password_message).text
        assert incorrect_password_message == 'Некорректный пароль'