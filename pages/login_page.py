from playwright.sync_api import Page
from utils.logger import logger


class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_msg =page.get_by_text("Epic sadface: Sorry, this user has been locked out.")

    def login(self,username,password):
        logger.info(f"Attempting login with username: {username}")
        self.username.fill(username)
        self.password.fill(password)

        self.login_button.click()
        logger.info("Login button clicked")

