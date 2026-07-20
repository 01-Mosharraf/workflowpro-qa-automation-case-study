from playwright.sync_api import expect
from automation.pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL_INPUT = "#email"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-btn"
    WELCOME_MESSAGE = ".welcome-message"

    def login(self, email, password):

        self.fill(self.EMAIL_INPUT, email)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def verify_login_success(self):

        self.page.wait_for_url("**/dashboard")

        expect(
            self.page.locator(self.WELCOME_MESSAGE)
        ).to_be_visible()