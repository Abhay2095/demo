import random
import string
import time

import pytest
from selenium.webdriver.common.by import By

from Utilities.ReadProperties import Readconfig
from Utilities.customlogger import LogGen
from PageObject.LoginPage import LoginPage
from PageObject.Add_New_Customer import Add_New_Customer


class Test_add_new_customer:
    baseurl = Readconfig.getbaseurl()
    email = Readconfig.getemail()
    password = Readconfig.getpassword()
    Password = Readconfig.getPassword()
    fname = Readconfig.getfname()
    lname = Readconfig.getlname()
    DOB = Readconfig.getDOB()
    cname = Readconfig.getcname()
    content = Readconfig.getcontent()

    logger = LogGen.loggen()

    def test_add_customer(self, setup):
        self.logger.info("**** start login ******")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.lp = LoginPage(self.driver)
        self.lp.set_email(self.email)
        self.lp.set_password(self.password)
        self.lp.clicklogin()

        time.sleep(3)
        self.ac = Add_New_Customer(self.driver)
        self.ac.clickcustomers()
        time.sleep(3)
        self.ac.clickcustmenu()
        self.ac.click_addnew()
        self.ac.setemail('abhay@gmail.com')
        self.ac.setpassword(self.Password)
        self.ac.setfname(self.fname)
        self.ac.setlname(self.lname)
        self.ac.setgender('Male')
        self.ac.setdob(self.DOB)
        self.ac.setcompanyname(self.cname)
        self.ac.set_customerrole('Guests')
        self.ac.setmngofvendor('Vendor 2')
        self.ac.setadminContent(self.content)
        self.ac.clickonsave()

        self.msg = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissable']").text

        if 'The new customer has been added successfully.' in self.msg:
            assert True == True

        else:
            assert True == False


























































