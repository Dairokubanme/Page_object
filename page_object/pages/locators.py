from  selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    RESISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    button_add_to_basket = (By.CSS_SELECTOR, "button.btn-lg:nth-child(3)")
    product_name_in_message = (By.CSS_SELECTOR, "div.alertinner strong")
    product_name = (By.CSS_SELECTOR,"div.product_main h1")
    message_basket_total = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    product_price = (By.CSS_SELECTOR, ".product_main .price_color")
    success_message = (By.CSS_SELECTOR, "div.alert-success")
    check_basket = (By.XPATH, "//a[text()='Посмотреть корзину']")
    basket_is_empty = (By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/p/a")

