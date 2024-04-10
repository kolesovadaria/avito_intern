import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope="session")
def browser(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    print('HELLO1')
    yield browser
    print('BYE')
    browser.close()


@pytest.fixture
def context(browser: browser) -> None:
    context = browser.new_context()
    print('HELLO2')
    yield context
    print('BYE2')
    context.close()


@pytest.fixture
def page(context: context) -> None:
    page = context.new_page()
    print('HELLO3')
    yield page
    print('BYE3')
    page.close()
