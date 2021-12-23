from time import sleep

import pytest
from selenium.webdriver.common.by import By

from .config import ADMIN_ID, ADMIN_PASSWORD, BASE_URL


@pytest.mark.no_login
def test_wrong_password(driver):
    """Cannot log in with wrong password."""
    driver.get(BASE_URL)

    # redirected to /login
    assert driver.current_url.endswith("/login")

    # right ID & wrong PASSWORD
    driver.find_element(
        By.CSS_SELECTOR,
        ".el-form-item:nth-child(1) .el-input__inner",
    ).send_keys(ADMIN_ID)

    driver.find_element(
        By.CSS_SELECTOR,
        ".el-form-item:nth-child(2) .el-input__inner",
    ).send_keys(ADMIN_PASSWORD + "wrong")

    # there is no message
    assert not driver.find_elements(By.CLASS_NAME, "el-message__content")

    # log in
    driver.find_element(By.CLASS_NAME, "el-button").click()
    sleep(1)

    # there is a message
    assert driver.find_element(By.CLASS_NAME, "el-message__content").text

    # still at login page
    assert driver.current_url.endswith("/login")


@pytest.mark.no_login
@pytest.mark.skip(reason="https://e.gitee.com/ecnu_sei_hysun/issues/list?issue=I4NWCP")
def test_home2login(driver):
    """Redirect to /login if not logged in."""
    driver.get(BASE_URL + "#/home")

    # there is a message
    assert driver.find_element(By.CLASS_NAME, "el-message__content").text

    # redirected to /login
    assert driver.current_url.endswith("/login")
