import time

import pytest

from pages.dashboard_page import DashboardPage
from pages.operators_page import OperatorsPage
@pytest.mark.smoke
def test_operators_module(login):

    operators_nav_mod = DashboardPage(login)
    ope_nav_mod = OperatorsPage(login)

    operators_nav_mod.click_operators()

    ope_nav_mod.click_create_operators()
    ope_nav_mod.username_type()
    ope_nav_mod.email_address_type()
    ope_nav_mod.first_name_type()
    ope_nav_mod.last_name_type()
    ope_nav_mod.designation_type()
    ope_nav_mod.phone_number_type()
    ope_nav_mod.password_type()
    ope_nav_mod.repeat_password_type()
    ope_nav_mod.create_button_click()
    time.sleep(5)

