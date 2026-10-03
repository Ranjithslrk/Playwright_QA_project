from playwright.sync_api import Page

class OverviewPage:
    def __init__(self, page: Page):
        self.page=page

        self.finish_button =page.locator('[data-test="finish"]')
        self.overview_title =page.locator('[data-test="title"]')
        self.overview_check = page.locator('[data-test="inventory-item-name"]')
        self.order_confirm = page.locator('[data-test="complete-header"]')

    def click_button(self):
        self.finish_button.click()


