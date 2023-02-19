# @Time:2023/1/4 22:57
# @Author:Henry
from time import sleep
import pytest
from page.LoginPage import LoginPage
import allure
from common.report_add_img import add_img_2_report


class TestLoginAssert:

    @pytest.mark.login
    @allure.feature("登录")
    @allure.description("登录后断言图片")
    def test_login_assert(self, driver):
        """登录后断言"""
        with allure.step("登录"):
            LoginPage().login(driver, "jay")
            sleep(3)
            add_img_2_report(driver, "登录")

        with allure.step("断言图片"):
            assert LoginPage().login_assert(driver, "head_img.png") > 0.9
