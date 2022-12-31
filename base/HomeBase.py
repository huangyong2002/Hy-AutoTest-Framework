# @Time:2022/12/30 17:11
# @Author:Henry
class HomeBase:

    def wallet_swich(self):
        """
        首页的钱包开关
        :return:
        """
        return "//span[contains(@class,'switch')]"

    def logo(self):
        """
        进入系统后，首页左上角的logo
        :return:
        """
        return "//div[contains(text(),'二手')]"

    def welcome(self):
        """
        首页欢迎您回来
        :return:
        """
        return "//span[starts-with(text(),'欢迎您回来')]"
    def show_date(self):
        """
        首页显示日期
        :return:
        """
        return "//div[text()='我的日历']/following-sibling::div"

    def home_user_avator(self):
        """
        首页头像大图
        :return:
        """
        # 同级元素的上一个元素
        return "//span[contains(text(),'欢迎您回来')]/parent::div/preceding-sibling::div//img"
    def home_user_avator_2(self):
        """
        首页头像大图二
        :return:
        """
        return "//span[text()='我的地址']//ancestor::div[@class='first_card']/div[contains(@class,'avater')]//img"
