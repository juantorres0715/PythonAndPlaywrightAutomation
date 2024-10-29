from src.test.utils.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # locators
        self.username_input_field = page.locator("#user-name")
        self.password_input_field = page.locator("#password")
        self.login_button = page.locator("#login-button")

    # Methods
    def login_process(self, username, password):
        self.send_text(self.username_input_field, username)
        self.send_text(self.password_input_field, password)
        self.click_on_element(self.login_button)

    def click_on_product_button(self):
        self.click_on_element(self.login_button)