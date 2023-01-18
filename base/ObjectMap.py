# @Time:2023/1/1 16:33
# @Author:Henry
# 存放selenium操作二次封装的方法
import datetime
import os.path
import time

from selenium.common.exceptions import ElementNotVisibleException, WebDriverException, NoSuchElementException, \
    StaleElementReferenceException

from common.find_img import FindImg
from common.tools import get_project_path,sep
from common.yaml_config import GetConf
from selenium.webdriver.common.keys import Keys
from common.report_add_img import add_img_path_2_report

class ObjectMap:
    # 获取基础地址：http://www.tcpjwtester.top
    url = GetConf().get_url()
    # locate_type,locate_expression定位表达式
    def element_get(self, driver, locate_type, locator_expression, timeout=10, must_be_visable=False):
        """
        单个元素获取
        :param driver:浏览器驱动 
        :param locate_type: 定位方式类别
        :param locator_expression: 定位表达式
        :param timeout: 超时时间
        :param must_be_visible:元素是否必须可见，True是必须可见，False是默认值 
        :return: 返回的元素
        """
        # 设置开始时间
        start_ms = time.time()
        print(start_ms)
        # 设置结束时间
        stop_ms = start_ms + (timeout * 1000)
        for x in range(int(timeout * 10)):
            # 查找元素
            try:
                element = driver.find_element(by=locate_type, value=locator_expression)
            # 如果元素不是必须可见的，就直接返回元素
                if not must_be_visable:
                    return element
            # 如果元素必须是可见的，则需要先判断元素是否可见
                else:
                    if element.is_dispayed():  # is_displayed判断元素是否可见的一个方法
                        return element
                    else:
                        raise Exception()
            except Exception:
                now_ms = time.time() * 1000
                if now_ms >= stop_ms:
                    break
                pass
            time.sleep(0.1)
        raise ElementNotVisibleException("元素定位失败，定位方式：" + locate_type + "定位表达式：" + locator_expression)

    def wait_for_ready_state_complete(self, driver, timeout=30):
        """
        等待页面完全加载成功
        :param driver: 浏览器驱动
        :param timeout: 超时时间
        :return:
        """
        # 设置开始时间
        start_ms = time.time() * 1000
        # 设置结束时间
        stop_ms = start_ms + (timeout * 1000)
        for x in range(int(timeout * 10)):
            try:
                # 获取页面的状态
                ready_state = driver.execute_script("reture document.readyState")
            except WebDriverException:
                # 如果有driver的错误，执行JS会失败，就直接跳过
                return True
            # 如果页面元素全部加载完成就返回True
            if ready_state == "complete":
                time.sleep(0.01)
                return True
            else:
                now_ms = time.time() * 1000
                # 如果超时了就break
                if now_ms >= stop_ms:
                    break
                time.sleep(0.1)
        raise Exception("打开网页是页面元素在%s秒后仍然没有完全加载完" % timeout)

    def element_disappear(self, driver, locate_type, locator_expression, timeout=30):
        """
        等待页面元素消失
        :param driver:浏览器驱动
        :param locate_type: 定位方式类型
        :param locator_expression: 定位表达式
        :param timeout: 超时时间
        :return:
        """
        if locate_type:
            # 开始时间
            start_ms = time.time() * 1000
            # 设置的结束时间
            stop_ms = start_ms + (timeout * 1000)
            for x in range(int(timeout * 10)):
                try:
                    element = driver.find_element(by=locate_type, value=locator_expression)
                    if element.is_displayed():
                        now_ms = time.time() * 1000
                        if now_ms >= stop_ms:
                            break
                        time.sleep(0.1)
                except Exception:
                    return True
            raise Exception("元素没有消失，定位方式：" + locate_type + "\n定位表达式：" + locator_expression)
        else:
            pass

    def element_appear(self, driver, locate_type, locator_expression, timeout=30):
        """
        等待页面元素出现
        :param driver:
        :param locate_type:
        :param locator_expression:
        :param timeout:
        :return:
        """
        if locate_type:
            # 开始时间
            start_ms = time.time() * 1000
            # 设置结束时间
            stop_ms = start_ms + (timeout * 1000)
            for x in range(int(timeout * 10)):
                try:
                    element = driver.find_element(by=locate_type, value=locator_expression)
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception()
                except Exception:
                    now_ms = time.time() * 1000
                    if now_ms >= stop_ms:
                        break
                    time.sleep(0.1)
                    pass
            raise ElementNotVisibleException(
                "元素没有出现，定位方式：" + locate_type + "定位表达式：" + locator_expression)
        else:
            pass

    def element_to_url(self,
                           driver,
                           url,
                           locate_type_disappear=None,
                           locator_expression_disappear=None,
                           locate_type_appear=None,
                           locator_expression_appear=None):
            """
            跳转地址
            :param driver: 浏览器驱动
            :param url: 跳转的地址
            :param locate_type_disappear:等待页面元素消失的定位方式
            :param locator_expression_disappear: 等待页面元素消失的定位表达式
            :param locate_type_appear:等待页面元素出现的定位方式
            :param locator_expression_appear:等待页面元素出现的定位表达式
            :return:
            """
            try:
                driver.get(self.url + url)
                # 等待页面元素加载完成
                self.wait_for_ready_state_complete(driver)
                # 跳转地址后等待元素消失
                self.element_disappear(driver,
                                       locate_type_disappear,
                                       locator_expression_disappear)
                # 跳转地址后等待元素出现
                self.element_appear(
                    driver,
                    locate_type_appear,
                    locator_expression_appear
                )
            except Exception as e:
                print("跳转地址出现异常，异常原因：%s" % e)
                return False
            return True

    def element_is_display(self, driver, locate_type, locator_experssion):
            """
            元素是否显示
            :param driver:
            :param locate_type:
            :param locator_experssion:
            :return:
            """
            try:
                driver.find_element(by=locate_type, value=locator_experssion)
                return True
            except NoSuchElementException:
                # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
                return False

    def element_fill_value(self, driver, locate_type, locator_expression, fill_value, timeout=30):
        """
        元素填值
        :param driver:浏览器驱动
        :param locate_type: 定位方式
        :param locator_expression: 定位表达式
        :param fill_value: 填入的值
        :param timeout: 超时时间
        :return:
        """

        # 元素必须先出现
        element = self.element_appear(
            driver,
            locate_type=locate_type,
            locator_expression=locator_expression,
            timeout=timeout
        )
        try:
            # 先清除元素中的原有值
            element.clear()
        except StaleElementReferenceException:  # 页面元素没有刷新出来，就对元素进行捕获，从而引发了这个异常
            self.wait_for_ready_state_complete(driver=driver)
            time.sleep(0.06)
            element = self.element_appear(
                driver,
                locate_type=locate_type,
                locator_expression=locator_expression,
                timeout=timeout
            )
            try:
                element.clear()
            except Exception:
                pass
        except Exception:
            pass
        # 填入值转成字符串
        if type(fill_value) is int or type(fill_value) is float:
            fill_value = str(fill_value)
        try:
            # 填入的值不是以\n结尾
            if not fill_value.endswith("\n"):  # 如果结尾是以\n
                element.send_keys(fill_value)
                self.wait_for_ready_state_complete(driver=driver)
            else:
                fill_value = fill_value[:-1]
                element.send_keys(fill_value)
                element.send_keys(Keys.RETURN)
                self.wait_for_ready_state_complete(driver=driver)
        except StaleElementReferenceException:
            self.wait_for_ready_state_complete(driver=driver)
            time.sleep(0.06)
            element = self.element_appear(driver, locate_type=locate_type, locator_expression=locator_expression)
            element.clear()
            # 填入的值不是以\n结尾
            if not fill_value.endswith("\n"):  # 如果结尾是以\n
                element.send_keys(fill_value)
                self.wait_for_ready_state_complete(driver=driver)
            else:
                fill_value = fill_value[:-1]
                element.send_keys(fill_value)
                element.send_keys(Keys.RETURN)
                self.wait_for_ready_state_complete(driver=driver)
        except Exception:
            raise Exception("元素填值失败")

        return True

    def element_click(self,
                      driver,
                      locate_type,
                      locator_expression,
                      locate_type_disappear=None,
                      locator_expression_disappear=None,
                      locate_type_appear=None,
                      locator_expression_appear=None,
                      timeout=30
                      ):
        """
        元素点击
        :param driver: 浏览器驱动
        :param locate_type: 定位方式类型
        :param locator_expression: 定位表达式
        :param locate_type_disappear: 等待元素消失的定位方式类型
        :param locator_expression_disappear: 等待元素消失的定位表达式
        :param locate_type_appear: 等待元素出现的定位方式类型
        :param locator_expression_appear: 等待元素出现的定位表达式
        :param timeout:
        :return:
        """

        # 元素要可见
        element = self.element_appear(
            driver=driver,
            locate_type=locate_type,
            locator_expression=locator_expression,
            timeout=timeout
        )
        try:
            # 点击元素
            element.click()
        except StaleElementReferenceException:
            self.wait_for_ready_state_complete(driver=driver)
            time.sleep(0.06)
            # 元素要可见
            element = self.element_appear(
                driver=driver,
                locate_type=locate_type,
                locator_expression=locator_expression,
                timeout=timeout
            )
            element.click()
        except Exception as e:
            print("页面出现异常，元素不可点击", e)
            return False
        try:
            # 点击元素后的元素出现或消失
            self.element_appear(
                driver,
                locate_type_appear,
                locator_expression_appear
            )
            self.element_disappear(
                driver,
                locate_type_disappear,
                locator_expression_disappear
            )
        except Exception as e:
            print("等待元素消失或出现失败", e)
            return False

        return True

    def upload(self,driver,locate_type,locator_expression,file_path):
        """
        文件上传
        :param driver:
        :param locate_type:
        :param locator_expression:
        :param file_path:
        :return:
        """
        element = self.element_get(driver,locate_type,locator_expression)
        return element.send_keys(file_path)


    def switch_into_iframe(self, driver, locate_iframe_type, locate_iframe_expression):
        """
        进入iframe
        :param driver:浏览器驱动
        :param locate_type: 定位iframe方式
        :param locate_iframe_expression: 定位iframe的表达式
        :return:
        """
        iframe = self.element_get(driver, locate_iframe_type, locate_iframe_expression)
        driver.switch_to.frame(iframe)

    def switch_from_iframe_to_content(self, driver):
        """
        从iframe切回主文档
        :param driver:
        :return:
        """
        driver.switch_to.parent_frame()

    def find_img_in_source(self, driver, img_name):
        """
        截图，并在截图中查找图片
        :param driver:
        :param img_name:
        :return:
        """

        # 截图后图片保存的路径
        source_img_path = get_project_path() + sep(["img", "source_img", img_name], add_sep_before=True)
        # 需要查找的图片路径
        search_img_path = get_project_path() + sep(["img", "assert_img", img_name], add_sep_before=True)
        # 截图并保存图片
        driver.get_screenshot_as_file(source_img_path)
        time.sleep(3)
        add_img_path_2_report(source_img_path, "原图")
        add_img_path_2_report(search_img_path, "需要查找的图片")
        # 在原图中查找是否有指定的图片，返回信心值
        confidence = FindImg().get_confidence(source_img_path, search_img_path)
        return confidence

    def element_screenshot(self, driver, locate_type, locator_expression):

        """
        元素截图
        :param driver:
        :param locate_type:
        :param locator_expression:
        :return:
        """
        ele_name = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".png"
        ele_img_dir_path = get_project_path() + sep(["img", "ele_img"], add_sep_before=True, add_sep_after=True)
        if not os.path.exists(ele_img_dir_path):
            os.makedirs(ele_img_dir_path)
        ele_img_path = ele_img_dir_path + ele_name
        self.element_get(driver, locate_type, locator_expression).screenshot(ele_img_path)
        return ele_img_path

    # 滚动到元素的方法
    def scroll_to_element(self, driver, locate_type, locator_expression):
        """
        滚动到元素
        :param driver:
        :param locate_type:
        :param locator_expression:
        :return:
        """
        ele = self.element_get(driver, locate_type, locator_expression)
        driver.execute_script("arguments[0].scrollIntoView()", ele)
        return True

# if __name__ == '__main__':
#     ObjectMap().element_get()
