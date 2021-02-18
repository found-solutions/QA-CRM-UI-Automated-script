import src.member_portal as pg


@pg.ddt.ddt
class TestRegister(pg.unittest.TestCase):
    def setUp(self):
        pg.log.info('********** test start **********')
        if int(pg.cf.get_global('is_headless')) == 1:
            # 注册页面的滑动验证码需要 去除 selenium 的机器人标识
            pg.selenium_option.add_argument("--disable-blink-features=AutomationControlled")
            self.driver = pg.webdriver.Chrome(options=pg.selenium_option, executable_path=pg.Paths.driver_path)
        else:
            op = pg.webdriver.ChromeOptions()
            op.add_argument("--disable-blink-features=AutomationControlled")
            self.driver = pg.webdriver.Chrome(options=op, executable_path=pg.Paths.driver_path)
        self.pr = pg.PageRegister(self.driver)
        self.pr._open(2)

    def tearDown(self):
        self.driver.quit()
        if self.sql:
            pg.log.info('执行清理环境sql：' + str(self.sql.format(self.email)))
            pg.db(self.sql.format(self.email))
        pg.log.info('********** test end **********')

    @pg.ddt.data(*pg.ExcelUtil('register.xlsx').dict_data())
    @pg.ddt.unpack
    def test_register(self, **kwargs):
        try:
            self.sql = kwargs.get('sql', 0)
            self.email = kwargs.get('email', 0)
            self.pr.go_to_register()
            self.pr.register_step1(
                kwargs.get('first_name'),
                kwargs.get('middle_name'),
                kwargs.get('last_name'),
                kwargs.get('email'),
                kwargs.get('phone'),
                kwargs.get('password')
            )
            self.pr.register_step2(
                kwargs.get('address'),
                kwargs.get('city'),
                kwargs.get('state'),
                kwargs.get('postcode'),
                kwargs.get('id_number'),
                kwargs.get('f_name'),
                kwargs.get('l_name'),
                kwargs.get('card_name'),
                kwargs.get('address_name')
            )
            self.pr.register_step3()
            self.pr.register_step4(
                kwargs.get('investor_password')
            )
            self.assertIn(kwargs.get('expect'), self.pr.get_title())
            pg.log.info('{}: 断言成功'.format(kwargs.get('desc')))
        except Exception as e:
            self.pr.img_screen('register')
            pg.log.error('注册异常：' + str(e))
            raise
