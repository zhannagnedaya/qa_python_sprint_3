from conftest import *
from locators import Locators
import time

class TestToProfile:

    def test_to_profile_before_login(self, driver):  # по клику на «Личный кабинет» до авторизации
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.profile_button).click()
        login_h2 = driver.find_element(By.XPATH, Locators.login_h2).text
        assert login_h2 == 'Вход'

    def test_to_profile_after_login(self, driver):  # по клику на «Личный кабинет» после авторизации
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.authorization_button).click()
        driver.find_element(By.XPATH, Locators.email_field).send_keys('zhannagnedaya6093@yandex.ru')
        driver.find_element(By.XPATH, Locators.password_field).send_keys('666666')
        driver.find_element(By.XPATH, Locators.login_button).click()
        time.sleep(1)
        driver.find_element(By.XPATH, Locators.profile_button).click()
        save_button = driver.find_element(By.XPATH, Locators.save_button).text
        assert save_button == 'Сохранить'