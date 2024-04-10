from pages.form_page import FormPage
from conftest import browser, context, page


URL = "https://www.avito.ru/avito-care/eco-impact"


class TestV:
    path = "../output/screenshot1.png"
    path2 = "../output/screenshot2.png"
    path3 = "../output/screenshot3.png"

    def test_1(self, browser, context, page):
        my_page = FormPage(page)
        my_page.navigate(URL)
        result = my_page.screenshots_weight(self.path)
        assert result, "Скриншот {} не создан".format(self.path)

    def test_2(self, browser, context, page):
        my_page = FormPage(page)
        my_page.navigate(URL)
        result = my_page.screenshots_water(self.path2)
        assert result, "Скриншот {} не создан".format(self.path2)

    def test_3(self, browser, context, page):
        my_page = FormPage(page)
        my_page.navigate(URL)
        result = my_page.screenshots_energy(self.path3)
        assert result, "Скриншот {} не создан".format(self.path3)
