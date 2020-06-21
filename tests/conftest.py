import pytest
from base.webdriverfactory import WebDriverFactory
import os

@pytest.yield_fixture()
def setUp(request):
    print("Running method level setUp")
    #request.cls.driver.get("https://www.google.com")
    yield
    print("Running method level tearDown")
    request.cls.wdf.gotoBaseURL(request.cls.driver)


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser, private, url):
    print("Running one time setUp")
    if url:
        wdf = WebDriverFactory(browser, private, baseURL=url)
    else:
        wdf = WebDriverFactory(browser, private)

    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver
        request.cls.wdf = wdf
    yield driver
    driver.quit()
    print("Running one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--private", help="private browser")
    parser.addoption("--url")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def private(request):
    return request.config.getoption("--private")

@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")