import pytest
from selenium import webdriver
from Utilities.ReadProperties import Readconfig
from PageObject.LoginPage import LoginPage
from Utilities.customlogger import LogGen


class Test_HomePage_001:
    baseurl = Readconfig.getbaseurl()
    email = Readconfig.getemail()
    password = Readconfig.getpassword()

    logger = LogGen.loggen()

    def test_HomePage_Title(self, setup):
        self.logger.info("**** start login ******")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(10)
        self.lp = LoginPage(self.driver)
        self.lp.set_email(self.email)
        self.lp.set_password(self.password)
        self.lp.clicklogin()

        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            self.driver.save_screenshot("E:\\nopcommerce\\Screenshots\\home.png")
            assert True
        else:
            self.driver.save_screenshot("E:\\nopcommerce\\Screenshots\\home.png")
            assert False

        self.logger.info("home page test completed")


























