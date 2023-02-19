# @Time:2023/1/4 21:31
# @Author:Henry
import aircv as ac

from common.tools import get_project_path, sep, get_now_date_time_str
import cv2
from common.report_add_img import add_img_path_2_report

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
        # 在原图上根据找到的坐标画框,rectangle可以再图片上绘制一个简单的矩形
        cv2.rectangle(
            img_src, result["rectangle"][0], result["rectangle"][3], (255, 0, 0), 2
        )
        # 获取到画框图片的路径
        diff_img_path = get_project_path() + sep(["img", "diff_img", get_now_date_time_str() + "-对比的图.png"],
                                                 add_sep_before=True)
        # 保存
        cv2.imencode(".png", img_src)[1].tofile(diff_img_path)
        # 加入测试报告
        add_img_path_2_report(diff_img_path, "查找到的图")
        return result["confidence"]


if __name__ == '__main__':
    source_path = get_project_path() + sep(["img", "source_img", "head_img.png"], add_sep_before=True)
    search_path = get_project_path() + sep(["img", "assert_img", "head_img.png"], add_sep_before=True)
    FindImg().get_confidence(source_path, search_path)