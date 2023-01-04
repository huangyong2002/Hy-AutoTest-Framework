# @Time:2023/1/4 21:31
# @Author:Henry
import aircv as ac

from common.tools import get_project_path, sep


class FindImg:

    def img_imread(self, img_path):
        """
        读取图片
        :param img_path:
        :return:
        """

        return ac.imread(img_path)

    def get_confidence(self, source_path, search_path):
        """
        查找图片
        :param source_path:原图路径
        :param search_path: 需要查找的图片的路径
        :return:
        """
        img_src = self.img_imread(source_path)
        img_sch = self.img_imread(search_path)
        result = ac.find_template(img_src, img_sch)
        print(result)
        return result["confidence"]

if __name__ == '__main__':
    source_path = get_project_path() + sep(["img", "source.png"], add_sep_before=True)
    search_path = get_project_path() + sep(["img", "search.png"], add_sep_before=True)

    FindImg().get_confidence(source_path, search_path)