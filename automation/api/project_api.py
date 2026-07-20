from automation.api.api_client import APIClient


class ProjectAPI:

    PROJECT_ENDPOINT = "/api/v1/projects"

    def __init__(self):

        self.client = APIClient()

    def create_project(self, token, tenant_id, payload):

        headers = {
            "Authorization": f"Bearer {token}",
            "X-Tenant-ID": tenant_id
        }

        response = self.client.post(
            self.PROJECT_ENDPOINT,
            json=payload,
            headers=headers
        )

        return response