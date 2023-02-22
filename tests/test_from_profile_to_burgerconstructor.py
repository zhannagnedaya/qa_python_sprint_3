from conftest import *
from locators import Locators


class TestFromPrivate_room_to_constructor:

    def test_move_by_click_to_constructor(self, driver):  # по клику на «Конструктор»
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.profile_button).click()
        driver.find_element(By.XPATH, Locators.constructor_button).click()
        constructor_h1 = driver.find_element(By.XPATH, Locators.constructor_h1).text
        assert constructor_h1 == 'Соберите бургер'

    def test_move_by_click_to_logo_with_registration(self, driver):  # по клику на логотип Stellar Burgers
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.profile_button).click()
        driver.find_element(By.XPATH, Locators.email_field).send_keys('zhannagnedaya6093@yandex.ru')
        driver.find_element(By.XPATH, Locators.password_field).send_keys('666666')
        driver.find_element(By.XPATH, Locators.login_button).click()
        driver.find_element(By.XPATH, Locators.logo).click()
        constructor_h1 = driver.find_element(By.XPATH, Locators.constructor_h1).text
        assert constructor_h1 == 'Соберите бургер'