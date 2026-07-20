from playwright.sync_api import expect
from automation.pages.base_page import BasePage


class ProjectsPage(BasePage):

    SEARCH_BOX = "#project-search"

    PROJECT_CARD = ".project-card"

    CREATE_BUTTON = "#create-project"

    def search_project(self, project_name):

        self.fill(self.SEARCH_BOX, project_name)

    def verify_project_exists(self, project_name):

        expect(
            self.page.locator(
                self.PROJECT_CARD
            )
        ).to_contain_text(project_name)

    def get_project_cards(self):

        return self.page.locator(
            self.PROJECT_CARD
        ).all()

    def verify_tenant(self, tenant):

        cards = self.get_project_cards()

        for card in cards:

            assert tenant in card.text_content()