from pages.basepage import SearchPage
from locators.page_locators import FormPageLocators as Locators


class FormPage(SearchPage):
    def __init__(self, page):
        super().__init__(page)

    def screenshots_water(self, path):
        return self.screenshot(Locators.FORM_AUTHORIZE_water, path)

    def screenshots_weight(self, path):
        return self.screenshot(Locators.FORM_AUTHORIZE_weight, path)

    def screenshots_energy(self, path):
        return self.screenshot(Locators.FORM_AUTHORIZE_energy, path)

