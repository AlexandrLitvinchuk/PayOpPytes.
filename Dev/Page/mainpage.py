from Dev.Locators_1.locators import Locator


class main_ob():
    id_email = "email"

    def __init__(self,driver):
        self.driver = driver


  #  def click_enter(self):
   #     self.driver.find_element_by_class_name(Locators_1.enter_buton_class).click

    def clik_on_email(self):
        self.driver.find_element_by_xpath(Locator.email_link_xpath).click()

    def clik_on_exit(self):
        self.driver.find_element_by_xpath(Locator.logout_link_xpath).click()
