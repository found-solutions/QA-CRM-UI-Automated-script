from common.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class PageDashboard(BasePage):
    dashboard_menu = (By.XPATH, "//span[text()='Dashboard']")
    # 添加真实账号
    add_live_account_bt = (By.XPATH, "//span[text()='Live Account Application']")
    agent_select = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/div/div/section/div[1]/div[2]/div/div/div[1]/div/div/input')
    agent_select_value = (By.XPATH, "/html/body/div[7]/div[1]/div[1]/ul/li[1]")
    ts_select = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/div/div/section/div[1]/div[2]/div/div/div[3]/div/div/input')
    ts_select_value = (By.XPATH, "/html/body/div[8]/div[1]/div[1]/ul/li[1]")
    node_select = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/div/div/section/div[1]/div[2]/div/div/div[5]/div[1]/div/input')
    node_select_value = (By.XPATH, "/html/body/div[9]/div[1]/div[1]/ul/li[1]")
    leverage_select = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/div/div/section/div[1]/div[2]/div/div/div[5]/div[2]/div/input')
    leverage_select_value = (By.XPATH, "/html/body/div[10]/div[1]/div[1]/ul/li[1]")
    trading_pwd = (By.NAME, "master_password")
    trading_pwd_conf = (By.NAME, "master_password_confirmation")
    invest_password = (By.NAME, 'invest_password')
    invest_password_conf = (By.NAME, 'invest_password_confirmation')
    hub_pin = (By.NAME, 'hub_password')
    hub_pin_conf = (By.NAME, 'hub_password_confirmation')
    note_input = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/div/div/section/div[1]/div[2]/div/div/div[11]/div/input')
    submit_bt = (By.XPATH, '//button[text()="SUBMIT"]')

    # 添加demo账号
    add_demo_account_bt = (By.XPATH, "//span[text()='Demo Account Application']")
    demo_ts_select = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/div/div/section/div[1]/div[2]/div/div/div/form/div[1]/div/div/div/input')
    demo_ts_select_value = (By.XPATH, '/html/body/div[7]/div[1]/div[1]/ul/li')
    demo_account_type_select = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/div/div/section/div[1]/div[2]/div/div/div/form/div[2]/div/div/div/input')
    demo_account_type_select_value = (By.XPATH, '/html/body/div[8]/div[1]/div[1]/ul/li')
    demo_leverage_select = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/div/div/section/div[1]/div[2]/div/div/div/form/div[3]/div/div/div[1]/input')
    demo_leverage_select_value = (By.XPATH, '/html/body/div[9]/div[1]/div[1]/ul/li')
    demo_currency_select = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/div/div/section/div[1]/div[2]/div/div/div/form/div[4]/div/div/div[1]/input')
    demo_currency_select_value = (By.XPATH, '/html/body/div[10]/div[1]/div[1]/ul/li')
    demo_deposit_select = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/div/div/section/div[1]/div[2]/div/div/div/form/div[5]/div/div/div[1]/input')
    demo_deposit_select_value = (By.XPATH, '/html/body/div[11]/div[1]/div[1]/ul/li')
    demo_trading_pwd = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/div/div/section/div[1]/div[2]/div/div/div/form/div[8]/div/div/input')
    demo_submit_bt = (By.XPATH, '//button[text()="SUBMIT"]')

    # 修改 live account 的 trading pwd
    l_setting_bt = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[1]/div[2]/div[2]/div[3]/table/tbody/tr[2]/td[14]/div/i')
    l_pwd = (By.NAME, 'password')
    l_update = (By.XPATH, '//button[text()="UPDATE"]')
    l_yes = (By.XPATH, "//button[text()='YES']")
    l_tip = (By.XPATH, "/html/body/div[7]/p")
    #

    # 修改 demo account 的 pwd
    d_setting_bt = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[1]/div[2]/div[4]/div[3]/table/tbody/tr[2]/td[13]/div/i')
    d_new_pwd = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/div/div/section/div[1]/div[2]/div/div/div/form/div[2]/div/div/input')
    d_submit_bt = (By.XPATH, '//button[text()="SUBMIT"]')
    d_yes = (By.XPATH, "//button[text()='YES']")
    d_tip = (By.XPATH, "/html/body/div[7]/p")


    def add_live_account(self, trade_pwd, invest_pwd, pin, note):
        self.find_element(*self.add_live_account_bt).click()
        self.log.info('点击【添加真实账号】')
        self.select_value_click(self.agent_select, self.agent_select_value)
        self.log.info('选择agent：')
        self.select_value_click(self.ts_select, self.ts_select_value)
        self.log.info('选择ts：')
        self.select_value_click(self.node_select, self.node_select_value)
        self.log.info('选择node：')
        self.select_value_click(self.leverage_select, self.leverage_select_value)
        self.log.info('选择leverage：')
        self.send_keys(trade_pwd, *self.trading_pwd)
        self.log.info('输入trade pwd：' + trade_pwd)
        self.send_keys(trade_pwd, *self.trading_pwd_conf)
        self.log.info('输入二次trade pwd：' + trade_pwd)
        self.send_keys(invest_pwd, *self.invest_password)
        self.log.info('输入invest_pwd：' + invest_pwd)
        self.send_keys(invest_pwd, *self.invest_password_conf)
        self.log.info('输入二次invest_pwd：' + invest_pwd)
        self.send_keys(pin, *self.hub_pin)
        self.log.info('输入pin：' + pin)
        self.send_keys(pin, *self.hub_pin_conf)
        self.log.info('输入二次pin：' + pin)
        self.send_keys(note, *self.note_input)
        self.log.info('输入note：' + note)
        self.find_element(*self.submit_bt).click()
        self.log.info('点击【提交】按钮')

    def add_demo_account(self, pwd):
        self.select_value_click(self.demo_ts_select, self.demo_ts_select_value)
        self.log.info('点击【添加demo账号】')
        self.select_value_click(self.demo_account_type_select, self.demo_account_type_select_value)
        self.log.info('选择account_type：')
        self.select_value_click(self.demo_leverage_select, self.demo_leverage_select_value)
        self.log.info('选择leverage：')
        self.select_value_click(self.demo_currency_select, self.demo_currency_select_value)
        self.log.info('选择currency：')
        self.select_value_click(self.demo_deposit_select, self.demo_deposit_select_value)
        self.log.info('选择deposit：')
        self.send_keys(pwd, *self.demo_trading_pwd)
        self.log.info('输入pwd：' + pwd)
        self.find_element(*self.demo_submit_bt).click()
        self.log.info('点击【提交】按钮')

    def update_live_account_trade_pwd(self, new_pwd):
        self.find_element(*self.l_setting_bt).click()
        self.log.info('点击【设置live】按钮')
        self.send_keys(new_pwd, *self.l_pwd)
        self.log.info('输入新密码：' + new_pwd)
        self.find_element(*self.l_update).click()
        self.log.info('点击【更新】按钮')
        self.find_element(*self.l_yes).click()
        self.log.info('点击【确认】按钮')

    def update_demo_pwd(self, new_pwd):
        self.find_element(*self.d_setting_bt).click()
        self.log.info('点击【设置demo】按钮')
        self.send_keys(new_pwd, self.d_new_pwd)
        self.log.info('输入新密码：' + new_pwd)
        self.find_element(*self.d_submit_bt).click()
        self.log.info('点击【提交】按钮')
        self.find_element(*self.d_yes).click()
        self.log.info('点击【确认】按钮')

    def get_add_live_tip(self):
        pass

    def get_add_demo_tip(self):
        pass

    def get_update_live_tip(self):
        tip = self.find_element(*self.l_tip).text
        return tip

    def get_update_demo_tip(self):
        tip = self.find_element(*self.d_tip).text
        return tip














































































