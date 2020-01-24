from selenium import webdriver
import pytest
from Dev.Page.Login_page1 import  Objects


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

        Objects.open(self)
        Objects.enter_wrong_login(self)
        Objects.enter_wrong_password(self)
        Objects.click_enter(self)
        assert self.driver.find_element_by_xpath("//span[text()='User not found']")