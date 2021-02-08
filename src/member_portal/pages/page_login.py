from common.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class PageLogin(BasePage):
    email_input = (By.XPATH, "//input[@aria-label='Email']")
    pwd_input = (By.XPATH, "//input[@aria-label='Password']")
    login_button = (By.XPATH, "//button[text()='LOGIN']")
    tips = (By.XPATH, "//p[@class='el-message__content']")

    def my_login(self, email='auto@gmail.com', pwd='Auto1234'):
        self.send_keys(email, *self.email_input)
        self.log.info('输入email：' + email)
        self.send_keys(pwd, *self.pwd_input)
        self.log.info('输入密码：' + pwd)
        self.find_element(*self.login_button).click()
        self.log.info('点击【登录】按钮')
        time.sleep(0.5)

    def get_home_title(self):
        title = self.driver.title
        return title

    def get_tip(self):
        tip = self.find_element(*self.tips).text
        return tip
