from .base_page import BasePage
from .locators import ProductLocators
from selenium.webdriver.common.by import By



class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_correct_url()
        self.should_be_add_to_cart()
        self.press_add_to_cart()

    def add_correct_product(self):
        self.name_matches()
        self.price_matches()




    def should_be_correct_url(self):
# проверка на корректный url адрес
        assert "?promo=offer" in self.browser.current_url, "url не совпадает"


    def should_be_add_to_cart(self):
#проверка наличия кнопки "Добавить в карзину"
        assert self.is_element_present(*ProductLocators.BOTTON_ADD), "The 'add to cart' button is not represented"


    def press_add_to_cart(self):
#нажатие кнопки "Добавить в карзину"
        button_add_to_cart = self.browser.find_element(*ProductLocators.BOTTON_ADD)
        button_add_to_cart.click()



    def name_matches(self):
# Название товара совпадает
        name_to_cart = self.browser.find_element(By.CSS_SELECTOR, "#messages strong").text
        name_book = self.browser.find_element(*ProductLocators.NAME_PRODUCT).text
        assert name_to_cart == name_book, "Название товара не совпадает"


    def price_matches(self):
# Цена товара совпадает
        price_to_cart = self.browser.find_element(By.CSS_SELECTOR, ".alert-info strong")
        price_book = self.browser.find_element(*ProductLocators.PRICE_PRODUCT)
        assert price_to_cart.text == price_book.text, "Цена товара не совпадает"
