# @Time:2023/1/2 21:36
# @Author:Henry
class GoodsBase:
    def goods_title(self):
        """
        商品标题
        :return:
        """

        return "//form[@class='el-form']//textarea[@placeholder='请输入商品标题']"

    def goods_details(self):
        """
        商品详情
        :return:
        """

        return "//form[@class='el-form']//textarea[@placeholder='请输入商品详情']"

    def goods_num(self, plus=True):
        """
        商品数量
        :param plus:如果为True，则为加号，为False则为直接输入数量
        :return:
        """
        if plus:
            return "//label[@for='product_stock']/following-sibling::div//i[@class='el-icon-plus']/parent::span"
        else:
            return "//label[@for='product_stock']/following-sibling::div//input[@placeholder='商品数量']"

    def goods_img(self):
        """
        商品图片
        :return:
        """

        return "//input[@type='file']"

    def goods_price(self):
        """
        商品单价
        :return:
        """

        return "//form[@class='el-form']//input[@placeholder='请输入商品单价']"

    def goods_status(self):
        """
        商品状态
        :return:
        """

        return "//form[@class='el-form']//input[@placeholder='请选择商品状态']"

    def goods_status_select(self, select_name):
        """
        选择商品状态
        :param select_name:上架，下架
        :return:
        """

        return "//span[text()='" + select_name + "']/parent::li"

    def add_goods_bottom_button(self, button_name):
        """
        新增二手商品底部按钮
        :param button_name:
        :return:
        """

        return "//span[text()='" + button_name + "']/parent::button"