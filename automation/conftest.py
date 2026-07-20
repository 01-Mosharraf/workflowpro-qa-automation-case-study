import pytest

from automation.utils.browser_factory import BrowserFactory


@pytest.fixture(scope="function")

def page():

    playwright, browser, page = BrowserFactory.launch_browser()

    yield page

    browser.close()

    playwright.stop()