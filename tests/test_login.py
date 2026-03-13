from pages.login_page import LoginPage

def test_login(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login('bineet_kumar', 'Cdot@123456')
