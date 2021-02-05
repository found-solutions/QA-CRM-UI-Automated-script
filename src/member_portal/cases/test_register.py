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
            pg.log.info('有界面模式：：')
            op = pg.webdriver.ChromeOptions()
            op.add_argument("--disable-blink-features=AutomationControlled")
            self.driver = pg.webdriver.Chrome(options=op, executable_path=pg.Paths.driver_path)
        self.pr = pg.PageRegister(self.driver)
        self.pr._open(2)

    def tearDown(self):
        self.driver.quit()
        pg.log.info('********** test end **********')
        sql = self.sql
        pg.log.info('需要执行的sql：：' + str(sql))

    @pg.ddt.data(*pg.ExcelUtil('register.xlsx').dict_data())
    @pg.ddt.unpack
    def test_register(self, **kwargs):
        pg.log.info('********** test_register **********')
        try:
            self.sql = kwargs.get('sql', 0)
            self.pr.go_to_register()
            self.pr.register_step1(
                kwargs.get('first_name'),
                kwargs.get('middle_name'),
                kwargs.get('last_name'),
                kwargs.get('email'),
                kwargs.get('phone'),
                kwargs.get('password')
            )
            # self.pr.register_step2()

        except Exception as e:
            print(e)
            self.pr.img_screen('register')
            pg.log.error('注册异常：' + str(e))
















