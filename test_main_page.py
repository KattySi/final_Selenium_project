# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



# def pytest_addoption(parser):
#     # parser.addoption('--browser_name', action='store', default='chrome',
#     #                  help="Choose browser: chrome or firefox")
#     parser.addoption('--language', action='store', default='en',
#                      help="Choose language: ru, en, es, ... (default - en)")



# @pytest.fixture(scope="function")
# def browser(request):
#     user_language = request.config.getoption("language")
#     options = Options()
#     options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
#     browser = webdriver.Chrome(options=options)
#     yield browser
#     browser.quit()



def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()
    print("okay")
