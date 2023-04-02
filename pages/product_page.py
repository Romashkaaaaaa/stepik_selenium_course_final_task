from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage): 
    def add_item_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_CART), "Button 'add to cart' is not presented"
        button_add = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART)
        button_add.click()

    def should_be_successful_addition(self):
        item_name_alert = self.get_element_text(*ProductPageLocators.ITEM_NAME_ALERT)
        item_name = self.get_element_text(*ProductPageLocators.ITEM_NAME)
        
        assert item_name_alert, "Item name alert is not presented"
        assert item_name, "Item name is not presented"
        assert item_name_alert == item_name, "Item name and item name alert are not the same"

    def should_be_same_cost(self):
        item_price_alert = self.get_element_text(*ProductPageLocators.ITEM_PRICE_ALERT)
        item_price = self.get_element_text(*ProductPageLocators.ITEM_PRICE)
        
        assert item_price_alert, "Item price alert is not presented"
        assert item_price, "Item price is not presented"
        assert item_price_alert == item_price, "Item price and item price alert are not the same"
#Пустая строчка снизу