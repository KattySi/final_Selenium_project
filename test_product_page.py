import pytest
from .pages.product_page import ProductPage
from selenium.webdriver.common.by import By
import time



@pytest.mark.parametrize('promo_offer', ["0", "1", "2", "3", "4", "5", "6", pytest.param("bugged_link_7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
# гость может добавить товар в корзину
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    product = ProductPage(browser, link)
    product.open()
    product.should_be_product_page()
    # login_page = LoginPage(browser, browser.current_url)
    product.solve_quiz_and_get_code()
    # time.sleep(10)
    product.add_correct_product()
