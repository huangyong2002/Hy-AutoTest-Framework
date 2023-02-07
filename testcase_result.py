# @Time:2023/2/7 14:54
# @Author:Henry

from common.ding_talk import send_dingtalk_msg_markdown
from common.yaml_config import GetConf

# 项目名称
project_name = "Hy-UiTest-Framework"
# 报告标题
report_title = "UI自动化测试-测试报告"
# jenkins地址
jenkins_url = GetConf().get_jenkins()["url"]
# allure测试报告地址
allure_url = jenkins_url + "/job/" + project_name + "/allure/"
# 发送报告到钉钉
dingding_webhook = GetConf().get_dingding_webhook()
send_dingtalk_msg_markdown(
    dingding_webhook,
    allure_url,
    report_title
)