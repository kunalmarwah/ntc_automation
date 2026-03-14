from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class DashboardPage(BasePage):

    PAGE_TITLE = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div[1]/h2')
    COMPANY_NAME = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div[1]/div/div[1]')
    OPERATOR_COUNT = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div/div[1]/div/h4')
    PLATFORMS_COUNT = (By. XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div/div[2]/div/h4')
    DEVICES_COUNT = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div/div[3]/div/h4')
    CERTIFIED_COUNT = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div/div[4]/div/h4')

    def get_dashboard_title(self):
        return self.get_text(self.PAGE_TITLE)

    def ger_company_name(self):
        return self.get_text(self.COMPANY_NAME)

    def get_operator_count(self):
        return self.get_text(self.OPERATOR_COUNT)

    def get_platforms_count(self):
        return self.get_text(self.OPERATOR_COUNT)

    def get_devices_count(self):
        return self.get_text(self.DEVICES_COUNT)

    def get_certified_count(self):
        return self.get_text(self.CERTIFIED_COUNT)


