from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class Operators_Module(BasePage):

    OPERATOR_NAVIGATION = (By.XPATH, '//*[@id="root"]/div/div/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div/div[2]/nav/a[2]')

    def click_operators(self):
        self.click(self.OPERATOR_NAVIGATION)

