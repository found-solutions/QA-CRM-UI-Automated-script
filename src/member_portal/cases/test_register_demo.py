import src.member_portal as pg


@pg.ddt.ddt
class TestRegisterDemo(pg.unittest.TestCase):
    def setUp(self):
        pg.log.info('********** test start register demo **********')
        if int(pg.cf.get_global('is_headless')) == 1:
            # 注册页面的滑动验证码需要 去除 selenium 的机器人标识
            pg.selenium_option.add_argument("--disable-blink-features=AutomationControlled")
            self.driver = pg.webdriver.Chrome(options=pg.selenium_option, executable_path=pg.Paths.driver_path)
        else:
            op = pg.webdriver.ChromeOptions()
            op.add_argument("--disable-blink-features=AutomationControlled")
            op.add_experimental_option("excludeSwitches", ['enable-automation'])
            self.driver = pg.webdriver.Chrome(options=op, executable_path=pg.Paths.driver_path)
        self.pr = pg.PageRegister(self.driver)
        self.pr._open('https://stag-crm-member-2.tm-nonprod.com/register?register_type=demo')

    def tearDown(self):
        self.driver.quit()
        if self.sql:
            pg.log.info('执行清理环境sql：' + str(self.sql.format(self.email)))
        pg.log.info('********** test end register demo ********** \n')

    @pg.ddt.data(*pg.ExcelUtil('register.xlsx').dict_data())
    @pg.ddt.unpack
    def test_register_demo(self, **kwargs):
        try:
            self.sql = kwargs.get('sql')
            self.email = kwargs.get('email')
            self.pr.register_step1(
                kwargs.get('first_name'),
                kwargs.get('middle_name'),
                kwargs.get('last_name'),
                kwargs.get('email'),
                kwargs.get('phone'),
                kwargs.get('password')
            )
            pg.time.sleep(5)
            self.pr.register_demo_step2(kwargs.get('password'))
            self.assertIn(kwargs.get('expect'), self.pr.get_title())
            pg.log.info('{}: 断言成功'.format(kwargs.get('desc')))
        except Exception as e:
            self.pr.img_screen('register_demo')
            pg.log.error('注册demo异常：' + str(e))
