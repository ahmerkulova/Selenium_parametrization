from selenium.webdriver.common.by import By
from time import sleep

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_should_be_available(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    button = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
    assert button, 'No "Add to cart button" was found'
    sleep(5)  # time to check the button name
