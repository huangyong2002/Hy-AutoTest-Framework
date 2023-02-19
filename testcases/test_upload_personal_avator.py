# @Time:2023/1/2 22:15
# @Author:Henry
from time import sleep

from page.LeftMenuPage import LeftMenuPage
from page.LoginPage import LoginPage
from page.AccountPage import AccountPage


class TestPersonalInfo:
    def test_upload_personal_avatar(self,driver):
        LoginPage().login(driver, "jay")
        LeftMenuPage().click_level_one_menu(driver, "账户设置")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver, "个人资料")
        sleep(2)
        AccountPage().upload_avatar(driver, "个人头像二.jpg")
        sleep(3)
        AccountPage().click_save(driver)
        sleep(3)
