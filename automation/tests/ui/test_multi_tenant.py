from automation.pages.login_page import LoginPage

from automation.pages.projects_page import ProjectsPage

from automation.config.config_reader import ConfigReader


config = ConfigReader.load_config()


def test_company2_projects(page):

    login = LoginPage(page)

    projects = ProjectsPage(page)

    page.goto(
        config["application"]["base_url"]
        + "/login"
    )

    login.login(

        "user@company2.com",

        "password123"

    )

    login.verify_login_success()

    projects.verify_tenant("Company2")