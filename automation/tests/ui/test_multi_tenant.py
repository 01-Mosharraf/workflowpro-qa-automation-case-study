import pytest
from automation.config.config_reader import ConfigReader

config = ConfigReader.load_config()

if config.get("framework", {}).get("demo_mode", False):
    pytest.skip(
        "WorkflowPro is a fictional application. UI execution is intentionally skipped.",
        allow_module_level=True
    )

from automation.pages.login_page import LoginPage
from automation.pages.projects_page import ProjectsPage
from automation.utils.test_data_manager import TestDataManager
from automation.config.config_reader import ConfigReader

config = ConfigReader.load_config()

users = TestDataManager.load("users.json")


def test_company2_access(page):

    login = LoginPage(page)

    projects = ProjectsPage(page)

    page.goto(
        config["application"]["base_url"] + "/login"
    )

    user = users["company2_user"]

    login.login(
        user["email"],
        user["password"]
    )

    login.verify_login_success()

    projects.verify_tenant("Company2")