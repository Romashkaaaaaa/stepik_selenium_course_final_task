from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUTTON_ADD_TO_CART = (By.CLASS_NAME, "btn-add-to-basket")
    ITEM_NAME_ALERT = (By.CSS_SELECTOR, ".alert-noicon:nth-child(1) strong")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ITEM_PRICE_ALERT = (By.CSS_SELECTOR, ".alert-noicon:nth-child(3) strong")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
#Пустая строчка внизу