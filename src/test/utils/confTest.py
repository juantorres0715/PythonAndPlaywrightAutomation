import pytest
from playwright.sync_api import sync_playwright

url = "https://www.saucedemo.com/"

@pytest.fixture(scope = "function")
def browser_set_up():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        yield page
        browser.close()