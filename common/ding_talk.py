# @Time:2023/2/4 20:44
# @Author:Henry

import requests
from common.yaml_config import GetConf
from common.tools import get_every_wallpaper


def send_dingtalk_msg(webhook, content):
    """
    发送钉钉消息-text
    :param webhook:
    :param content:
    :return:
    """
    headers = {"Content-Type": "application/json ;charset=utf-8"}
    data = {
        "msgtype": "text",
        "text": {"content": content, "at": {"isAtAll": False}}
    }
    res = requests.post(url=webhook, json=data, headers=headers)
    print("发送钉钉消息，返回结果:", res.text)

def send_dingtalk_msg_markdown(
        ding_webhook,
        allure_url,
        report_title
):
    """
    发送markdown格式的消息到钉钉
    :param ding_webhook: 钉钉群的webhook
    :param allure_url: allure地址
    :param report_title: 报告标题
    :return:
    """
    # 获取壁纸
    wallpaper_url = get_every_wallpaper()
    headers = {"Content-Type": "application/json ;charset=utf-8"}
    data = {
        "msgtype": "markdown",
        "markdown": {
            "title": report_title,
            "text": "#### "
                    + report_title
                    + " \n >   ![每日壁纸]({})\n> ###### 点击查看测试报告 \n>  [Allure测试报告]({})".format(
                wallpaper_url,
                allure_url,
            ),
        },
    }
    res = requests.post(url=ding_webhook, json=data, headers=headers)
    print("发送钉钉消息，返回结果:", res.text)

if __name__ == '__main__':
    webhook=GetConf().get_dingding_webhook()
    send_dingtalk_msg(webhook, "自动化测试")
