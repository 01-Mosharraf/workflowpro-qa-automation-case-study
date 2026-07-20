import pytest

from .utils.browser_factory import BrowserFactory


@pytest.fixture

def page():

    playwright, browser, page = BrowserFactory.launch_browser()

    yield page

    browser.close()

    playwright.stop()
    