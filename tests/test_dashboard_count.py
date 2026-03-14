from pages.dashboard_page import DashboardPage

def test_dashboard_count(login):

    dashboard_count = DashboardPage(login)

    operator = dashboard_count.get_operator_count()
    platforms = dashboard_count.get_platforms_count()
    devices_count = dashboard_count.get_devices_count()
    certified_count = dashboard_count.get_certified_count()

    assert int(operator) >= 0
    assert int(platforms) >= 0
    assert int(devices_count) >= 0
    assert int(certified_count) >= 0
