# @Time:2023/1/3 17:02
# @Author:Henry
import pytest
from config.driver_config import DriverConfig


@pytest.fixture(scope="function")
def driver():
    get_driver = DriverConfig().driver_config()
    yield get_driver
    get_driver.quit()
