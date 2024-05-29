from .base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from .locators import LoginPageLocators
from .locators import ProductPageLocators
from selenium.common.exceptions import NoSuchElementException
import pytest
import time
import math


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_basket()
        self.should_be_message_about_adding()
        self.should_be_message_basket_total()


    def should_be_basket(self):
        assert self.browser.find_element(*ProductPageLocators.button_add_to_basket), "Basket missing"

    def should_be_message_about_adding(self):
        assert self.is_element_present(*ProductPageLocators.product_name), "Product name is not presented"
        assert self.is_element_present(*ProductPageLocators.product_name_in_message), "Message invalid"
        product_name = self.browser.find_element(*ProductPageLocators.product_name).text
        product_name_in_message = self.browser.find_element(*ProductPageLocators.product_name_in_message).text
        assert product_name == product_name_in_message, "Product name otlichaetsya"


    def should_be_message_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.message_basket_total), "Message basket total invalid"
        assert self.is_element_present(*ProductPageLocators.product_price), "Product price invalid"
        message_basket_total = self.browser.find_element(*ProductPageLocators.message_basket_total).text
        product_price = self.browser.find_element(*ProductPageLocators.product_price).text
        assert product_price in message_basket_total, "No price in message"

    def should_not_be_success_massage(self):
        assert self.is_not_element_present(*ProductPageLocators.success_message), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.success_message), \
            "Success meassage did not disappear, although it should have been"
