import pytest

from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):

    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/inventory.html")
    driver.maximize_window()
    print(driver.title)
    request.cls.driver = driver
    yield
    driver.close()
