from automation.pages.login_page import LoginPage
from automation.config.config_reader import ConfigReader
from automation.utils.test_data_manager import TestDataManager
from automation.utils.logger import get_logger

logger = get_logger(__name__)

config = ConfigReader.load_config()

users = TestDataManager.load("users.json")


def test_user_login(page):

    logger.info("Opening login page")

    login = LoginPage(page)

    page.goto(
        config["application"]["base_url"] + "/login"
    )

    user = users["company1_admin"]

    login.login(
        user["email"],
        user["password"]
    )

    login.verify_login_success()

    logger.info("Login successful")