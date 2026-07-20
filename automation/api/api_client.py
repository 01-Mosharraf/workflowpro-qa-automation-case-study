import requests

from automation.config.config_reader import ConfigReader

config = ConfigReader.load_config()


class APIClient:

    def __init__(self):

        self.base_url = config["application"]["base_url"]

    def get(self, endpoint, headers=None):

        return requests.get(
            self.base_url + endpoint,
            headers=headers
        )

    def post(self, endpoint, json=None, headers=None):

        return requests.post(
            self.base_url + endpoint,
            json=json,
            headers=headers
        )

    def delete(self, endpoint, headers=None):

        return requests.delete(
            self.base_url + endpoint,
            headers=headers
        )