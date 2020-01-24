from selenium import webdriver
import pytest
from Dev.Page.Login_page1 import Objects
from Dev.Page.mainpage import main_ob

class TestSite():


    @pytest.fixture()
    def test_setap(self):
        global driver
        self.driver=webdriver.Chrome(Objects.driver_path)
        self.driver.implicitly_wait(10)
        yield
        self.driver.close()
        self.driver.quit()

    def testsss(self,test_setap,):

        Objects.open(self)
        Objects.enter_login(self)
        Objects.enter_password(self)
        Objects.click_enter(self)
        main_ob.clik_on_email(self)
        assert self.driver.title == "PayOp - Merchant Panel"
        main_ob.clik_on_exit(self)
