from browser import Browser
class BasePage(Browser):

    def check_error_message(self, locator, expected_result, message_fail):
        actual_result = self.chrome.find_element(*locator).text
        assert actual_result == expected_result, message_fail

    def check_page_url(self, partial_url):
        actual_url = self.chrome.current_url
        assert partial_url in actual_url, "ERROR: Page url is not correct. Please check your data"


