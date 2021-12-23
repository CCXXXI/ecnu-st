import pytest
from selenium.webdriver.common.by import By

from tests.config import BASE_URL


@pytest.mark.parametrize(
    "s",
    [
        "今日咨询数",
        "今日咨询时长",
        "在线咨询师",
        "正在进行的咨询",
        "在线督导",
        pytest.param(
            "正在进行的督导会话",
            marks=pytest.mark.xfail(
                reason="https://e.gitee.com/ecnu_sei_hysun/issues/list?issue=I4NWCV",
            ),
        ),
        "当月咨询数量排行",
        "当月好评数量排行",
    ],
)
def test_home(driver, s):
    """The admin can view all the statistics data."""
    driver.get(BASE_URL + "#/home")

    assert driver.find_element(
        By.XPATH,
        f"//*[contains(text(), '{s}')]",
    ).is_displayed()
