from pages.dashboard_page import DashboardPage

def  test_dashboard(login):

    dashboard_page = DashboardPage(login)

    title = dashboard_page.get_dashboard_title()
    company_name = dashboard_page.ger_company_name()

    assert "Service Provider" in title
    assert "Welcome Group10 pvt ltd 🙏" in company_name