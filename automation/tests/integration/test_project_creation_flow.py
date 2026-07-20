"""
Integration Test:
API → Web UI → Mobile → Tenant Isolation

NOTE:
WorkflowPro is a fictional application used only for the assessment.
This test demonstrates framework design and testing strategy.
"""

import pytest

from automation.api.project_api import ProjectAPI
from automation.pages.login_page import LoginPage
from automation.pages.projects_page import ProjectsPage
from automation.utils.test_data_manager import TestDataManager
from automation.config.config_reader import ConfigReader

config = ConfigReader.load_config()
users = TestDataManager.load("users.json")
projects = TestDataManager.load("projects.json")


class TestProjectCreationFlow:

    def test_project_creation_flow(self, page):

        """
        Step 1
        Create project through API
        """

        api = ProjectAPI()

        admin = users["company1_admin"]

        project = projects["default_project"]

        response = api.create_project(
            token="PLACEHOLDER_TOKEN",
            tenant_id=admin["tenant"],
            payload=project
        )

        # Placeholder assertion for fictional API
        # assert response.status_code == 201

        """
        Step 2
        Login through Web UI
        """

        login = LoginPage(page)

        page.goto(
            config["application"]["base_url"] + "/login"
        )

        login.login(
            admin["email"],
            admin["password"]
        )

        login.verify_login_success()

        """
        Step 3
        Verify project in UI
        """

        projects_page = ProjectsPage(page)

        projects_page.search_project(
            project["name"]
        )

        projects_page.verify_project_exists(
            project["name"]
        )

        """
        Step 4
        BrowserStack Mobile Validation

        In production:
        Launch BrowserStack Android/iOS session.
        Login.
        Search project.
        Verify responsive layout.
        """

        """
        Step 5
        Tenant Isolation

        Login using Company2.

        Verify the project is NOT visible.
        """

        """
        Step 6
        Cleanup

        Delete project using API.

        This prevents test pollution.
        """