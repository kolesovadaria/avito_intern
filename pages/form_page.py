from pages.basepage import SearchPage
from locators.page_locators import FormPageLocators as Locators


class FormPage(SearchPage):
    def __init__(self, page):
        super().__init__(page)

    def fill_and_submit(self):
        self.element_is_visible(Locators.FORM_AUTHORIZE_water)

    def screenshots_water(self, path):
        return self.screenshot(Locators.FORM_AUTHORIZE_water, path)

    def screenshots_weight(self, path):
        return self.screenshot(Locators.FORM_AUTHORIZE_weight, path)

    def screenshots_energy(self, path):
        return self.screenshot(Locators.FORM_AUTHORIZE_energy, path)

    #def result_text(self):
     #   print(self.screenshots_check())
     #   return self.fill_and_submit().text
