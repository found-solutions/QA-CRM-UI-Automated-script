from common.operate_file import ExcelUtil
from read_config import ReadConfig
from selenium import webdriver
from common.logs import MyLog
# from common.my_db import db
from all_path import Paths
import unittest
import time
import ddt
from src.member_portal.pages.page_register import PageRegister


cf = ReadConfig()
log = MyLog.my_log().get_logger()

# 无头模式参数
selenium_option = webdriver.ChromeOptions()
selenium_option.add_argument('headless')
selenium_option.add_argument('--disable-gpu')
