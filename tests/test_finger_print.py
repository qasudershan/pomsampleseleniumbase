import pytest
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.templates_page import TemplatesPage
from pages.fingerprint_page import FingerPrintPage
from seleniumbase import BaseCase

class TestFingerPrint(BaseCase):

    @pytest.mark.xfail
    def test_finger_print(self):
        # Initialize page objects
        login = LoginPage()
        profile = ProfilePage()
        templates = TemplatesPage()
        fingerprint = FingerPrintPage()

        # Step 1: Log in with valid credentials
        self.log_info("Logging in with valid credentials.")
        login.login("engg_user.noreply@prezent.ai", "kiqjemkh")

        # Step 2: Navigate to profile
        self.log_info("Navigating to profile.")
        profile.go_to_profile()

        # Step 3: Click fingerprint tab
        self.log_info("Clicking fingerprint tab.")
        fingerprint.go_to_fingerprint_tab()

        # Step 4: Retake Fingerprint and complete the steps
        self.log_info("Clicking on Re-take Fingerprint and completing the steps.")
        fingerprint.retake_fingerprint()

        # TODO: Step: At each step, print all available options and indicate which option was selected

        # Step 5: Click Go Back to Prezent and then go to Profile and log out
        self.log_info("Clicking 'Go Back to Prezent,' navigating to profile, and logging out.")
        profile.logout()
