from playwright.sync_api import sync_playwright


class BrowserFactory:

    @staticmethod
    def launch_browser(headless=True):

        playwright = sync_playwright().start()

        browser = playwright.chromium.launch(
            headless=headless
        )

        page = browser.new_page(
            viewport={
                "width": 1920,
                "height": 1080
            }
        )

        return playwright, browser, page