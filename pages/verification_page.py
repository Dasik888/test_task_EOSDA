from .base_page import BasePage
from .locators import VerificationPageLocators


class VerificationPage(BasePage):
    def should_be_confirm_in_link(self):
        self.is_link_correct("confirm")

    def fill_confirm_code(self, code):
        self.browser.find_element(*VerificationPageLocators.CONFIRM_CODE_FIELD).send_keys(code)
