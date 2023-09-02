from selenium.webdriver.support.select import Select
from base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class MyAccount_page(BasePage):

    EDIT_BTN = (By.CSS_SELECTOR, "a[class='flex flex-col items-center w-1/6 account-button']")
    MONTH_FIELD = (By.ID, "168584")
    DAY_FIELD = (By.ID, "171280")
    UPDATE_BTN = (By.CSS_SELECTOR, "button[class='cf-submit-form cf-button btn button']")
    BIRTHDAY = (By.XPATH, "//p[@class='body-2']/span")
    LOGOUT = (By.XPATH, "//*[@id='root']/div[1]/div/nav/ul/li[6]/a")


    def click_edit_btn(self):
        element = self.chrome.find_element(*self.EDIT_BTN)
        self.chrome.execute_script("arguments[0].click();", element)

    def select_date_of_birth(self, month, day):
        dropdown_month = Select(self.chrome.find_element(*self.MONTH_FIELD))
        dropdown_month.select_by_visible_text(month)
        dropdown_day = Select(self.chrome.find_element(*self.DAY_FIELD))
        dropdown_day.select_by_visible_text(day)

    def click_update_btn(self):
        self.chrome.find_element(*self.UPDATE_BTN).click()
        WebDriverWait(self.chrome, 20).until(EC.visibility_of_element_located(self.EDIT_BTN))

    def check_updated_birth(self, expected_birthday):
        birthday_text = self.chrome.find_element(*self.BIRTHDAY).text
        assert expected_birthday == birthday_text, f"Fail: The birthday {birthday_text} was not displayed"

    def logout_btn(self):
        element = self.chrome.find_element(*self.LOGOUT)
        self.chrome.execute_script("arguments[0].click();", element)
