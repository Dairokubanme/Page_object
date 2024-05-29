from .locators import MainPageLocators
from .locators import ProductPageLocators
from .login_page import LoginPage
from .product_page import ProductPage
from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(LoginPage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def check_locator_go_to_login(self):
        self.should_be_login_link()

    def check_go_to_login(self):
        link_smoke = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link_smoke.click()

    def check_login_in_url(self):
        link_smoke = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link_smoke.click()
        self.should_be_login_url()

    def check_login_form(self):
        link_smoke = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link_smoke.click()
        self.should_be_login_form()

    def check_register_form(self):
        link_smoke = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link_smoke.click()
        self.should_be_register_form()

    def check_all_asserts(self):
        self.should_be_login_link()
        link_smoke = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link_smoke.click()
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def open_basket(self):
        link = self.browser.find_element(*ProductPageLocators.check_basket)
        link.click()
        self.basket_is_empty()

class MainPage2(ProductPage):
    def check_open_basket(self):
        link = self.browser.find_element(*ProductPageLocators.button_add_to_basket)
        link.click()

    def check_basket(self):
        self.should_be_basket()
        link = self.browser.find_element(*ProductPageLocators.button_add_to_basket)
        link.click()
        self.solve_quiz_and_get_code()
        self.should_be_message_about_adding()
        self.should_be_message_basket_total()
