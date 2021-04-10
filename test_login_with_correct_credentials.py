from .pages.main_page import MainPage
from .pages.account_page import AccountPage


def test_user_can_login(browser):
    url = "https://eos.com/crop-monitoring/"
    login = "vasyadasha328+10@gmail.com"
    password = "Pp123456"
    page = MainPage(browser, url)
    page.open()
    page.should_be_login_in_link()
    page.go_to_login_form()
    page.should_be_auth_in_link()
    page.fill_email_in_form(login)
    page.fill_password_in_form(password)
    page.click_login_button()
    acc_page = AccountPage(browser, url)
    acc_page.should_be_fields_in_link()

