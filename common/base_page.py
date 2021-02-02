from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.select import Select
from common.logs import MyLog
from all_path import Paths
from read_config import ReadConfig
import os


class BasePage(object):
    def __init__(self, selenium_driver):
        """
        初始化参数
        :param selenium_driver: 浏览器driver
        """
        self.driver = selenium_driver
        self.url = ReadConfig().get_url('current_url')
        self.log = MyLog.my_log().get_logger()

    def _open(self):
        """
        用于打开浏览器，最大化浏览器，智能等待时间设置为30秒
        :return: None
        """
        try:
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.driver.implicitly_wait(30)
            self.log.info('打开测试网址成功.')
        except:
            self.log.error("未能正确打开页面：" + self.url)
            raise

    def find_element(self, *loc):
        """
        查找元素
        :param loc:定位器，接收多种定位方式
        :return: 元素对象
        """
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(loc))
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
