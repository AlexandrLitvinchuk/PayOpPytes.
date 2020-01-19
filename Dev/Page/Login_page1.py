from Dev.Locators_1.login_password import LoginPasswords
from Dev.Locators_1.locators import Locator


class Objects():
    id_email = "email"

    def __init__(self,driver):
        self.driver = driver



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


