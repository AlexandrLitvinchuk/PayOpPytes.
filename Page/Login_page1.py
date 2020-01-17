from Locators.login_password import LoginPasswords
from Locators.locators import Locators


class Objects():
    id_email = "email"

    def __init__(self,driver):
        self.driver = driver



    def enter_login(self):
        #id_email = "email"
        self.driver.find_element_by_id(Locators.email_field_id).send_keys(LoginPasswords.corect_login)

    def enter_password(self):
        self.driver.find_element_by_id(Locators.password_field_id).send_keys(LoginPasswords.corect_password)

    def click_enter(self):
        self.driver.find_element_by_class_name(Locators.enter_buton_class).click()

    def enter_wrong_login(self):
        self.driver.find_element_by_id(Locators.email_field_id).send_keys(LoginPasswords.wrong_login)


    def enter_wrong_password(self):
        self.driver.find_element_by_id(Locators.password_field_id).send_keys(LoginPasswords.wrong_password)


