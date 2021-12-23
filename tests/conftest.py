from time import sleep

import pytest
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

from .config import ADMIN_ID, ADMIN_PASSWORD, BASE_URL

options = Options()
options.page_load_strategy = "eager"


@pytest.fixture(scope="module")
def driver():
    """The selenium driver."""
    # noinspection PyArgumentList
    _driver = Edge(options=options)
    _driver.implicitly_wait(3)
    yield _driver
    _driver.quit()


@pytest.fixture(autouse=True, scope="module")
def login(driver, request):
    """The happy path of logging in as admin."""
    if "no_login" in request.keywords:
        return

    driver.get(BASE_URL)

    driver.find_element(
        By.CSS_SELECTOR,
        ".el-form-item:nth-child(1) .el-input__inner",
    ).send_keys(ADMIN_ID)

    driver.find_element(
        By.CSS_SELECTOR,
        ".el-form-item:nth-child(2) .el-input__inner",
    ).send_keys(ADMIN_PASSWORD)

    driver.find_element(By.CLASS_NAME, "el-button").click()
    sleep(3)

    # redirected to /home
    assert driver.current_url.endswith("/home")
