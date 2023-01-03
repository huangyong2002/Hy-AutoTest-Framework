# @Time:2023/1/2 21:53
# @Author:Henry
from time import sleep

from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.GoodsPage import GoodsPage


class TestAddGoods:


    def test_add_goods_001(self,driver):
        LoginPage().login(driver, "jay")
        LeftMenuPage().click_level_one_menu(driver, "产品")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver, "新增二手商品")
        sleep(2)
        GoodsPage().add_new_goods(
            driver,
            goods_title="新增商品测试",
            goods_details="新增商品测试详情",
            goods_num=1,
            goods_pic_list=["商品图片一.jpg"],
            goods_price=123,
            goods_status="上架",
            bottom_button_name="提交"
        )
        sleep(3)
