from automation.pages.login_page import LoginPage

from automation.config.config_reader import ConfigReader


config = ConfigReader.load_config()


def test_login(page):

    login = LoginPage(page)

    page.goto(
        config["application"]["base_url"]
        + "/login"
    )

    login.login(

        "admin@company1.com",

        "password123"

    )

    login.verify_login_success()