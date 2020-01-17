from selenium import webdriver
import pytest

from Page.Login_page1 import Objects

from Page.mainpage import main_ob

#import allure
#import pytest_html


class TestSite():

    username = "litvinchucksasha@gmail.com"

    @pytest.fixture()
    def test_setap(self):
        global driver
        self.driver=webdriver.Chrome("/Users/oleksandrlitvincuk/Downloads/chromedriver2")
        self.driver.implicitly_wait(10)
        yield
        self.driver.close()
        self.driver.quit()

    def testsss(self,test_setap,):


        self.driver.get("https://payop.com/ru/auth/login")
      #  self.driver.find_element_by_id("email").send_keys("litvinchucksasha@gmail.com")
        Objects.enter_login(self)
        Objects.enter_password(self)
        Objects.click_enter(self)
        #time.sleep(5)
        #assert self.driver.title == "PayOp - Merchant Panel"


        main_ob.clik_on_email(self)
        assert self.driver.title == "PayOp - Merchant Panel"
        main_ob.clik_on_exit(self)
       # time.sleep(3)
       # main_ob.clik_on_email(self)
       # main_ob.clik_on_exit(self)

