# @Time:2023/1/2 21:50
# @Author:Henry
from time import sleep
from selenium.webdriver.common.by import By
from base.ObjectMap import ObjectMap
from base.GoodsBase import GoodsBase
from common.tools import get_img_path


class GoodsPage(GoodsBase, ObjectMap):
    def input_goods_title(self, driver, input_value):
        """
        输入商品标题
        :param driver:
        :param input_value:
        :return:
        """

        goods_title_xpath = self.goods_title()
        return self.element_fill_value(driver, By.XPATH, goods_title_xpath, input_value)

    def input_goods_details(self, driver, input_value):
        """
        输入商品详情
        :param driver:
        :param input_value:
        :return:
        """

        goods_details_xpath = self.goods_details()
        return self.element_fill_value(driver, By.XPATH, goods_details_xpath, input_value)

    def select_goods_num(self, driver, num):
        """
        选择商品数量
        :param driver:
        :param num:
        :return:
        """

        goods_num_add_xpath = self.goods_num(plus=True)
        for i in range(num):
            self.element_click(driver, By.XPATH, goods_num_add_xpath)
            sleep(0.5)

    def upload_goods_img(self, driver, img_name):
        """
        上传商品图片
        :param driver:
        :param img_name:
        :return:
        """

        img_path = get_img_path(img_name)
        upload_xpath = self.goods_img()
        return self.upload(driver, By.XPATH, upload_xpath, img_path)

    def input_goods_price(self, driver, input_value):
        """
        输入商品单价
        :param driver:
        :param input_value:
        :return:
        """

        goods_price_xpath = self.goods_price()
        return self.element_fill_value(driver, By.XPATH, goods_price_xpath, input_value)

    def select_goods_status(self, driver, select_name):
        """
        选择商品状态
        :param driver:
        :param select_name: 上架，下架
        :return:
        """

        goods_status_xpath = self.goods_status()
        self.element_click(driver, By.XPATH, goods_status_xpath)
        sleep(1)
        goods_status_select_xpath = self.goods_status_select(select_name)
        return self.element_click(driver, By.XPATH, goods_status_select_xpath)

    def click_bottom_button(self, driver, button_name):
        """
        点击底部按钮
        :param driver:
        :param button_name:
        :return:
        """

        button_xpath = self.add_goods_bottom_button(button_name)
        return self.element_click(driver, By.XPATH, button_xpath)

    # 将新增二手商品页面整个页面流程做一个填值
    def add_new_goods(
            self, driver, goods_title, goods_details, goods_num, goods_pic_list,
            goods_price, goods_status, bottom_button_name):
        """
        新增二手商品
        :param driver:
        :param goods_title:
        :param goods_details:
        :param goods_num:
        :param goods_pic_list:
        :param goods_price:
        :param goods_status:
        :param bottom_button_name:
        :return:
        """

        self.input_goods_title(driver, goods_title)
        self.input_goods_details(driver, goods_details)
        self.select_goods_num(driver, goods_num)
        for goods_pic in goods_pic_list:
            self.upload_goods_img(driver, goods_pic)
            sleep(5)
        self.input_goods_price(driver, goods_price)
        self.select_goods_status(driver, goods_status)
        self.click_bottom_button(driver, bottom_button_name)
        return True