from conftest import *
from locators import Locators


class TestLogin:

    def test_login_through_authorization_button(self, driver):  # по кнопке «Войти в аккаунт» на главной
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.authorization_button).click()
        driver.find_element(By.XPATH, Locators.email_field).send_keys('zhannagnedaya6093@yandex.ru')
        driver.find_element(By.XPATH, Locators.password_field).send_keys('666666')
        driver.find_element(By.XPATH, Locators.login_button).click()
        order_button = driver.find_element(By.XPATH, Locators.order_button).text
        assert order_button == 'Оформить заказ'

    def test_login_through_profile_button(self, driver):  # через кнопку «Личный кабинет»
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.profile_button).click()
        driver.find_element(By.XPATH, Locators.email_field).send_keys('zhannagnedaya6093@yandex.ru')
        driver.find_element(By.XPATH, Locators.password_field).send_keys('666666')
        driver.find_element(By.XPATH, Locators.login_button).click()
        order_button = driver.find_element(By.XPATH, Locators.order_button).text
        assert order_button == 'Оформить заказ'

    def test_login_through_login_link(self, driver):  # через кнопку в форме регистрации
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.profile_button).click()
        driver.find_element(By.XPATH, Locators.register_link).click()
        driver.find_element(By.XPATH, Locators.login_link).click()
        driver.find_element(By.XPATH, Locators.email_field).send_keys('zhannagnedaya6093@yandex.ru')
        driver.find_element(By.XPATH, Locators.password_field).send_keys('666666')
        driver.find_element(By.XPATH, Locators.login_button).click()
        order_button = driver.find_element(By.XPATH, Locators.order_button).text
        assert order_button == 'Оформить заказ'

    def test_login_through_forgot_password_link(self, driver):  # через кнопку в форме восстановления пароля
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.authorization_button).click()
        driver.find_element(By.XPATH, Locators.forgot_password_link).click()
        driver.find_element(By.XPATH, Locators.login_link).click()
        driver.find_element(By.XPATH, Locators.email_field).send_keys('zhannagnedaya6093@yandex.ru')
        driver.find_element(By.XPATH, Locators.password_field).send_keys('666666')
        driver.find_element(By.XPATH, Locators.login_button).click()
        order_button = driver.find_element(By.XPATH, Locators.order_button).text
        assert order_button == 'Оформить заказ'