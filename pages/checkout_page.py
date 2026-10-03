from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page : Page):
        self.page = page
        self.fname = page.get_by_placeholder("First Name")
        self.lname = page.get_by_placeholder("Last Name")
        self.zipcode =  page.get_by_placeholder("Zip/Postal Code")
        self.click_button  =  page.locator('[data-test="continue"]')
        self.checkout_title =page.locator('[data-test="title"]')
    def fill_checkout_page(self,fname,lname,zipcode):
        self.fname.fill(fname)
        self.lname.fill(lname)
        self.zipcode.fill(zipcode)
        self.click_button.click()




