from .pages.main_page import MainPage
from .pages.verification_page import VerificationPage


def test_guest_open_main_page(browser):
    url = "https://eos.com/crop-monitoring/"
    page = MainPage(browser, url)
    page.open()
    page.should_be_login_in_link()
    page.fill_first_name_in_sign_up_form()
    page.fill_last_name_in_sign_up_form()
    page.fill_email_in_sign_up_form()
    page.fill_password_in_sign_up_form()
    page.choose_pp_checkbox_in_sign_up_form()
    page.click_sign_up_button()
    code = page.get_code()
    temp_page = VerificationPage(browser, url)
    temp_page.should_be_confirm_in_link()
    temp_page.fill_confirm_code(code)
    temp_page.should_be_fields_in_link()





