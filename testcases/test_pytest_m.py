# @Time:2023/1/3 12:44
# @Author:Henry
from time import sleep
from config.driver_config import DriverConfig
import pytest


class TestPytestMClass:

    @pytest.mark.bing
    def test_open_bing(self):
        driver = DriverConfig().driver_config()
        driver.get("https://cn.bing.com")
        sleep(3)
        driver.quit()

    @pytest.mark.baidu
    def test_open_baidu(self):
        print("test_open_baidu")
        driver = DriverConfig().driver_config()
        driver.get("https://www.baidu.com")
        sleep(3)
        driver.quit()

    @pytest.mark.google
    def test_open_google(self):
        driver = DriverConfig().driver_config()
        driver.get("https://www.google.com")
        sleep(3)
        driver.quit()