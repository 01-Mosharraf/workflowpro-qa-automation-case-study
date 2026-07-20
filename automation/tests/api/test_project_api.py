import pytest

@pytest.mark.skip(reason="WorkflowPro is a fictional application.")
def test_user_login(page):
    pass

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