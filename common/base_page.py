from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from common.logs import MyLog
from all_path import Paths
from read_config import ReadConfig
from common.operate_file import find_file_abspath
import os
import time
import win32gui
import win32con


class BasePage(object):
    def __init__(self, selenium_driver):
        """
        初始化参数
        :param selenium_driver: 浏览器driver
        """
        self.driver = selenium_driver
        self.log = MyLog.my_log().get_logger()
        self.cf = ReadConfig()

    def _open(self, url_type):
        """
        用于打开浏览器，最大化浏览器，智能等待时间设置为30秒
        :param url_type: 1 admin portal； 2 member portal； other 自定义url
        :return:
        """
        try:
            if url_type == 1:
                self.driver.get(ReadConfig().get_url('admin_portal'))
                self.log.info('打开测试网址成功: ' + str(ReadConfig().get_url('admin_portal')))
            elif url_type == 2:
                self.driver.get(ReadConfig().get_url('member_portal'))
                self.log.info('打开测试网址成功：' + str(ReadConfig().get_url('member_portal')))
            else:
                self.driver.get(url_type)
                self.log.info('打开测试网址成功：' + str(url_type))
            self.driver.maximize_window()
            self.driver.implicitly_wait(20)
        except:
            self.log.error("未能正确打开页面：{}".format(url_type))
            raise

    def find_element(self, *loc):
        """
        查找元素
        :param loc:定位器，接收多种定位方式
        :return: 元素对象
        """
        try:
            WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(loc))
            WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            self.log.error("元素未找到：" + str(loc))
            raise

    def send_keys(self, value, *loc, clear=True):
        """
        重写输入的方法
        :param value: 要输入的内容
        :param clear: 判定是否要先清空输入框
        :param loc:
        :return:
        """
        try:
            if clear:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
                time.sleep(0.3)
            else:
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            self.log.error("输入失败:loc=" + str(loc) + "；value=" + value)
            raise

    def img_screen(self, img_name):
        """
        截图函数
        :param img_name: 保存图片的名字
        :return: None
        """
        try:
            self.driver.save_screenshot(os.path.join(Paths.error_img, '{}.png'.format(img_name)))
        except:
            self.log.error("截图失败：" + img_name)

    def select_value(self, *loc, index=None, texts=None, value=None):
        try:
            if index is not None:
                Select(self.find_element(*loc)).select_by_index(index)
            elif texts is not None:
                Select(self.find_element(*loc)).select_by_visible_text(texts)
            elif value is not None:
                Select(self.find_element(*loc)).select_by_value(value)
        except:
            self.log.error("下拉框选择失败：" + str(loc))
            raise

    def select_value_click(self, a, b):
        try:
            self.find_element(*a).click()
            time.sleep(0.5)
            self.find_element(*b).click()
            time.sleep(0.3)
        except:
            self.log.error("选择非标准的下拉框失败：" + str(a))
            raise

    def move_yzm(self, a, b):
        """
        验证码 滑动 ，
        :param a:  滑动按钮定位
        :param b:  滑动模块整体定位
        :return:
        """
        try:
            yzm = self.find_element(*a)
            yzm_back = self.find_element(*b)
            yzm_back_size = yzm_back.size
            action = ActionChains(self.driver)
            action.drag_and_drop_by_offset(yzm, yzm_back_size['width'], yzm_back_size['height']).perform()
            time.sleep(0.3)
        except Exception as e:
            self.log.error('验证码滑动失败：' + str(e))
            raise

    def scroll_window(self, y=10000):
        """
        移动浏览器滚动条到窗口指定位置 -- 浏览器自带的滚动条
        :param y:  指定位置，默认滚动到浏览器底部
        :return: None
        """
        try:
            js = 'document.documentElement.scrollTop={}'.format(y)
            self.driver.excute_script(js)
        except Exception as e:
            self.log.error('【浏览器滚动条】滚动失败[位置：{}]：{}'.format(y, str(e)))

    def upload_file(self, name):
        """
        windows上传文件文件窗口处理
        :param name:  需要上传的文件名称
        :return:
        """
        try:
            # exe_path = os.path.join(os.path.dirname(__file__), 'upload_file.exe')
            # command = '{} {}'.format(exe_path, find_file_abspath('data', name))
            # print('命令：', command)
            # os.system(command)

            dialog = win32gui.FindWindow("#32770", "打开")
            comboxex32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
            combox = win32gui.FindWindowEx(comboxex32, 0, "ComboBox", None)
            edit = win32gui.FindWindowEx(combox, 0, "Edit", None)
            button = win32gui.FindWindowEx(dialog, 0, "Button", "打开(&0)")
            win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, find_file_abspath('data', name))
            win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
        except Exception as e:
            self.log.error('上传文件【{}】失败：{}'.format(name, str(e)))
            raise

    def custom_scroll_window(self, *loc, y=100):
        """
        移动浏览器滚动条到窗口指定位置 -- 自定义的滚动条
        :param y: 位置
        :return:
        """
        try:
            action = ActionChains(self.driver)
            scroll_bar = self.find_element(*loc)
            action.move_to_element(scroll_bar)
            action.click_and_hold()
            action.move_by_offset(0, y)
            action.release()
            action.perform()
        except Exception as e:
            self.log.error('移动页面【自定义的滚动条】失败：' + str(e))

    def enter_down_key(self, n):
        """
        通过按键  ↓  实现滚动条滚动
        :param n: 按键次数
        :return:
        """
        try:
            ac = ActionChains(self.driver)
            for _ in range(n):
                ac.key_down(Keys.DOWN).perform()
                time.sleep(0.2)
        except Exception as e:
            self.log.error('键盘↓按失败：' + str(e))
