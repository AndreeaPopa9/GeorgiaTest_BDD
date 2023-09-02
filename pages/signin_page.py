from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import base_page

class Signin_page(base_page.BasePage):

    email_address = "andreeapopa9793@gmail.com"
    password = "TestingPass9%"
    EMAIL_FIELD = (By.ID, "emailcustomer[email]")
    PASSWORD_FIELD = (By.ID, "passwordcustomer[password]")
    SIGNIN_BTN = (By.XPATH, "//div[@class='mt-1']/button")
    ERROR_MSG = (By.CSS_SELECTOR, "p.text-sm.text-center")


    def open_signin_page(self):
        self.chrome.get("https://www.luluandgeorgia.com/account/login")

    def enter_email(self, email_address):
        self.chrome.find_element(*self.EMAIL_FIELD).send_keys(email_address)

    def enter_password(self, password):
        self.chrome.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_signin_btn(self):
        element = self.chrome.find_element(*self.SIGNIN_BTN)
        self.chrome.execute_script("arguments[0].click();", element)

    def check_my_account_page(self):
        self.check_page_url("/account")

    def signin(self):
        self.open_signin_page()
        self.enter_email(self.email_address)
        self.enter_password(self.password)
        self.click_signin_btn()

    def check_signin_error_message(self, expected_result):
        error_message = "error: the failed login message is not displayed"
        WebDriverWait(self.chrome, 10).until(EC.visibility_of_element_located(self.ERROR_MSG))
        self.check_error_message(self.ERROR_MSG, expected_result, error_message)








