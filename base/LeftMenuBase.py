# @Time:2022/12/31 8:05
# @Author:Henry
class LeftMenuBase:
    def level_one_menu(self,menu_name):
        """
        一级菜单栏
        :param menu_name:菜单栏名称
        :return:
        """
        return "//aside[@class='el-aside']//span[text()='" + menu_name + "']/ancestor::li"
    def level_two_menu(self,menu_name):
        """
        二级菜单栏
        :param menu_name:菜单栏名称
        :return:
        """
        return "//aside[@class='el-aside']//span[text()='" + menu_name + "']/parent::li"

if __name__ == '__main__':
    # print(LeftMenuBase().level_one_menu("交易市场"))
    print(LeftMenuBase().level_two_menu("已买到的宝贝"))
