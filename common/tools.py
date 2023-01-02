# @Time:2022/12/27 12:31
# @Author:Henry
import datetime
import os


def get_now_time():
    return datetime.datetime.now()


def get_project_path():
    """
    获取项目绝对路径
    :return:
    """
    project_name = "CampusTrading-ui-autotest"
    file_path = os.path.dirname(__file__)
    # print(file_path)
    # print(file_path.find(project_name))
    # print(file_path[:file_path.find(project_name)+len(project_name)])

    return file_path[:file_path.find(project_name) + len(project_name)]


def sep(path, add_sep_before=False, add_sep_after=False):
    all_path = os.sep.join(path)

    if add_sep_before:
        all_path = os.sep+all_path
    if add_sep_after:
        all_path = all_path+os.sep
    print(all_path)
    return all_path

# 在新增二手商品中对添加图片做一个单独的处理
def get_img_path(img_name):
    """
    获取商品图片的路径
    :param img_name:
    :return:
    """

    img_dir_path = get_project_path() + sep(["img", img_name], add_sep_before=True)
    return img_dir_path

if __name__ == '__main__':
    # print(get_now_time())
    # print(get_project_path())
    sep(["config", "environment.yaml"],add_sep_before=True,add_sep_after=True)
    print(get_img_path("商品图片一.jpg"))