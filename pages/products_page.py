from playwright.sync_api import Page

class ProductsPage :
    def __init__(self,page : Page) :
        self.page = page
        self.page_title = page.locator('[data-test="title"]')
        self.product = page.locator("#item_5_img_link")
        self.clicked_product = page.locator('[data-test="item-sauce-labs-fleece-jacket-img"]')
        self.add_to_cart = page.locator('[data-test="add-to-cart"]')
        self.cart_badge =  page.locator('[data-test="shopping-cart-badge"]')
        self.cart_link = page.locator('[data-test="shopping-cart-link"]')

    def select_product(self):
        self.product.click()


    def click_add_to_cart(self):
        self.add_to_cart.click()

    def click_cart_link(self):
        self.cart_link.click()




