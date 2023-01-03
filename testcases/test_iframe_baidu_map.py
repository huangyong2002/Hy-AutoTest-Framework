# @Time:2023/1/2 22:30
# @Author:Henry
from time import sleep

from page.LeftMenuPage import LeftMenuPage
from page.LoginPage import LoginPage
from page.IframeBaiduMapPage import IframeBaiduMapPage


class TestIframeBaiduMap:

    def test_iframe_baidu_map(self, driver):
        LoginPage().login(driver, "jay")
        sleep(3)
        LeftMenuPage().click_level_one_menu(driver, "iframe测试")
        sleep(1)
        IframeBaiduMapPage().switch_2_baidu_map_iframe(driver)
        IframeBaiduMapPage().get_baidu_map_search_button(driver)
        sleep(1)
        IframeBaiduMapPage().iframe_out(driver)
        LeftMenuPage().click_level_one_menu(driver, "首页")
        sleep(3)