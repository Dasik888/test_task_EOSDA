
from selenium.webdriver.common.by import By


class MainPageLocators:
    FIRST_NAME_FIELD = (By.ID, "first_name")
    LAST_NAME_FIELD = (By.ID, "last_name")
    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "password")
    PP_CHECKBOX = (By.ID, "policy_confirm")
    SIGN_UP_BTN = (By.CSS_SELECTOR, ".primary.ui-button")
    LOGIN_FORM_BTN = (By.XPATH, "//ui-login-flow-btn-group/div[2]")
    LOGIN_BTN = (By.CSS_SELECTOR, ".submit-btn.primary.ui-button")


class VerificationPageLocators:
    CONFIRM_CODE_FIELD = (By.ID, "confirm-code-input")


