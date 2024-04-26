import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Add_New_Customer:

    text_customers_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    text_customer_menu_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btn_add_new_xpath = "//a[normalize-space()='Add new']"
    text_Email_xpath = "//input[@id='Email']"
    text_Password_xpath = "//input[@id='Password']"
    text_fname_xpath = "//input[@id='FirstName']"
    text_lname_xpath = "//input[@id='LastName']"
    btn_gen_male_xpath = "//input[@id='Gender_Male']"
    btn_gen_female_xpath = "//input[@id='Gender_Female']"
    text_dob_xpath = "//input[@id='DateOfBirth']"
    text_companyname_xpath = "//input[@id='Company']"
    text_customer_role_xpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    lstitem_administrator_xpath = "//li[contains(text(),'Administrators')]"
    lstitem_guest_xpath = "//li[contains(text(),'Guests')]"
    lstitem_registered_xpath = "//li[contains(text(),'Registered')]"
    lstitem_vendor_xpath = "//li[contains(text(),'Vendors')]"
    drp_mgrofvendor_xpath = "//select[@id='VendorId']"
    text_admin_content = "//textarea[@id='AdminComment']"
    btn_save_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickcustomers(self):
        self.driver.find_element(By.XPATH, self.text_customers_xpath).click()

    def clickcustmenu(self):
        self.driver.find_element(By.XPATH, self.text_customer_menu_xpath).click()

    def click_addnew(self):
        self.driver.find_element(By.XPATH, self.btn_add_new_xpath).click()

    def setemail(self, Email):
        self.driver.find_element(By.XPATH, self.text_Email_xpath).send_keys(Email)

    def setpassword(self, Password):
        self.driver.find_element(By.XPATH, self.text_Password_xpath).send_keys(Password)

    def setfname(self, fname):
        self.driver.find_element(By.XPATH, self.text_fname_xpath).send_keys(fname)

    def setlname(self, lname):
        self.driver.find_element(By.XPATH, self.text_lname_xpath).send_keys(lname)

    def setgender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH, self.btn_gen_male_xpath).click()

        elif gender == "Female":
            self.driver.find_element(By.XPATH, self.btn_gen_female_xpath).click()

        else:
            self.driver.find_element(By.XPATH, self.btn_gen_male_xpath).click()

    def setdob(self, DOB):
        self.driver.find_element(By.XPATH, self.text_dob_xpath).send_keys(DOB)

    def setcompanyname(self, cname):
        self.driver.find_element(By.XPATH, self.text_companyname_xpath).send_keys(cname)

    def set_customerrole(self, role):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.text_customer_role_xpath).click()

        if role == "Registered":
            self.lst_item = self.driver.find_element(By.XPATH, self.lstitem_registered_xpath)

        elif role == "Administrators":
            self.lst_item = self.driver.find_element(By.XPATH, self.lstitem_administrator_xpath)

        elif role == "Guests":
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.lst_item = self.driver.find_element(By.XPATH, self.lstitem_guest_xpath)

        elif role == "Registered":
            self.lst_item = self.driver.find_element(By.XPATH, self.lstitem_registered_xpath)

        elif role == "Vendors":
            self.lst_item = self.driver.find_element(By.XPATH, self.lstitem_vendor_xpath)

        else:
            self.lst_item = self.driver.find_element(By.XPATH, self.lstitem_guest_xpath)

        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.lst_item)

    def setmngofvendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drp_mgrofvendor_xpath))
        drp.select_by_visible_text(value)

    def setadminContent(self, content):
        self.driver.find_element(By.XPATH, self.text_admin_content).send_keys(content)

    def clickonsave(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()







































