from selenium import webdriver
from selenium.webdriver.common.by import By



class SearchCustomer:

    txt_Email_id = "SearchEmail"
    txt_fname_id = "SearchFirstName"
    txt_lname_id = "SearchLastName"
    btn_search_id = "search-customers"
    table_xpath = "//div[@class='row']//div[@class='col-md-12']"
    tbl_row_xpath = "//table[@id='customers-grid']/tbody/tr"
    tbl_col_xpath = "//table[@id='customers-grid']/tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.txt_Email_id).clear()
        self.driver.find_element(By.ID, self.txt_Email_id).send_keys(email)

    def setfname(self,fname):
        self.driver.find_element(By.ID, self.txt_fname_id).clear()
        self.driver.find_element(By.ID, self.txt_fname_id).send_keys(fname)

    def setlname(self,lname):
        self.driver.find_element(By.ID, self.txt_lname_id).clear()
        self.driver.find_element(By.ID, self.txt_lname_id).send_keys(lname)

    def clicksearchbtn(self):
        self.driver.find_element(By.ID, self.btn_search_id).click()

    def getrownum(self):
        return len(self.driver.find_elements(By.XPATH, self.tbl_row_xpath))

    def getcolnum(self):
        return len(self.driver.find_elements(By.XPATH, self.tbl_col_xpath))

    def searchcustomerbymail(self,email):
        flag = False
        for r in range(1,self.getrownum()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            emailid = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag


    def serachcustomerbyname(self, Name):
        flag = False
        for r in range(1, self.getrownum() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[3]").text
            if name == Name:
                flag = True
                break
            return flag







































