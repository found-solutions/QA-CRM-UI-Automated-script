from common.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class PageRegister(BasePage):
    register_bt = (By.XPATH, "//a[text()='sign up']")
    step_4_scroll_bt = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[4]/div')
    # step1
    first_name_input = (By.XPATH, "//input[@aria-label='First Name-en *']")
    middle_name_input = (By.XPATH, "//input[@aria-label='Middle Name-en']")
    last_name_input = (By.XPATH, "//input[@aria-label='Last Name-en *']")
    email_input = (By.XPATH, "//input[@aria-label='Email *']")
    country_select = (By.XPATH, '//*[@id="app"]/div/section/div[2]/div/div[2]/form/label[5]/div/div[1]/div[3]/i')
    country_select_value = (By.XPATH, '//div[text()="{}"]')

    mobile_input = (By.XPATH, "//input[@aria-label='Mobile Number *']")
    # //*[@id="app"]/div/section/div[2]/div/div[2]/form/label[8]/div/div[1]/div[1]/input
    pwd_input = (By.XPATH, '//*[@id="app"]/div/section/div[2]/div/div[2]/form/label[8]/div/div[1]/div[1]/input')
    pwd_2_input = (By.XPATH, "//input[@aria-label='Confirm Password *']")
    yzm = (By.XPATH, "//*[@id='nc_1_n1z']")
    yzm_back = (By.XPATH, '//*[@id="nc_1__scale_text"]/span')
    next1 = (By.XPATH, "//*[@id='app']/div/section/div[2]/div/div[3]/button")

    # 异常场景各种提示tip
    blacklist_country_tip = (By.XPATH, '//*[@id="app"]/div/section/div[2]/div/div[2]/form/label[5]/div/div[2]/div/div')
    email_tip = (By.XPATH, '//*[@id="app"]/div/section/div[2]/div/div[2]/form/label[4]/div/div[2]/div/div')
    password_tip = (By.XPATH, '//*[@id="app"]/div/section/div[2]/div/div[2]/form/label[8]/div/div[2]/div/div')

    # step2
    birth_input_button = (By.XPATH, "//input[@aria-label='Date of Birth *']")
    year = (By.XPATH, "//*[text()='2000']")
    month = (By.XPATH, "//*[text()='Jan']")
    day = (By.XPATH, "//*[text()='15']")
    ok_button = (By.XPATH, "//span[text()='OK']")

    address_input = (By.XPATH, "//input[@aria-label='Address *']")
    city_input = (By.XPATH, "//input[@aria-label='City *']")
    state_input = (By.XPATH, "//input[@aria-label='State *']")
    post_code_input = (By.XPATH, "//input[@aria-label='Postcode *']")
    gender_select = (By.XPATH, "//*[@id='app']/div/section/main/section/div[2]/div[2]/section/div[2]/div/div/div[2]/form/div[1]/label[6]/div")
    gender_select_value = (By.XPATH, "//*[text()='Male']")
    # crm配置开启认证才有
    # ------------------------------------------------------------------------------
    electronic_select = (By.XPATH, "//*[@id='app']/div/section/main/section/div[2]/div[2]/section/div[2]/div/div/div[2]/form/div[2]/label/div")
    electronic_select_value = (By.XPATH, "/html/body/div[5]/div[2]/div[6]/div[2]/div")
    id_number_input = (By.XPATH, "//input[@aria-label='ID Number *']")
    title_select = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/section/div[2]/div/div/div[2]/form/div[2]/label[3]/div')
    title_select_value = (By.XPATH, "//*[text()='Mr.']")
    first_input = (By.XPATH, "//input[@aria-label='First Name *']")
    last_input = (By.XPATH, "//input[@aria-label='Last Name *']")
    # ------------------------------------------------------------------------------
    # next2 = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/section/div[2]/div/div/div[2]/div/button')
    next2 = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/section/div[2]/div/div/div[2]/div/button')
    upload_id = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/section/div[2]/div/div/div[2]/form/div[2]/div[3]/div[1]/div/div/div/div')
    upload_proof = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/section/div[2]/div/div/div[2]/form/div[2]/div[3]/div[3]/div/div/div/div')
    id_card_input = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/section/div[2]/div/div/div[2]/form/div[2]/div[3]/div[1]/div/div/div/input')

    # step3
    question1_checkbox = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/section/div[2]/div/div/div[3]/form/div/div[2]/div/div[1]/div[1]/div')
    next3 = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/section/div[2]/div/div/div[3]/div/button')

    # step4
    account_type_select1 = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/section/div[2]/div/div/div[4]/form/div[1]/div/div[2]/label/div')
    account_type_select1_value = (By.XPATH, '//*[text()="fefe"]')
    currency_select = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/section/div[2]/div/div/div[4]/form/div[1]/div/div[3]/label/div')
    currency_select_value = (By.XPATH, "//*[text()='USD']")
    leverage_select = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/section/div[2]/div/div/div[4]/form/div[2]/label/div')
    leverage_select_value = (By.XPATH, "//*[text()='1:10']")
    trade_password = (By.XPATH, "//input[@aria-label='Password *']")
    trade_2_password = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/section/div[2]/div/div/div[4]/form/div[3]/div[2]/label/div/div[1]/div[1]/input')
    investor_password = (By.XPATH, "//input[@aria-label='Investor Password *']")
    investor_2_password = (By.XPATH, "//*[@id='app']/div/section/main/section/div[2]/div[2]/section/div[2]/div/div/div[4]/form/div[4]/div[2]/label/div/div[1]/div[1]/input")
    note_input = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/section/div[2]/div/div/div[4]/form/div[5]/label/div/div/div/input')
    auth1 = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/section/div[2]/div/div/div[4]/form/div[7]/div[1]/div[1]/div')
    auth2 = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/section/div[2]/div/div/div[4]/form/div[7]/div[2]/div[1]/div')
    submit = (By.XPATH, '//*[text()="SUBMIT"]')

    # demo step2
    ts_select = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/section/div[2]/form/div[1]/label/div')
    # Trading Server-en *
    ts_select_value = (By.XPATH, '//*[text()="MT4 demo-tm_demo_demo_ts"]')
    account_type_select = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/section/div[2]/form/div[2]/label/div')
    # Account Type-en *
    account_type_select_value = (By.XPATH, '//*[text()="test55-en"]')
    account_leverage_select = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/section/div[2]/form/div[3]/label/div/div/div[1]')
    account_leverage_select_value = (By.XPATH, '//*[text()="1:10"]')
    account_currency_select = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/section/div[2]/form/div[4]/div[1]/label/div/div/div[1]')
    account_currency_select_value = (By.XPATH, '//*[text()="AUD"]')
    deposit_select = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/section/div[2]/form/div[4]/div[2]/label/div/div/div[1]')
    deposit_select_value = (By.XPATH, '//*[text()="1500.22"]')
    td_pwd = (By.XPATH, '//*[@aria-label="Password *"]')
    td_2_pwd = (By.XPATH, '//*[@aria-label="Confirm Password"]')
    demo_submit = (By.XPATH, '//div[text()="SUBMIT"]')
    tips = (By.XPATH, "/html/body/div[5]/p")

    # 首页两个按钮 关闭弹窗 跳转注册完善资料
    close_pop_window_button = (By.XPATH, "//button[text()='CLOSE']")
    continue_button = (By.XPATH, "//button[text()='CONTINUE']")
    progress = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/section/div[2]/div/div/div[1]/div[3]/span[2]')

    def go_to_register(self):
        self.find_element(*self.register_bt).click()
        self.log.info('点击【注册】按钮')
        time.sleep(2.2)

    def register_step1(self, fn, mn, ln, email, country, phone, pwd, is_submit=1, sleep=10):
        """
        pass
        :param fn:
        :param mn:
        :param ln:
        :param email:
        :param country:
        :param phone:
        :param pwd:
        :param is_submit:  用于判断是否需要滑动验证码和点击下一步按钮，第一步异常场景不需要点击下一步按钮
        :param sleep: 点击 提交按钮 后， 休眠的时间， 默认 15S
        :return:
        """
        self.send_keys(fn, *self.first_name_input)
        self.log.info('输入first name：' + fn)
        self.send_keys(mn, *self.middle_name_input)
        self.log.info('输入middle name：' + mn)
        self.send_keys(ln, *self.last_name_input)
        self.log.info('输入last name：' + ln)
        self.send_keys(email, *self.email_input)
        self.log.info('输入email：' + email)
        # ----------------------- 选择指定名称的国家 -----------------------------
        c = list(self.country_select_value)
        c[1] = c.__getitem__(1).format(country)
        self.select_value_click(self.country_select, tuple(c))
        self.log.info('选择国家：' + country)
        # ---------------------------------------------------------------------
        self.send_keys(phone, *self.mobile_input)
        self.log.info('输入phone：' + phone)
        self.send_keys(pwd, *self.pwd_input)
        self.log.info('输入pwd：' + pwd)
        self.send_keys(pwd, *self.pwd_2_input)
        self.log.info('输入确认密码：' + pwd)
        time.sleep(0.8)
        # 异常场景 是否需要 点击提交 按钮，
        if is_submit == 1:
            self.move_yzm(self.yzm, self.yzm_back)
            self.log.info('滑动验证码')
            time.sleep(0.8)
            self.find_element(*self.next1).click()
            self.log.info('点击step1【下一步】按钮')
            time.sleep(sleep)

    def register_step2(self, address, city, state, postcode, id_number, first_name, last_name, id_card_name, c):
        self.find_element(*self.birth_input_button).click()
        time.sleep(0.2)
        self.log.info('点击birth日期控件')
        self.find_element(*self.year).click()
        time.sleep(0.2)
        self.log.info('点击 年份')
        self.find_element(*self.month).click()
        time.sleep(0.2)
        self.log.info('点击 月份')
        self.find_element(*self.day).click()
        time.sleep(0.2)
        self.log.info('点击 day')
        self.send_keys(address, *self.address_input)
        self.log.info('输入address：' + address)
        self.send_keys(city, *self.city_input)
        self.log.info('输入city：' + city)
        self.send_keys(state, *self.state_input)
        self.log.info('输入state：' + state)
        self.send_keys(postcode, *self.post_code_input)
        self.log.info('输入postcode：' + postcode)
        self.select_value_click(self.gender_select, self.gender_select_value)
        self.log.info('选择gender en： Mail')
        # 通过国家判断是不是需要认证， 仅配置中国需要认证
        if c == 'China':
            self.select_value_click(self.electronic_select, self.electronic_select_value)
            self.log.info('选择电子身份证： 中国身份证')
            self.send_keys(id_number, *self.id_number_input)
            self.log.info('输入id_number：' + id_number)
            self.select_value_click(self.title_select, self.title_select_value)
            self.log.info('选择 title： Mr.')
            self.send_keys(first_name, *self.first_input)
            self.log.info('输入first_name：' + first_name)
            self.send_keys(last_name, *self.last_input)
            self.log.info('输入last_name：' + last_name)
            self.find_element(*self.next2).click()
            self.log.info('点击step2【下一步】按钮')
            # 验证 身份证 信息， 等待时间要长一点
            time.sleep(10)
            # 需要滑动 滚动条  通过按键盘↓实现
            self.enter_down_key(10)
            time.sleep(2)
            # --------------------- 上传ID文件 --------------------------------------
            self.find_element(*self.upload_id).click()
            self.log.info('点击【上传身份证】按钮')
            self.upload_file(id_card_name)
            self.log.info('上传文件: ' + id_card_name)
            # ---------------------------------------------------------------------
            time.sleep(2)
        self.find_element(*self.next2).click()
        self.log.info('点击step2【下一步】按钮')
        time.sleep(0.5)

    def register_step3(self):
        self.find_element(*self.question1_checkbox).click()
        self.log.info('点击【复选框】按钮')
        self.find_element(*self.next3).click()
        self.log.info('点击step3【下一步】按钮')
        time.sleep(2.2)

    def register_step4(self, investor_password, trade_password, note, c):
        if c == 'China':
            self.select_value_click(self.account_type_select1, self.account_type_select1_value)
            self.log.info('选择 第一个 account type：')
        self.select_value_click(self.currency_select, self.currency_select_value)
        self.log.info('选择currency： USD')
        self.select_value_click(self.leverage_select, self.leverage_select_value)
        self.log.info('选择 leverage： 1:10')
        self.send_keys(trade_password, *self.trade_password)
        self.log.info('输入 trade_password：' + trade_password)
        self.send_keys(trade_password, *self.trade_2_password)
        self.log.info('输入 trade_password：' + trade_password)
        self.send_keys(investor_password, *self.investor_password)
        self.log.info('输入 investor_password：' + investor_password)
        self.send_keys(investor_password, *self.investor_2_password)
        self.log.info('输入确认 investor_password：' + investor_password)
        self.send_keys(note, *self.note_input)
        self.log.info('输入 note：' + note)
        time.sleep(1)
        self.move_to_element(*self.submit)
        time.sleep(1)
        self.log.info('移动Y轴滚动条到页面底部')
        self.find_element(*self.auth1).click()
        self.log.info('点击【复选框1】按钮')
        self.find_element(*self.auth2).click()
        self.log.info('点击【复选框2】按钮')
        self.find_element(*self.submit).click()
        self.log.info('点击【提交】按钮')
        time.sleep(5)

    def register_demo_step2(self, pwd, country):
        """
        xxx
        :param pwd:
        :param country: 当前注册的国家 用于区分在crm后台是否配置了默认选项
        :return:
        """
        if country == 'China':
            self.select_value_click(self.ts_select, self.ts_select_value)
            self.log.info('选择 ts')
            self.select_value_click(self.account_type_select, self.account_type_select_value)
            self.log.info('选择 account_type')
            self.select_value_click(self.account_leverage_select, self.account_leverage_select_value)
            self.log.info('选择 account_leverage')
            self.select_value_click(self.account_currency_select, self.account_currency_select_value)
            self.log.info('选择 account_currency')
            self.select_value_click(self.deposit_select, self.deposit_select_value)
            self.log.info('选择 deposit')
        self.send_keys(pwd, *self.td_pwd)
        self.log.info('输入交易密码：' + pwd)
        self.send_keys(pwd, *self.td_2_pwd)
        self.log.info('输入2次密码：' + pwd)
        time.sleep(0.8)
        self.find_element(*self.demo_submit).click()
        self.log.info('点击【submit】按钮')
        time.sleep(8)

    def get_title(self):
        title = self.driver.title
        return title

    def get_tip(self):
        """
        弹窗提示
        :return:
        """
        t = self.find_element(*self.tips).text
        return t

    def get_step1_button_status(self):
        """
        获取 注册 第一步 页面中 提交按钮的状态
        :return:
        """
        t = self.find_element(*self.next1).get_attribute('disabled')
        if t:
            return t
        return 0

    def get_step2_button_status(self):
        """
        获取 注册 第二步 页面中 提交按钮的状态
        :return:
        """
        t = self.find_element(*self.next2).get_attribute('disabled')
        if t:
            return t
        return 0

    def get_error_tip(self, n):
        """
         通过data文件中的flag列判断获取哪个tip的值  前端输入框校验错误信息
        :param n:  自定义
        :return:  获取的文本信息：：--> str
        """
        if n == 2:
            t = self.find_element(*self.blacklist_country_tip).text
            return t
        elif n == 5:
            t = self.find_element(*self.email_tip).text
            return t
        elif n == 7:
            t = self.find_element(*self.password_tip).text
            return t
        else:
            return 0

    def get_progress(self):
        """
        获取 注册 页面的进度
        :return:
        """
        p = self.find_element(*self.progress).text
        return p

    def close_pop_window_and_finish_info(self):
        """
        关闭首页的弹窗，并跳转 完善信息界面
        :return:
        """
        self.find_element(*self.close_pop_window_button).click()
        self.find_element(*self.continue_button).click()
        time.sleep(2)

