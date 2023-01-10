# @Time:2023/1/6 21:26
# @Author:Henry

from time import sleep
import allure


def add_img_2_report(driver, step_name, need_sleep=True):
    """
    截图并插入allure报告
    :param driver:
    :param step_name:
    :param need_sleep:
    :return:
    """
    if need_sleep:
        sleep(2)
    allure.attach(
        driver.get_screenshot_as_png(),  # 截图
        step_name + ".png",  # 测试步骤
        allure.attachment_type.PNG  # 附件名称
    )


def add_img_path_2_report(img_path, step_name):
    """
    将图片插入Allure报告
    :param imh_path:图片路径
    :param step_name:步骤名称
    :return:
    """
    allure.attach.file(img_path, step_name, allure.attachment_type.PNG)