from common.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class PageLogin(BasePage):
    login_type_button = (By.XPATH, "//*[text()='Default Login Method']")
    name_input = (By.XPATH, "//*[@placeholder='Login Name']")
    pwd_input = (By.XPATH, "//*[@placeholder='Password']")
    login_button = (By.XPATH, "//*[@type='submit']")
    user_none_tip = (By.XPATH, "//*[@id='app']/div/div[2]/form/div[1]/div/div[2]")
    password_none_tip = (By.XPATH, "//*[@id='app']/div/div[2]/form/div[2]/div/div[2]")

    def click_login_type(self):
        self.find_element(*self.login_type_button).click()
        self.log.info('点击登录类型。')

    def login(self, user, pwd):
        self.send_keys(user, *self.name_input)
        self.log.info('输入用户名：{}'.format(user))
        self.send_keys(pwd, *self.pwd_input)
        self.log.info('输入密码：{}'.format(pwd))
        self.find_element(*self.login_button).click()
        self.log.info('点击登录按钮')
        time.sleep(4)

    def get_home_title(self):
        title = self.driver.title
        return title

    def get_none_user_tip(self):
        t = self.find_element(*self.user_none_tip).text
        return t

    def get_none_pwd_tip(self):
        t = self.find_element(*self.password_none_tip).text
        return t


