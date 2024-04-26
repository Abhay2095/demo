import time

import pytest
from selenium import webdriver
from Utilities.ReadProperties import Readconfig
from PageObject.LoginPage import LoginPage
from Utilities.customlogger import LogGen
from PageObject.Add_New_Customer import Add_New_Customer
from PageObject.SearchCustomer import SearchCustomer

class Test_searchcustomerbymail:
    baseurl = Readconfig.getbaseurl()
    email = Readconfig.getemail()
    password = Readconfig.getpassword()

    logger = LogGen.loggen()

    def test_searchcustomerbymail(self,setup):
        self.logger.info("**** start login ******")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.lp = LoginPage(self.driver)
        self.lp.set_email(self.email)
        self.lp.set_password(self.password)
        self.lp.clicklogin()

        time.sleep(3)
        self.ac = Add_New_Customer(self.driver)
        self.ac.clickcustomers()
        time.sleep(3)
        self.ac.clickcustmenu()
        time.sleep(3)

        self.sc = SearchCustomer(self.driver)
        self.sc.setEmail('kiyjcycyhjc676008@gmail.com')
        time.sleep(5)
        self.sc.clicksearchbtn()
        time.sleep(3)
        status = self.sc.searchcustomerbymail('kiyjcycyhjc676008@gmail.com')
        assert True == status











































