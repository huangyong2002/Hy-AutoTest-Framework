# @Time:2023/1/10 22:07
# @Author:Henry

from time import sleep
import pytest
import allure

from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.GoodsPage import GoodsPage
from page.TradingMarketPage import TradingMarketPage
from page.OrderPage import OrderPage
from common.report_add_img import add_img_2_report
from common.tools import get_now_date_time_str


class TestTradingFlow:
    @pytest.mark.trading_flow
    @allure.feature("交易流")
    @allure.description("交易流")
    def test_trading_flow(self, driver):
        """交易流"""
        with allure.step("登录卖家"):
            LoginPage().api_login(driver, "jay")
            add_img_2_report(driver, "登录卖家")

        with allure.step("进入新增二手商品"):
            LeftMenuPage().click_level_one_menu(driver, "产品")
            sleep(1)
            LeftMenuPage().click_level_two_menu(driver, "新增二手商品")
            sleep(2)
            add_img_2_report(driver, "进入新增二手商品")

        with allure.step("新增商品"):
            goods_title = "交易流测试" + get_now_date_time_str()
            GoodsPage().add_new_goods(
                driver,
                goods_title=goods_title,
                goods_details="交易流测试",
                goods_num=1,
                goods_pic_list=["商品图片一.jpg"],
                goods_price=99,
                goods_status="上架",
                bottom_button_name="提交"
            )
            add_img_2_report(driver, "新增商品")
            sleep(8)

        with allure.step("登录买家"):
            LoginPage().api_login(driver, "william")
            add_img_2_report(driver, "登录买家")

        with allure.step("进入交易市场"):
            LeftMenuPage().click_level_one_menu(driver, "交易市场")
            add_img_2_report(driver, "进入交易市场")

        with allure.step("搜索宝贝"):
            TradingMarketPage().input_search_input(driver, goods_title)
            TradingMarketPage().click_search(driver)
            sleep(2)
            add_img_2_report(driver, "搜索宝贝")

        with allure.step("点击商品卡片"):
            TradingMarketPage().click_product_card(driver, goods_title)
            sleep(1)
            add_img_2_report(driver, "点击商品卡片")

        with allure.step("点击我想要"):
            TradingMarketPage().click_i_want(driver)
            sleep(1)
            add_img_2_report(driver, "点击我想要")

        with allure.step("选择收货地址"):
            TradingMarketPage().click_address(driver)
            sleep(1)
            TradingMarketPage().select_detail_address(driver, 1)
            sleep(1)
            add_img_2_report(driver, "选择收货地址")

        with allure.step("点击确定"):
            TradingMarketPage().click_bottom_button(driver)
            sleep(1)
            add_img_2_report(driver, "点击确定")

        with allure.step("买家支付"):
            OrderPage().click_order_operation(driver, goods_title, "去支付")
            sleep(1)
            OrderPage().click_order_operation_confirm(driver)
            add_img_2_report(driver, "买家支付")

        with allure.step("登录买家"):
            LoginPage().api_login(driver, "jay")
            add_img_2_report(driver, "登录买家")

        with allure.step("进入已卖出的宝贝"):
            LeftMenuPage().click_level_one_menu(driver, "我的订单")
            sleep(1)
            LeftMenuPage().click_level_two_menu(driver, "已卖出的宝贝")
            sleep(2)
            add_img_2_report(driver, "进入已卖出的宝贝")

        with allure.step("卖家发货"):
            OrderPage().click_order_operation(driver, goods_title, "去发货")
            sleep(1)
            OrderPage().click_delivery_logistics(driver)
            sleep(1)
            OrderPage().click_select_logistics(driver, "顺丰速运")
            sleep(1)
            OrderPage().input_logistics_order_no(driver, "123456789")
            sleep(1)
            OrderPage().click_order_operation_confirm(driver)
            add_img_2_report(driver, "卖家发货")
            sleep(3)

        with allure.step("登录买家"):
            LoginPage().api_login(driver, "william")
            add_img_2_report(driver, "登录买家")

        with allure.step("进入已买到的宝贝"):
            LeftMenuPage().click_level_one_menu(driver, "我的订单")
            sleep(1)
            LeftMenuPage().click_level_two_menu(driver, "已买到的宝贝")
            sleep(2)
            add_img_2_report(driver, "进入已买到的宝贝")

        with allure.step("买家确认收货"):
            OrderPage().click_order_operation(driver, goods_title, "去确认收货")
            sleep(1)
            OrderPage().click_order_operation_confirm(driver)
            add_img_2_report(driver, "买家确认收货")

        with allure.step("买家评价"):
            OrderPage().click_order_operation(driver, goods_title, "去评价")
            sleep(1)
            OrderPage().click_evaluation(driver, 5)
            sleep(2)
            OrderPage().click_evaluation_confirm(driver)
            add_img_2_report(driver, "买家评价")