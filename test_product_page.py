from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_item_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_successful_addition()
    product_page.should_be_same_cost()
#Пустая строчка снизу