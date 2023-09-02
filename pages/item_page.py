from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from base_page import BasePage


class Item_page(BasePage):
    SEARCH_FIELD = (By.XPATH, "//*[@placeholder='Search for rugs, furniture, and more']")
    SEARCH_BTN = (By.XPATH, "//a[@id='ss-search-toggle']/div")
    SEARCH_BTN2= (By.XPATH, "//button[@aria-label='Search']")
    SEARCHED_ITEM = (By.CSS_SELECTOR, "div[class='product-card__slider ss-slider ss-slider-right'] a")
    ADD_TO_CART_BTN = (By.XPATH, "//button[contains(text(),'Add to Cart')]")
    ITEM_PRICE = (By.XPATH, "//*[@id='searchspring-content']/section/div/div/article[1]/p/span/span")
    FILTER_ON_PAGE = (By.XPATH, "//div[@class='ss-list-option font-josefin ng-scope']")


    def open_main_page(self):
        self.chrome.get("https://www.luluandgeorgia.com/")

    def search_for_item(self, item):
        el1 = self.chrome.find_element(*self.SEARCH_BTN)
        self.chrome.execute_script("arguments[0].click();", el1)
        sleep(2)
        self.chrome.find_element(*self.SEARCH_FIELD).send_keys(item)
        el2 = self.chrome.find_element(*self.SEARCH_BTN2)
        self.chrome.execute_script("arguments[0].click();", el2)

    def add_item_to_cart(self):
        element = self.chrome.find_element(*self.SEARCHED_ITEM)
        self.chrome.execute_script("arguments[0].click();", element)
        WebDriverWait(self.chrome, 10).until(EC.visibility_of_element_located(self.ADD_TO_CART_BTN))
        element_1 = self.chrome.find_element(*self.ADD_TO_CART_BTN)
        self.chrome.execute_script("arguments[0].click();", element_1)

    def get_item_price(self):
        return float(self.chrome.find_element(*self.ITEM_PRICE).text.replace("$", "").replace(",", ""))

    def filter_items(self, filter):
        element = self.chrome.find_element(By.XPATH, f"//div/a[contains(text(),'{filter}')]")
        self.chrome.execute_script("arguments[0].click();", element)

    def verify_filter_on_page(self, expected_result):
        filters = []
        filter_elem = self.chrome.find_elements(*self.FILTER_ON_PAGE)
        for i in range(0, len(filter_elem)):
            filters.append(filter_elem[i].text)
        assert expected_result in filters, f"Error: The filter is not selected as {expected_result}"
