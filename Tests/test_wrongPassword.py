from selenium import webdriver
import re
import pytest
from Page.Login_page import Objects


class TestSite1():

    username = "litvinchucksasha@gmail.com"

    @pytest.fixture()
    def test_setap(self):
        global driver
        self.driver=webdriver.Chrome("/Users/oleksandrlitvincuk/Downloads/chromedriver2")
        self.driver.implicitly_wait(10)
        yield
        self.driver.close()

    def testsss(self,test_setap,):
        username = "litvinchucksasha@gmail.com"

        self.driver.get("https://payop.com/ru/auth/login")
      #  self.driver.find_element_by_id("email").send_keys("litvinchucksasha@gmail.com")
        Objects.enter_login(self)
        Objects.enter_wrong_password(self)
        Objects.click_enter(self)
        assert self.driver.find_element_by_xpath("//span[text()='User not found']")
       # time.sleep(3)
       # main_ob.clik_on_email(self)
        #main_ob.clik_on_exit(self)

