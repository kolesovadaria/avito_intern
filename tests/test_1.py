from pages.form_page import FormPage
from conftest import browser, context, page
import os

URL = "https://www.avito.ru/avito-care/eco-impact"


class TestV:

    path = "../output/screenshot1.png"

    def test_search(self, browser, context, page):
        my_page = FormPage(page)
        my_page.navigate(URL)
        my_page.screenshots_weight(self.path)
        assert os.path.exists(self.path) == True