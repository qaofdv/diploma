from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        #login_url = self.browser.find_element(*LoginPageLocators.LOGIN_URL)
        assert "login" in self.browser.current_url, "URL is not correct"

    def should_be_login_form(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        assert True, "Login form is not present"

    def should_be_register_form(self):
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        assert True, "Register form is not present"