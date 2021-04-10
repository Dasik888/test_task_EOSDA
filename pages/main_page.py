import email
import imaplib
import re
import time
from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def should_be_login_in_link(self):
        self.is_link_correct("login")

    def should_be_auth_in_link(self):
        self.is_link_correct("auth")

    def fill_first_name_in_sign_up_form(self):
        self.browser.find_element(*MainPageLocators.FIRST_NAME_FIELD).send_keys("user_name")

    def fill_last_name_in_sign_up_form(self):
        self.browser.find_element(*MainPageLocators.LAST_NAME_FIELD).send_keys("user_last_name")

    def fill_email_in_form(self, login):
        self.browser.find_element(*MainPageLocators.EMAIL_FIELD).send_keys(login)

    def fill_password_in_form(self, password):
        self.browser.find_element(*MainPageLocators.PASSWORD_FIELD).send_keys(password)

    def choose_pp_checkbox_in_sign_up_form(self):
        self.browser.find_element(*MainPageLocators.PP_CHECKBOX).click()

    def click_sign_up_button(self):
        self.click_if_element_present(*MainPageLocators.SIGN_UP_BTN)

    def go_to_login_form(self):
        self.browser.find_element(*MainPageLocators.LOGIN_FORM_BTN).click()

    def click_login_button(self):
        self.click_if_element_present(*MainPageLocators.LOGIN_BTN)

    def get_code(self):
        time.sleep(60)
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login('vasyadasha328@gmail.com', 'Pp123456')
        mail.list()
        mail.select("inbox")
        result, data = mail.search(None, "ALL")
        ids = data[0]
        id_list = ids.split()
        latest_email_id = id_list[-1]
        result, data = mail.fetch(latest_email_id, "(RFC822)")
        raw_email = data[0][1].decode('utf-8')
        email_message = email.message_from_string(raw_email)
        for payload in email_message.get_payload():
            body = payload.get_payload(decode=True).decode('utf-8')
            code = re.findall(
                r'Вы можете использовать приведенный ниже код подтверждения, чтобы завершить регистрацию. '
                r'Просто скопируйте и вставьте его на страницу завершения регистрации.\s*(\d{2}-\d{2})', body)
            return code



