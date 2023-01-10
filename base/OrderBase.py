# @Time:2023/1/2 22:06
# @Author:Henry
class OrderBase:

    def order_tab(self, tab_name):
        """
        订单tab按钮
        :param tab_name:全部，代付款，代发货，运输中，待确认，待评价
        :return:
        """

        return "//div[@role='tab' and text()='" + tab_name + "']"

    def order_operation(self, product_title, operation):
        """
        订单的操作按钮
        :param product_title:
        :param operation:
        :return:
        """
        return "//div[text()='" + product_title + "']/ancestor::tr//span[text()='" + operation + "']/parent::button"

    def order_operation_confirm(self):
        """
        点击操作按钮以后，弹框的确定按钮
        :return:
        """
        return "//div[@class='el-dialog__wrapper' and contains(@style,'index')]//span[text()='确 定']/parent::button"

    def delivery_logistics(self):
        """
        发货的物流公司选择框
        :return:
        """
        return "//label[text()='物流公司']/following-sibling::div//input"

    def select_logistics(self, company):
        """
        物流公司
        :param company:
        :return:
        """
        return "//span[text()='" + company + "']/parent::li"

    def logistics_order_no(self):
        """
        物流单号
        :return:
        """
        return "//label[text()='物流单号']/following-sibling::div//input"

    def evaluation(self, num):
        """
        评价星级
        :param num:
        :return:
        """
        return "//span[text()='请给卖家评价']/following-sibling::div/span[" + str(num) + "]/i"

    def evaluation_confirm(self):
        """
        评价完后确定
        :return:
        """
        return "//span[text()='评价']/ancestor::div[@role='dialog']//span[text()='确 定']/parent::button"