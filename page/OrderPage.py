# @Time:2023/1/2 22:07
# @Author:Henry
from selenium.webdriver.common.by import By
from base.OrderBase import OrderBase
from base.ObjectMap import ObjectMap
from logs.log import log

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

    def click_order_operation(self, driver, product_title, operation):
        """
        点击订单的操作按钮
        :param driver:
        :param product_title:
        :param operation:
        :return:
        """
        log.info("订单标题为" + product_title + ",点击订单的操作按钮" + operation)
        button_xpath = self.order_operation(product_title, operation)
        return self.element_click(driver, By.XPATH, button_xpath)

    def click_order_operation_confirm(self, driver):
        """
        点击订单操作按钮后的弹框的确认按钮
        :param driver:
        :return:
        """
        log.info("点击订单操作按钮后的弹框的确认按钮")
        button_xpath = self.order_operation_confirm()
        return self.element_click(driver, By.XPATH, button_xpath)

    def click_delivery_logistics(self, driver):
        """
        点击物流
        :param driver:
        :return:
        """
        log.info("点击物流")
        input_xpath = self.delivery_logistics()
        return self.element_click(driver, By.XPATH, input_xpath)

    def click_select_logistics(self, driver, company):
        """
        选择物流公司
        :param criver:
        :param company:
        :return:
        """
        log.info("选择物流公司")
        select_xpath = self.select_logistics(company)
        return self.element_click(driver, By.XPATH, select_xpath)

    def input_logistics_order_no(self, driver, order_no):
        """
        填入物流单号
        :param driver:
        :param order_no:
        :return:
        """
        log.info("填入物流单号" + str(order_no))
        input_xpath = self.logistics_order_no()
        return self.element_fill_value(driver, By.XPATH, input_xpath, order_no)

    def click_evaluation(self, driver, num):
        """
        评价星级
        :param driver:
        :param num:
        :return:
        """
        log.info("评价星级：" + str(num) + "星")
        star_xpath = self.evaluation(num)
        return self.element_click(driver, By.XPATH, star_xpath)

    def click_evaluation_confirm(self, driver):
        """
        评价完后点击确定
        :param driver:
        :return:
        """
        log.info("评价完后点击确定")
        button_xpath = self.evaluation_confirm()
        return self.element_click(driver, By.XPATH, button_xpath)
