from .base_page import BasePage
from .locators import MainPageLocators


class AccountPage(BasePage):
    def should_be_fields_in_link(self):
        self.is_link_correct("fields")