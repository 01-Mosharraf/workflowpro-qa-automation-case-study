from automation.api.api_client import APIClient


class AuthAPI:

    LOGIN_ENDPOINT = "/api/v1/login"

    def __init__(self):

        self.client = APIClient()

    def login(self, email, password):

        payload = {
            "email": email,
            "password": password
        }

        response = self.client.post(
            self.LOGIN_ENDPOINT,
            json=payload
        )

        return response