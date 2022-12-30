# @Time:2022/12/30 9:31
# @Author:Henry
from base.LoginBase import LoginBase
class LoginPage(LoginBase):
    def login_input_value(self,driver,input_placeholder,input_value):
        """
        登录页输入
        :param driver:
        :param input_placeholder:
        :param input_value:
        :return:
        """
        input_xpath = self.login_input(input_placeholder)
        return driver.find_element_by_xpath(input_xpath).send_keys(input_value)

    def click_login(self,driver,button__name):
        """
        点击登录
        :param driver:
        :param button__name:
        :return:
        """
        button__xpath = self.login_button(button__name)
        return driver.find_element_by_xpath(button__xpath).click()
