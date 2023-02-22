from conftest import *
from locators import Locators


class TestSections:

    def test_buns_section(self, driver):  # переход к разделу «Булки»
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.authorization_button).click()
        driver.find_element(By.XPATH, Locators.email_field).send_keys('zhannagnedaya6093@yandex.ru')
        driver.find_element(By.XPATH, Locators.password_field).send_keys('666666')
        driver.find_element(By.XPATH, Locators.login_button).click()
        driver.find_element(By.XPATH, Locators.sauces_section).click()
        driver.find_element(By.XPATH, Locators.no_select_buns_section)
        driver.find_element(By.XPATH, Locators.buns_section).click()
        driver.find_element(By.XPATH, Locators.select_buns_section)

    def test_sauces_section(self, driver):  # переход к разделу «Соусы»
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.authorization_button).click()
        driver.find_element(By.XPATH, Locators.email_field).send_keys('zhannagnedaya6093@yandex.ru')
        driver.find_element(By.XPATH, Locators.password_field).send_keys('666666')
        driver.find_element(By.XPATH, Locators.login_button).click()
        driver.find_element(By.XPATH, Locators.sauces_section).click()
        driver.find_element(By.XPATH, Locators.select_sauces_section)

    def test_toppings_section(self, driver):  # переход к разделу «Начинки»
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.authorization_button).click()
        driver.find_element(By.XPATH, Locators.email_field).send_keys('zhannagnedaya6093@yandex.ru')
        driver.find_element(By.XPATH, Locators.password_field).send_keys('666666')
        driver.find_element(By.XPATH, Locators.login_button).click()
        driver.find_element(By.XPATH, Locators.toppings_section).click()
        driver.find_element(By.XPATH, Locators.select_toppings_section)