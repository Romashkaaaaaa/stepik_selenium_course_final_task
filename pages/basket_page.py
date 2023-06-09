from .locators import BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage): 
    def should_be_text_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_EMPTY_BASKET), "Text about the empty basket is not presented"
        
    def should_not_be_items_in_busket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Items in the basket is presented, but should not be"
#Пустая строчка снизу