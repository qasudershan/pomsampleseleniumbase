from seleniumbase import BaseCase

class BasePage(BaseCase):
    def open(self, url):
        self.open(url)

    def find_element(self, locator):
        return self.find_element(locator)

    def click(self, locator):
        self.click(locator)

    def type_text(self, locator, text):
        self.type(locator, text)

    def get_text(self, locator):
        return self.get_text(locator)
