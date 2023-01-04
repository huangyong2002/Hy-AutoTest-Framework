# @Time:2023/1/4 22:57
# @Author:Henry
from time import sleep
import pytest
from page.LoginPage import LoginPage


class TestLoginAssert:

    @pytest.mark.login
    def test_login_assert(self, driver):
        """登录后断言"""
        LoginPage().login(driver, "jay")
        sleep(3)
        assert LoginPage().login_assert(driver, "head_img.png") > 0.9
