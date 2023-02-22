from conftest import *
from locators import Locators
import time

class TestLogout:

    def test_logout(self, driver):  # по кнопке «Выйти» в личном кабинете
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.authorization_button).click()
        driver.find_element(By.XPATH, Locators.email_field).send_keys('zhannagnedaya6093@yandex.ru')
        driver.find_element(By.XPATH, Locators.password_field).send_keys('666666')
        driver.find_element(By.XPATH, Locators.login_button).click()
        time.sleep(1)
        driver.find_element(By.XPATH, Locators.profile_button).click()
        driver.find_element(By.XPATH, Locators.logout_button).click()
        login_button = driver.find_element(By.XPATH, Locators.login_button).text
        assert login_button == 'Войти'