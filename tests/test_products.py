import pytest
from playwright.sync_api import Page,expect

from conftest import test_data
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.overview_page import OverviewPage



@pytest.mark.regression

def test_products(logged_in_page:Page, test_data):
    product_name = test_data["product"]["Cart_item"]
    first_name = test_data["checkout"]["fname"]
    last_name = test_data["checkout"]["lname"]
    zipcode = test_data["checkout"]["zipcode"]
    page = logged_in_page


    product_page = ProductsPage(page)



    expect(product_page.product).to_be_visible()
    product_page.select_product()
    expect(product_page.clicked_product).to_be_visible()
    product_page.click_add_to_cart()
    expect(product_page.cart_badge).to_have_count(1)
    product_page.click_cart_link()


    cart_page = CartPage(page)
    expect(cart_page.cart_title).to_have_text("Your Cart")
    expect(cart_page.cart_inventory).to_have_text(product_name)
    cart_page.click_checkout()

    check_out_page = CheckoutPage(page)
    expect(check_out_page.checkout_title).to_have_text("Checkout: Your Information")
    check_out_page.fill_checkout_page(first_name,last_name,zipcode)




    overview = OverviewPage(page)
    expect(overview.overview_title).to_have_text("Checkout: Overview")
    expect(overview.overview_check).to_have_text(product_name)
    overview.click_button()
    expect(overview.order_confirm).to_have_text("Thank you for your order!")