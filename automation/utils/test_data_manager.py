import json
from pathlib import Path


class TestDataManager:

    @staticmethod
    def load(filename):

        path = Path(__file__).parent.parent / "testdata" / filename

        with open(path) as file:

            return json.load(file)