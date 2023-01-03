# @Time:2023/1/3 12:44
# @Author:Henry
from time import sleep
import pytest


class TestPytestMClass:
    @pytest.fixture(scope="class")
    def scope_class(self):
        print("我是class级别，我只执行一次")

    @pytest.mark.bing
    def test_open_bing(self,driver,scope_class):
        # driver = DriverConfig().driver_config()
        driver.get("https://cn.bing.com")
        sleep(3)

    @pytest.mark.baidu
    def test_open_baidu(self,driver,scope_class):
        print("test_open_baidu")
        # driver = DriverConfig().driver_config()
        driver.get("https://www.baidu.com")
        sleep(3)

    @pytest.mark.google
    def test_open_google(self,driver,scope_class):
        # driver = DriverConfig().driver_config()
        driver.get("https://www.google.com")
        sleep(3)
