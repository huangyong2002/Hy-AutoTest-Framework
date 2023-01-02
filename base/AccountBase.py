# @Time:2023/1/2 22:12
# @Author:Henry
class AccounttBase:

    def basic_info_avatar_input(self):
        """
        基本资料-个人头像
        :return:
        """

        return "//input[@type='file']"

    def basic_info_save_button(self):
        """
        基本资料-保存按钮
        :return:
        """

        return "//span[text()='保存']/parent::button"