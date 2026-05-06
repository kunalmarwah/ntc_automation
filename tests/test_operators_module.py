import time

import pytest

from pages.dashboard_page import DashboardPage
from pages.operators_page import OperatorsPage
from utils.data_loader import load_test_data

test_data = load_test_data("operators.json")

@pytest.mark.smoke
@pytest.mark.parametrize("operators_data", test_data)
def test_operators_module_create_operator(login, operators_data):
    operators_nav_mod = DashboardPage(login)
    ope_nav_mod = OperatorsPage(login)

    operators_nav_mod.click_operators()
    ope_nav_mod.click_create_operators()

    ope_nav_mod.fill_operators_form(operators_data)
    ope_nav_mod.create_button_click()
    time.sleep(5)
@pytest.mark.sanity
def test_edit_operators(login):

    operators_nav_mod = DashboardPage(login)
    ope_nav_mod = OperatorsPage(login)

    operators_nav_mod.click_operators()
    ope_nav_mod.click_actions_button()
    ope_nav_mod.click_edit_button()
    time.sleep(5)
