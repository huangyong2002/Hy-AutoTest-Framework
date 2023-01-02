# @Time:2023/1/2 22:07
# @Author:Henry
from selenium.webdriver.common.by import By
from base.OrderBase import OrderBase
from base.ObjectMap import ObjectMap


class OrderPage(OrderBase, ObjectMap):

    def click_order_tab(self, driver, tab_name):
        """
        订单tab栏按钮
        :param driver:
        :param tab_name:
        :return:
        """

        tab_xpath = self.order_tab(tab_name)
        return self.element_click(driver, By.XPATH, tab_xpath)
