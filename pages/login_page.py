from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class LoginPage(BasePage):

    LOGIN = (By.XPATH, '//*[@id="navbarToggler"]/ul/li[3]/button')
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    SIGN_IN = (By.ID, 'kc-login')

    def open(self):
        self.driver.get("https://ntcstage.cdot.in/")

    def login(self, username, password):
        self.click(self.LOGIN)
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.SIGN_IN)



