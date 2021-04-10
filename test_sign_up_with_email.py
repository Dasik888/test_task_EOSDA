from .pages.main_page import MainPage
from .pages.verification_page import VerificationPage
from .pages.account_page import AccountPage


def test_guest_can_sign_up_with_email(browser):
    url = "https://eos.com/crop-monitoring/"
    login = "vasyadasha328+11@gmail.com"
    password = "Pp123456"
    page = MainPage(browser, url)
    page.open()
    page.should_be_login_in_link()
    page.fill_first_name_in_sign_up_form()
    page.fill_last_name_in_sign_up_form()
    page.fill_email_in_form(login)
    page.fill_password_in_form(password)
    page.choose_pp_checkbox_in_sign_up_form()
    page.click_sign_up_button()
    code = page.get_code()
    temp_page = VerificationPage(browser, url)
    temp_page.should_be_confirm_in_link()
    temp_page.fill_confirm_code(code)
    acc_page = AccountPage(browser, url)
    acc_page.should_be_fields_in_link()





