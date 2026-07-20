from playwright.sync_api import expect
from automation.pages.base_page import BasePage


class DashboardPage(BasePage):

    DASHBOARD_TITLE = "h1"

    def verify_dashboard_loaded(self):

        expect(
            self.page.locator(self.DASHBOARD_TITLE)
        ).to_be_visible()

    def get_current_url(self):

        return self.page.url