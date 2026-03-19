import time

import pytest

from pages.dashboard_page import DashboardPage

def test_navigation_toggle(login):

    dashboard_page = DashboardPage(login)

    dashboard_page.click_operators()
    dashboard_page.click_three_lines()
    dashboard_page.click_platforms()
    time.sleep(2)
    dashboard_page.click_three_lines()
    dashboard_page.click_token()
    time.sleep(2)
    dashboard_page.click_three_lines()
    dashboard_page.click_devices()
    time.sleep(2)