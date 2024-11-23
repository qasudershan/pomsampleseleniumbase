from pages.base_page import BasePage

class TemplatesPage(BasePage):
    TEMPLATE_NAMES = "css selector .template-name"
    ACTIVE_TEMPLATE = "css selector .active-template"

    def get_5template_names(self):
        template_elements = self.find_elements(self.TEMPLATE_NAMES)
        return [template.text for template in template_elements[:5]]

    def get_active_template(self):
        return self.get_text(self.ACTIVE_TEMPLATE)
