import pytest
from selenium import webdriver

@pytest.fixture(scope='function")
def browser():
    print('\nstarting browser')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    yield browser
    print('\nquiting browser')
    browser.quit()