import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope="session")
def browser(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()


@pytest.fixture
def context(browser: browser) -> None:
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture
def page(context: context) -> None:
    page = context.new_page()
    yield page
    page.close()
