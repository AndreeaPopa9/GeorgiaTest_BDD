from selenium import webdriver

class Browser:
    chrome = webdriver.Chrome()
    chrome.maximize_window()
    chrome.get("https://www.luluandgeorgia.com/")
    chrome.implicitly_wait(5)

    def close(self):
        self.chrome.quit()

