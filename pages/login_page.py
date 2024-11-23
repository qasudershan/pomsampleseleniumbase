from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://prezent-uatstaging.myprezent.com/signin"
    EMAIL_INPUT = "input[id='username']"
    PASSWORD_INPUT = "input[id='password']"
    CONTINUE_BUTTON = "button[id='continue']"
    LOGIN_BUTTON = "button[id='submit']"

    def open_login_page(self):
        self.open(self.URL)

    def is_email_input_field_visible(self):
        return self.is_element_visible(self.EMAIL_INPUT)

    def login(self, email, password):
        self.open_login_page()
        self.type(self.EMAIL_INPUT, email)
        self.click(self.CONTINUE_BUTTON)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
