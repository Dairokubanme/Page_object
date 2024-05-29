from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators
from .locators import ProductPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_link()
        self.should_be_login_form()
        self.should_be_register_form()
        self.basket_is_empty()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert "login" in url, "URL incorrect"

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link incorrect"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form incorrect"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.RESISTER_FORM), "Register form incorrect"

    def basket_is_empty(self):
        assert self.is_element_present(*ProductPageLocators.basket_is_empty), "Basket not empty"