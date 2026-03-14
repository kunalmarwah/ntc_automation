import pytest

from pages.login_page import LoginPage
from utils.driver_factory import get_driver

@pytest.fixture
def driver() :
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.mark.smoke
def login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login('bineet_kumar', 'Cdot@123456')

    input("Enter captcha manually and press enter")


