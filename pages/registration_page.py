from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base_page import BasePage


class Registration_page(BasePage):
    FIRST_NAME_FIELD = (By.ID, "122926")
    LAST_NAME_FIELD = (By.ID, "723706")
    EMAIL_ADDRESS_FIELD = (By.ID, "218148")
    PASSWORD_FIELD = (By.XPATH, '//input[@autocomplete="new-password"]')
    SUBSCRIPTION_BTN = (By.ID, "287410")
    CREATE_ACCOUNT_BTN = (By.XPATH, "//button[@class='cf-submit-form cf-button btn button']")
    ERROR_MSG = (By.XPATH, "//ul[@class='cf-form-errors']/div/li")

    def open_registration_page(self):
        self.chrome.get("https://www.luluandgeorgia.com/account/login")

    def input_firstname(self, firstname):
        self.chrome.find_element(*self.FIRST_NAME_FIELD).send_keys(firstname)

    def input_lastname(self, lastname):
        self.chrome.find_element(*self.LAST_NAME_FIELD).send_keys(lastname)

    def input_email(self, email):
        self.chrome.find_element(*self.EMAIL_ADDRESS_FIELD).send_keys(email)

    def input_password(self, password):
        pass_field = self.chrome.find_elements(*self.PASSWORD_FIELD)
        for i in range(0, len(pass_field)):
            pass_field[i].send_keys(password)

    def deselect_subscription(self):
        checkbox = self.chrome.find_element(*self.SUBSCRIPTION_BTN)
        self.chrome.execute_script("arguments[0].click();", checkbox)

    def click_create_account_btn(self):
        element = self.chrome.find_element(*self.CREATE_ACCOUNT_BTN)
        self.chrome.execute_script("arguments[0].click();", element)

    def check_registration_error_message(self, expected_result):
        error_message = f"Error: Message is not as expected {expected_result}"
        WebDriverWait(self.chrome, 10).until(EC.visibility_of_element_located(self.ERROR_MSG))
        self.check_error_message(self.ERROR_MSG, expected_result, error_message)



