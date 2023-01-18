# @Time:2023/1/18 9:30
# @Author:Henry
from time import sleep
import pytest
import allure
from common.report_add_img import add_img_2_report
from page.LoginPage import LoginPage


class TestCaptchaLogin:
    @pytest.mark.login
    @allure.feature("登录")
    @allure.description("验证码登录")
    def test_captcha_login(self, driver):
        """验证码登录"""
        with allure.step("登录"):
            LoginPage().login(driver, "jay", need_captcha=True)
            sleep(3)
            add_img_2_report(driver, "登录")
