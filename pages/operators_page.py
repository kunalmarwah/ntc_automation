import time

from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class OperatorsPage(BasePage):

    Click_create_operator = (By.XPATH, "//button[normalize-space()='Create Operators']")
    username = (By.XPATH, " //input[@id='username']")
    email_address = (By.XPATH, "//input[@id='email']")
    first_name = (By.XPATH, "//input[@id='firstName']")
    last_name = (By.XPATH, "//input[@id='lastName']")
    designation = (By.XPATH, "//input[@id='designation']")
    phone_number = (By.XPATH, "//input[@id='phoneNumber']")
    password = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[1]/div[7]/div[1]/div[1]/div[1]/div[1]/input[1]")
    repeat_password = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/div[1]/div[8]/div[1]/div[1]/input[1]")
    create_button = (By.XPATH, "//button[normalize-space()='Create']")

    actions_button  = (By.XPATH, "//tbody/tr[1]/td[8]/button[1]//*[name()='svg']")
    edit_button = (By.XPATH, "//li[normalize-space()='Edit']")


    def click_create_operators(self):
        return self.click(self.Click_create_operator)

    def username_type(self, value):
        return self.type(self.username, value)

    def email_address_type(self, value):
        return self.type(self.email_address, value)

    def first_name_type(self, value):
        return self.type(self.first_name, value)

    def last_name_type(self, value):
        return self.type(self.last_name, value)

    def designation_type(self, value):
        return self.type(self.designation, value)

    def phone_number_type(self, value):
        return self.type(self.phone_number, value)

    def password_type(self, value):
        return self.type(self.password, value)

    def repeat_password_type(self, value):
        return self.type(self.repeat_password, value)

    def create_button_click(self):
        return self.click(self.create_button)

    def click_actions_button(self):
        return self.click(self.actions_button)

    def click_edit_button(self):
        return self.click(self.edit_button)

    def fill_operators_form(self, data):
        self.username_type(data["username"])
        self.email_address_type(data["email"])
        self.first_name_type(data["first_name"])
        self.last_name_type(data["last_name"])
        self.designation_type(data["designation"])
        self.phone_number_type(data["phone"])
        self.password_type(data["password"])
        self.repeat_password_type(data["password"])
