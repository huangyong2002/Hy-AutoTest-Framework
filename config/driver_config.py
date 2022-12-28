# @Time:2022/12/29 7:36
# @Author:Henry
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class DriverConfig:
    @staticmethod
    def driver_config():
        """
        浏览器驱动
        :return:
        """
        options = webdriver.ChromeOptions()
        options.add_argument("disable-infobars")
        # 设置窗口大小，设置为1920*1080
        options.add_argument("window-size=1920,1080")
        # 无头模式
        options.add_argument('--headless')
        # 解决卡顿
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sanbox")
        options.add_argument('--disable-dev-shm-usage')
        # 解决selenium无法访问https的问题
        options.add_argument("--ignore-certificate-errors")
        # 允许忽略localhost上的TLS/SSL错误
        options.add_argument("--allow-insecure-localhost")
        # 设置为无痕模式
        options.add_argument("--incognito")
        # 去除“Chrome正受到自动测试软件的控制”
        options.add_experimental_option(
            "excludeSwitches", ["enable-automation"]
        )
        # 实例化浏览器驱动
        driver = webdriver.Chrome(
            ChromeDriverManager(url="http://npm.taobao.org/mirrors/chromedriver",
                                latest_release_url="http://npm.taobao.org/mirrors/chromedriver/LATEST_RELEASE",
                                cache_valid_range=365).install(),
            options=options
        )
        # 隐性等待时间
        driver.implicitly_wait(3)
        # 删除所有cookies
        driver.delete_all_cookies()
        return driver


if __name__ == '__main__':
    DriverConfig().driver_config()
