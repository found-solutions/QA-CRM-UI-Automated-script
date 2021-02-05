from read_config import ReadConfig
from all_path import Paths
from selenium import webdriver
import unittest
from common.logs import MyLog
from common.operate_file import ExcelUtil
# from common.my_db import db
import time
from src.admin_portal.pages.page_login import PageLogin
import ddt

cf = ReadConfig()
log = MyLog.my_log().get_logger()

# 无头模式参数
selenium_option = webdriver.ChromeOptions()
selenium_option.add_argument('headless')
selenium_option.add_argument('--disable-gpu')
