import pytest
from selenium.webdriver.common.by import By

from .config import ADMIN_ID
from .config import ADMIN_PASSWORD
from .config import BASE_URL


@pytest.mark.no_login
def test_wrong_password(driver):
    """Cannot log in with wrong password."""
    driver.get(BASE_URL)

    driver.find_element(
        By.CSS_SELECTOR,
        ".el-form-item:nth-child(1) .el-input__inner",
    ).send_keys(ADMIN_ID)

    driver.find_element(
        By.CSS_SELECTOR,
        ".el-form-item:nth-child(2) .el-input__inner",
    ).send_keys(ADMIN_PASSWORD + "wrong")

    driver.find_element(By.CLASS_NAME, "el-button").click()

    # there is an alert
    assert driver.find_element(By.CSS_SELECTOR, "[role=alert]").is_displayed()

    # still at login page
    assert driver.current_url.endswith("/login")
