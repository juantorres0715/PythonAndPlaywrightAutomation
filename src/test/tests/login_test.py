import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
from src.test.pages.login_page import LoginPage
from src.test.utils.confTest import browser_set_up

def test_login_process(browser_set_up):
    page = browser_set_up
    login_page = LoginPage(page)

    login_page.login_process("standard_user","secret_sauce")