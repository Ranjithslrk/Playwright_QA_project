from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_page = page.locator('[data-test="checkout"]')
        self.cart_title =page.locator('[data-test="title"]')
        self.cart_inventory=page.locator('[data-test="inventory-item-name"]')

    def click_checkout(self):
        self.checkout_page.click()







