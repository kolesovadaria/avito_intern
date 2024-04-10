from pages.form_page import FormPage
from conftest import browser, context, page
import os

URL = "https://www.avito.ru/avito-care/eco-impact"


class TestV:

    path2 = "../output/screenshot2.png"

    def test_search2(self, browser, context, page):
        my_page = FormPage(page)
        my_page.navigate(URL)
        my_page.screenshots_water(self.path2)
        assert os.path.exists(self.path2) == True