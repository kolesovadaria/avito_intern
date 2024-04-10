from pages.form_page import FormPage
from conftest import browser, context, page
import os

URL = "https://www.avito.ru/avito-care/eco-impact"


class TestV:

    path3 = "../output/screenshot3.png"

    def test_search3(self, browser, context, page):
        my_page = FormPage(page)
        my_page.navigate(URL)
        my_page.screenshots_energy(self.path3)
        assert os.path.exists(self.path3) == True