from selenium.webdriver.common.by import By


class LoginPage:
    text_email_id = "Email"
    text_password_id = "Password"
    btn_login_xpath = "//button[normalize-space()='Log in']"

    def __init__(self, driver):
        self.driver = driver


    def set_email(self, email):
        self.driver.find_element(By.ID, self.text_email_id).clear()
        self.driver.find_element(By.ID, self.text_email_id).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(By.ID, self.text_password_id).clear()
        self.driver.find_element(By.ID, self.text_password_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

































