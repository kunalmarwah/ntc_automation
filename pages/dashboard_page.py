from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class DashboardPage(BasePage):
    PAGE_TITLE = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div[1]/h2')
    COMPANY_NAME = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div[1]/div/div[1]')
    OPERATOR_COUNT = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div/div[1]/div/h4')
    PLATFORMS_COUNT = (
    By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div/div[2]/div/h4')
    DEVICES_COUNT = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div/div[3]/div/h4')
    CERTIFIED_COUNT = (
    By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div/div[4]/div/h4')

    SIDEBAR_TOGGLE = (By.XPATH, '//*[@id="root"]/div/div/div[1]/div[2]/div/button')
    SIDE_THREE_LINES = (By.XPATH, '//*[@id="root"]/div/div/div[1]/div/button')

    OPERATOR_NAVIGATION = (
    By.XPATH, '//*[@id="root"]/div/div/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div/div[2]/nav/a[2]')
    PLATFORMS_NAVIGATION = (
    By.XPATH, '//*[@id="root"]/div/div/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div/div[2]/nav/a[3]')
    TOKEN_MANAGEMENT = (
    By.XPATH, '//*[@id="root"]/div/div/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div/div[2]/nav/a[4]')
    DEVICES_NAVIGATION = (
    By.XPATH, '//*[@id="root"]/div/div/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div/div[2]/nav/a[5]')

    def get_dashboard_title(self):
        return self.get_text(self.PAGE_TITLE)

    def get_company_name(self):
        return self.get_text(self.COMPANY_NAME)

    def get_operator_count(self):
        return self.get_text(self.OPERATOR_COUNT)

    def get_platforms_count(self):
        return self.get_text(self.OPERATOR_COUNT)

    def get_devices_count(self):
        return self.get_text(self.DEVICES_COUNT)

    def get_certified_count(self):
        return self.get_text(self.CERTIFIED_COUNT)

    def click_side_arrow(self):
        return self.click(self.SIDEBAR_TOGGLE)

    def click_three_lines(self):
        return self.click(self.SIDE_THREE_LINES)

    def click_operators(self):
        self.click(self.OPERATOR_NAVIGATION)

    def click_platforms(self):
        self.click(self.PLATFORMS_NAVIGATION)

    def click_token(self):
        self.click(self.TOKEN_MANAGEMENT)

    def click_devices(self):
        self.click(self.DEVICES_NAVIGATION)






























