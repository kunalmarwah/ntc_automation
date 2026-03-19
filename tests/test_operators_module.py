import pytest

from pages.dashboard_page import DashboardPage
@pytest.mark.smoke
def test_operators_module(login):

    operators_nav_mod = DashboardPage(login)

    operators_nav_mod.click_operators()

