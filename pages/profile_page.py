from pages.base_page import BasePage

class ProfilePage(BasePage):
    BASICS_TAB = 'a[href="#basics"]'
    PROFILE_ICON = "div.right-nav-item.profile-link"
    LOGOUT_BUTTON = "div>button.edit-profile-btn.log-out-button"

    def go_to_profile(self):
        self.click(self.PROFILE_ICON)

    def logout(self):
        self.click(self.BASICS_TAB)
        self.sleep(2)  # Sleep for 2 seconds for the logout button to be ready
        self.click(self.LOGOUT_BUTTON)
