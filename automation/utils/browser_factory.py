from playwright.sync_api import sync_playwright
from automation.config.config_reader import ConfigReader


class BrowserFactory:

    @staticmethod
    def launch_browser():

        config = ConfigReader.load_config()

        browser_name = config["browser"]["name"]

        headless = config["browser"]["headless"]

        playwright = sync_playwright().start()

        if browser_name == "chromium":
            browser = playwright.chromium.launch(headless=headless)

        elif browser_name == "firefox":
            browser = playwright.firefox.launch(headless=headless)

        elif browser_name == "webkit":
            browser = playwright.webkit.launch(headless=headless)

        else:
            raise Exception("Unsupported browser")

        page = browser.new_page(
            viewport=config["browser"]["viewport"]
        )

        return playwright, browser, page