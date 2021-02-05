from common.base_page import BasePage
from selenium.webdriver.common.by import By


class PageGodUser(BasePage):
    user_management_menu = (By.XPATH, "//*[@class='header-menu']/a[8]")
    sub_god_user_menu = (By.XPATH, "//*[text()='God User']")
    add_god_user_bt = (By.XPATH, "//*[@id='app']/div/section/main/section/div[1]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div/div/i")
    login_name_input = (By.XPATH, "//*[@id='app']/div/section/main/section/div[1]/div[2]/div/div/div/section/div[1]/form/div[1]/div[1]/div/div/div/input")
    name_input = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[1]/div[2]/div/div/div/section/div[1]/form/div[2]/div[1]/div/div/div/input')
    email_input = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[1]/div[2]/div/div/div/section/div[1]/form/div[3]/div[1]/div/div/div/input')
    pwd = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[1]/div[2]/div/div/div/section/div[1]/form/div[5]/div[1]/div/div/div/input')
    en_pwd = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[1]/div[2]/div/div/div/section/div[1]/form/div[6]/div[1]/div/div/div/input')
    create_bt = (By.XPATH, "//*[text()=' CREATE ']")
    tips = (By.XPATH, "/html/body/div[4]/p")

    def into_god_user_page(self):
        self.find_element(*self.user_management_menu).click()
        self.log.info('点击user management菜单')
        self.find_element(*self.sub_god_user_menu).click()
        self.log.info('点击god user子菜单')

    def add_god_user(self, login_name, name, email, pwd):
        self.find_element(*self.add_god_user_bt).click()
        self.log.info('点击添加god user按钮')
        self.send_keys(login_name, *self.login_name_input)
        self.log.info('输入登录名: ', login_name)
        self.send_keys(name, *self.name_input)
        self.log.info('输入name：{}', name)
        self.send_keys(email, *self.email_input)
        self.log.info('输入email：{}', email)
        self.send_keys(pwd, *self.pwd)
        self.log.info('输入pwd：{}', pwd)
        self.send_keys(pwd, *self.en_pwd)
        self.log.info('输入确认密码：{}', pwd)
        self.find_element(*self.create_bt).click()
        self.log.info('点击create按钮')

    def get_tip(self):
        tip = self.find_element(*self.tips).text
        return tip






