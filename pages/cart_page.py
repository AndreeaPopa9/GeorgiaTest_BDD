from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base_page import BasePage


class Cart_page(BasePage):
    CART_BTN = (By.CSS_SELECTOR,
                "a[class='nav-aux__item pr-0 flex items-center text-xs cart-drawer-toggle js-cart-drawer-toggle relative']")
    ITEMS_NUMBER_IN_CART = (By.CSS_SELECTOR,
                            "span[class='ml-1 js-cart-count cart-count leading-none absolute flex justify-center items-center w-3 h-3 rounded-full bg-black text-white']")
    ITEM_IN_CART = (By.CSS_SELECTOR, "h3[class='body-1 capitalize']")
    SUCCESS_MSG = (By.CSS_SELECTOR, "h2[class='body-large normal-case mb-4']")
    ITEMS_SUBTOTAL = (By.XPATH, "//*[@id='cart']/div/div/div/div[2]/div[2]")

    def enter_cart_page(self):
        element = self.chrome.find_element(*self.CART_BTN)
        self.chrome.execute_script("arguments[0].click();", element)

    def check_number_items_in_cart(self, items_in_cart):
        no_items = self.chrome.find_element(*self.ITEMS_NUMBER_IN_CART).text
        assert no_items == items_in_cart, f"Fail: There are more than one items in cart."

    def remove_item_from_cart(self, item):
        element = self.chrome.find_element(By.XPATH,
                                           f"//*[contains(text(), '{item}')]/parent::h3/parent::td/following-sibling::td/following-sibling::td/following-sibling::td/a/div/div/button")
        self.chrome.execute_script("arguments[0].click();", element)

    def check_item_in_cart(self, item):
        try:
            EC.presence_of_element_located((By.CSS_SELECTOR, f"a[data-gtmevlabel='{item}']"))
        except:
            assert False, f"Fail: The item {item} was not displayed in cart."

    def check_successful_message(self, expected_result):
        actual_result = self.chrome.find_element(*self.SUCCESS_MSG).text
        assert actual_result == expected_result, f"Error: The item was not removed from the cart"

    def verify_total_price(self, *items, items_prices):
        actual_result = float(self.chrome.find_element(*self.ITEMS_SUBTOTAL).text.replace("$", "").replace(",", ""))
        expected_result = 0
        for i in items:
            if i in items_prices.keys():
                expected_result += items_prices[i]
        assert actual_result == expected_result, f"Total price mismatch. Expected: {expected_result}, Actual: {actual_result}"
