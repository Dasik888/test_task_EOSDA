from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.maximize_window()
        self.browser.implicitly_wait(timeout)

    def click_if_element_present(self, how, what):
        self.browser.set_script_timeout(10)
        btn = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((how, what))
        )
        btn.click()


    def is_link_correct(self, text):
        try:
            WebDriverWait(self.browser, 20).until(
                EC.url_contains(text)
            )
        finally:
            assert text in self.browser.current_url, "Link is incorrect"

    def open(self):
        self.browser.get(self.url)
