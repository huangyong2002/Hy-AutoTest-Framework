# @Time:2023/1/2 22:26
# @Author:Henry
class IframeBaiduMapBase:

    def search_button(self):
        return "//button[@id='search-button']"

    def baidu_map_iframe(self):
        return "//iframe[@src='https://map.baidu.com/']"
