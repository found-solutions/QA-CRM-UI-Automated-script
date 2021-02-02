from read_config import ReadConfig
from all_path import Paths
from selenium import webdriver
import unittest
from common.logs import MyLog
from common.operate_file import ExcelUtil
# from common.my_db import db
import time
from src.pages.page_login import PageLogin
import ddt

cf = ReadConfig()
log = MyLog.my_log().get_logger()
