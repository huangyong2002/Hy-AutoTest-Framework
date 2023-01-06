# @Time:2023/1/6 23:32
# @Author:Henry
import logging
import os.path
import time
from common.tools import get_project_path, sep


def get_log(logger_name):
    # 创建一个logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    # 设置日志存放路径，日志文件名
    # 获取本地时间
    rq = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
    # print(rq)

    # 设置日志存放路径
    all_log_path = get_project_path() + sep(["logs", "all_logs"], add_sep_before=True, add_sep_after=True)

    # 如果日志目录不存在就自动创建
    if not os.path.exists(all_log_path):
        os.makedirs(all_log_path)

    # 设置日志文件名
    all_log_name = all_log_path + rq + ".log"

    # 创建handler
    # 创建一个handler写入日志
    fh = logging.FileHandler(all_log_name)
    fh.setLevel(logging.INFO)

    # 定义日志输出格式
    all_log_formatter = logging.Formatter("%(asctime)s - %(module)s - %(funcName)s - %(lineno)d - %(message)s",
                                          datefmt="%Y-%m-%d %H:%M:%S")
    # 将定义好的输出形式添加到handler
    fh.setFormatter(all_log_formatter)

    # 给logger添加handler
    logger.addHandler(fh)
    return logger


log = get_log("自动化测试")

if __name__ == '__main__':
    # get_log("自动化测试")
    log.debug("I am debug message")
    log.info("I am info message")
    log.warning("I am warning message")
    log.error("I am error message")
    log.critical("I am critical message")