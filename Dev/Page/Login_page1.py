from Dev.Locators_1.login_password import LoginPasswords
from Dev.Locators_1.locators import Locator
from selenium import webdriver


class Objects():
    url = "https://payop.com/ru/auth/login"
    driver_path = "/Users/oleksandrlitvincuk/Downloads/chromedriver2"

    def __init__(self,driver):
        self.driver = driver

    def open(self):
        self.driver.get(Objects.url)

    def dreiver(self):
        self.driver=webdriver.Chrome(Objects.driver_path)


    def enter_login(self):
        #id_email = "email"
        self.driver.find_element_by_id(Locator.email_field_id).send_keys(LoginPasswords.corect_login)

    def enter_password(self):
        self.driver.find_element_by_id(Locator.password_field_id).send_keys(LoginPasswords.corect_password)

    def click_enter(self):
        self.driver.find_element_by_class_name(Locator.enter_buton_class).click()

    def enter_wrong_login(self):
        self.driver.find_element_by_id(Locator.email_field_id).send_keys(LoginPasswords.wrong_login)


    def enter_wrong_password(self):
        self.driver.find_element_by_id(Locator.password_field_id).send_keys(LoginPasswords.wrong_password)