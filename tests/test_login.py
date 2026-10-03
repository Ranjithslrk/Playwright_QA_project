import pytest
from playwright.sync_api import Page,expect
from pytest_base_url.plugin import base_url

from pages.login_page import LoginPage
from pages.products_page import ProductsPage

from utils.test_data_reader import get_login_users



@pytest.mark.parametrize(
    "username, password, expected_type, expected_result",
    [
        (
            user["username"],
            user["password"],
            user["expected_type"],
            user["expected_result"]
        )
        for user in get_login_users()
    ]
)
@pytest.mark.smoke
def test_login(page:Page,environment,username, password,expected_type,expected_result):
    page.goto(environment["base_url"])
    login_page = LoginPage(page)
    login_page.login(username, password)
    if expected_type == "locked":
        expect(login_page.error_msg).to_have_text(expected_result)
    else:
        product_page = ProductsPage(page)
        expect(product_page.page_title).to_have_text(expected_result)



