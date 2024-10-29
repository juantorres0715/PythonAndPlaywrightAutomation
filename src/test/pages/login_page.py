from src.test.utils.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # locators
        self.username_input_field = "input[id='user-name']"
        self.password_input_field = "input[id='password']"
        self.login_button = "input[id='login-button']"

        # Methods
    def login_process(self, username, password):
        self.send_text(self.username_input_field, username)
        self.send_text(self.password_input_field, password)
        self.click_on_element(self.login_button)

    def click_on_product_button(self):
        self.click_on_element(self.login_button)