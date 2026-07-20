from playwright.sync_api import expect


class BasePage:

    def __init__(self, page):

        self.page = page

    def open(self, url):

        self.page.goto(url)

    def click(self, locator):

        self.page.locator(locator).click()

    def fill(self, locator, text):

        self.page.locator(locator).fill(text)

    def wait_for_visible(self, locator):

        expect(
            self.page.locator(locator)
        ).to_be_visible()

    def get_text(self, locator):

        return self.page.locator(locator).text_content()