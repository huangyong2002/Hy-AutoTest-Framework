# @Time:2022/12/30 9:31
# @Author:Henry
from time import sleep
from page.LoginPage import LoginPage
from config.driver_config import DriverConfig
class TestLogin:

    def test_login(self):
        driver = DriverConfig().driver_config()
        driver.get("http://www.tcpjwtester.top")
        sleep(3)
        LoginPage().login_input_value(driver, "用户名", "周杰伦")
        sleep(1)
        LoginPage().login_input_value(driver, "密码", "123456")
        sleep(1)
        LoginPage().click_login(driver, "登录")
        sleep(3)
        driver.quit()