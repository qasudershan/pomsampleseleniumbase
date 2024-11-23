from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.templates_page import TemplatesPage
from seleniumbase import BaseCase

class TestLoginProfile(BaseCase):

    def test_login_and_fetch_templates(self):
        # Initialize page objects
        login = LoginPage()
        profile = ProfilePage()
        templates = TemplatesPage()

        # Step 1: Log in with valid credentials
        self.log_info("Logging in with valid credentials.")
        login.login("engg_user.noreply@prezent.ai", "kiqjemkh")

        # Step 2: Navigate to profile
        self.log_info("Navigating to profile.")
        profile.go_to_profile()

        # Step 3: Fetch and validate first 5 template names
        self.log_info("Fetching first five template names.")
        template_names = templates.get_5template_names()
        self.log_info(f"First five templates: {template_names}")
        self.assert_equal(len(template_names), 5, "The number of templates should be 5.")

        # Step 4: Fetch the active template
        self.log_info("Fetching active template.")
        active_template = templates.get_active_template()
        self.log_info(f"Active template: {active_template}")

        # Step 5: Log out from the Basics tab
        self.log_info("Logging out from Basics tab.")
        profile.logout()
        self.assert_true(login.is_email_input_field_visible(), "Email input field should be visible after logout.")
