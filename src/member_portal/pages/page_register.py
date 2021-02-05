from common.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class PageRegister(BasePage):
    register_bt = (By.XPATH, "//a[text()='sign up']")
    # step1
    first_name_input = (By.XPATH, "//input[@aria-label='First Name-en *']")
    middle_name_input = (By.XPATH, "//input[@aria-label='Middle Name-en']")
    last_name_input = (By.XPATH, "//input[@aria-label='Last Name-en *']")
    email_input = (By.XPATH, "//input[@aria-label='Email *']")
    mobile_input = (By.XPATH, "//input[@aria-label='Mobile Number *']")
    pwd_input = (By.XPATH, "//input[@aria-label='Client Portal Password']")
    yzm = (By.XPATH, "//*[@id='nc_1_n1z']")
    yzm_back = (By.XPATH, '//*[@id="nc_1__scale_text"]/span')
    next1 = (By.XPATH, "//*[@id='app']/div/section/div[2]/div/div[3]/button")

    # step2
    birth_input = (By.XPATH, "//input[@aria-label='Date of Birth *']")
    address_input = (By.XPATH, "//input[@aria-label='Address *']")
    city_input = (By.XPATH, "//input[@aria-label='City *']")
    state_input = (By.XPATH, "//input[@aria-label='State *']")
    post_code_input = (By.XPATH, "//input[@aria-label='Postcode *']")
    gender_select = (By.XPATH, "//*[@id='app']/div/section/main/section/div[2]/div[2]/section/div[2]/div/div/div[2]/form/div[1]/label[6]/div")
    gender_select_value = (By.XPATH, "//*[text()='Male']")
    # 开启认证才有 ------------------------------------------------------------------------------
    electronic_select = (By.XPATH, "//*[@id='app']/div/section/main/section/div[2]/div[2]/section/div[2]/div/div/div[2]/form/div[2]/label/div")
    electronic_select_value = (By.XPATH, "//*[text()='Australian Driving Licence']")
    id_number_input = (By.XPATH, "//input[@aria-label='ID Number *']")
    title_select = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/section/div[2]/div/div/div[2]/form/div[2]/label[3]/div')
    title_select_value = (By.XPATH, "//*[text()='Mr.']")
    driver_state_input = (By.XPATH, "//input[@aria-label='Drive State *']")
    # ------------------------------------------------------------------------------
    next2 = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/section/div[2]/div/div/div[2]/div/button')

    # step3
    question1_checkbox = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/section/div[2]/div/div/div[3]/form/div/div[2]/div/div[1]/div[1]/div')
    next3 = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/section/div[2]/div/div/div[3]/div/button')

    # step4
    currency_select = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/section/div[2]/div/div/div[4]/form/div[1]/div/div[3]/label/div')
    currency_select_value = (By.XPATH, "//*[text()='AUD']")
    leverage_select = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/section/div[2]/div/div/div[4]/form/div[2]/label/div')
    leverage_select_value = (By.XPATH, "//*[text()='1:10']")
    investor_password = (By.XPATH, "//input[@aria-label='Investor Password']")
    auth1 = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/section/div[2]/div/div/div[4]/form/div[7]/div[1]/div[1]/div')
    auth2 = (By.XPATH, '//*[@id="app"]/div/section/main/section/div[2]/div[2]/section/div[2]/div/div/div[4]/form/div[7]/div[2]/div[1]/div')
    submit = (By.XPATH, '//*[text()="SUBMIT"]')

    def go_to_register(self):
        self.find_element(*self.register_bt).click()
        self.log.info('点击【注册】按钮')

    def register_step1(self, fn, mn, ln, email, phone, pwd):
        self.send_keys(fn, *self.first_name_input)
        self.log.info('输入first name：' + fn)
        self.send_keys(mn, *self.middle_name_input)
        self.log.info('输入middle name：' + mn)
        self.send_keys(ln, *self.last_name_input)
        self.log.info('输入last name：' + ln)
        self.send_keys(email, *self.email_input)
        self.log.info('输入email：' + email)
        self.log.info('123输入phone：' + phone)
        self.send_keys(phone, *self.mobile_input)
        self.log.info('输入phone：' + phone)
        self.send_keys(pwd, *self.pwd_input)
        self.log.info('输入pwd：' + pwd)
        time.sleep(0.8)
        self.move_yzm(self.yzm, self.yzm_back)
        self.log.info('滑动验证码')
        time.sleep(0.8)
        self.find_element(*self.next1).click()
        self.log.info('点击step1【下一步】按钮')
        time.sleep(0.8)

    def register_step2(self, birth, address, city, state, postcode):
        self.send_keys(birth, *self.birth_input)
        self.log.info('输入birth：' + birth)
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
        self.find_element(*self.next2).click()
        self.log.info('点击step2【下一步】按钮')
        time.sleep(0.8)

    def register_step3(self):
        self.find_element(*self.question1_checkbox).click()
        self.log.info('点击【复选框】按钮')
        self.find_element(*self.next3).click()
        self.log.info('点击step3【下一步】按钮')

    def register_step4(self, investor_password):
        self.select_value_click(self.currency_select, self.currency_select_value)
        self.select_value_click(self.leverage_select, self.leverage_select_value)
        self.send_keys(investor_password, *self.investor_password)







