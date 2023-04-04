import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

login_link = "http://selenium1py.pythonanywhere.com/accounts/login/"
coders_at_work_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
the_city_and_the_stars_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

@pytest.mark.login_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser, login_link)
        login_page.open()
        login_page.register_new_user()
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_item_to_cart()
        product_page.solve_quiz_and_get_code()
        product_page.should_be_successful_addition()
        product_page.should_be_same_cost()

    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, coders_at_work_link)
        product_page.open() 
        product_page.should_not_be_success_message()

@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", 
                                               marks = pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_item_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_successful_addition()
    product_page.should_be_same_cost()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    product_page = ProductPage(browser, coders_at_work_link)
    product_page.open()                   
    product_page.go_to_login_page()  
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_form()      
    login_page.should_be_register_form()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page = ProductPage(browser, coders_at_work_link)
    product_page.open()
    product_page.go_to_basket_page()
    busket_page = BasketPage(browser, browser.current_url)
    busket_page.should_not_be_items_in_busket()
    busket_page.should_be_text_about_empty_basket()

def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, coders_at_work_link)
    product_page.open()
    product_page.should_not_be_success_message()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, coders_at_work_link)
    product_page.open()
    product_page.add_item_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_not_be_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    product_page = ProductPage(browser, the_city_and_the_stars_link)
    product_page.open()
    product_page.should_be_login_link()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, coders_at_work_link)
    product_page.open()
    product_page.add_item_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_disappeared_success_message()
#Пустая строчка снизу