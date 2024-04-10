class SearchPage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def element_is_visible(self, locator):
        self.page.wait_for_selector(locator).is_enabled()

    def screenshot(self, locator, path):
        try:
            self.page.locator(locator).screenshot(path=path)
            return True
        except (ValueError, Exception):
            print(f'Ошибка при создании скриншота')
            return False

    #def screenshots_check(self, locator):
     #   return (self.page.locator(locator)(".status")).to_have_text("Submitted")
