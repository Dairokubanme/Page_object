from .pages.main_page import MainPage2
from .pages.main_page import MainPage
import pytest
import math


@pytest.mark.parametrize('link', [0,1,2,3,4,5,6,pytest.param(7, marks=pytest.mark.xfail),8,9])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer{link}"
    page = MainPage2(browser, link)
    page.open()
    page.check_basket()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage2(browser, link)
    page.open()
    page.check_basket()
    page.should_not_be_success_massage()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage2(browser, link)
    page.open()
    page.should_not_be_success_massage()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage2(browser, link)
    page.open()
    page.check_basket()
    page.success_message_should_disappear()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser, link)
    page.open()
    page.open_basket()
