import pytest
from automation.config.config_reader import ConfigReader

config = ConfigReader.load_config()

if config.get("framework", {}).get("demo_mode", False):
    pytest.skip(
        "WorkflowPro API is fictional. API execution is intentionally skipped.",
        allow_module_level=True
    )

from automation.api.project_api import ProjectAPI


def test_create_project_api():

    api = ProjectAPI()

    payload = {
        "name": "Automation Demo Project",
        "description": "Created through API",
        "team_members": [
            "user1",
            "user2"
        ]
    }

    response = api.create_project(
        token="sample_token",
        tenant_id="company1",
        payload=payload
    )

    assert response.status_code == 200