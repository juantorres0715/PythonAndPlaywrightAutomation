from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    # Common methods
    def click_on_element(self, selector):
        self.page.click(selector)

    def get_title(self):
        return self.page.title()

    def send_text(self, selector, text):
        self.page.fill(selector, text)