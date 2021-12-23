from time import sleep

import pytest
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

from .config import ADMIN_ID, ADMIN_PASSWORD, BASE_URL

options = Options()
options.page_load_strategy = "eager"


@pytest.fixture
def driver():
    """The selenium driver."""
    # noinspection PyArgumentList
    driver = Edge(options=options)
    driver.implicitly_wait(3)
    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def login(driver, request):
    """Log in as admin."""
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
