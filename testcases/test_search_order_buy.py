# @Time:2023/1/2 22:08
# @Author:Henry
from time import sleep

import pytest
from page.LeftMenuPage import LeftMenuPage
from page.LoginPage import LoginPage
from page.OrderPage import OrderPage

# 参数化
# 打开浏览器点击全部，然后退出，然后再打开，点击待付款，然后退出...

tab_list = ["全部", "待付款", "待发货", "运输中", "待确认", "待评价"]

class TestOrderBuy:
    @pytest.mark.parametrize("tab",tab_list)
    def test_order_buy(self,driver,tab):
        LoginPage().login(driver, "jay")
        LeftMenuPage().click_level_one_menu(driver, "我的订单")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver, "已买到的宝贝")
        sleep(2)
        # tab_list = ["全部", "待付款", "待发货", "运输中", "待确认", "待评价"]
        # for tab in tab_list:
        OrderPage().click_order_tab(driver, tab)
        sleep(2)