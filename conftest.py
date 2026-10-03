import pytest
from _pytest import scope
from playwright.sync_api import Page,expect

from pages import products_page
from pages.products_page import ProductsPage

from pages.login_page import LoginPage
from playwright.sync_api import Page, expect
import json
from pathlib import Path
from utils.environment_reader import get_environment
@pytest.fixture

def environment(request):
    env_name = request.config.getoption("--env")
    return get_environment(env_name)

@pytest.fixture(scope="session")
def test_data():
    with open("test_data/test_data.json", "r") as read_file:
        test_data = json.load(read_file)
        return test_data
@pytest.fixture

def logged_in_page(page:Page, environment, test_data):
    page.goto(environment["base_url"])

    login_page = LoginPage(page)
    login_page.login(test_data["login"]["username"], test_data["login"]["password"])
    product_page = ProductsPage(page)
    expect(product_page.page_title).to_have_text("Products")
    return page
@pytest.fixture(autouse=True)
def screenshot_on_failure(page, request):
    yield

    if request.node.rep_call.failed:
        safe_name = request.node.name.replace(":", "_")
        screenshot_path = Path("screenshots") / f"{safe_name}.png"
        page.screenshot(path=str(screenshot_path))

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="qa",
        help="Environment to run tests against"
    )


