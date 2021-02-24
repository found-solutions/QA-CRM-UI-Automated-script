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
        self.pr.go_to_register()

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
            self.sql = kwargs.get('sql', None)
            self.email = kwargs.get('email', 0)
            country = kwargs.get('country', None)
            self.pr.register_step1(
                kwargs.get('first_name'),
                kwargs.get('middle_name'),
                kwargs.get('last_name'),
                kwargs.get('email'),
                country,
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
                country
            )
            if country == 'Taiwan':
                self.assertEqual(kwargs.get('expect'), self.pr.get_tip())
                pg.log.info('{}: 断言成功'.format(kwargs.get('desc')))
            else:
                pg.time.sleep(6)
                self.pr.register_step3()
                self.pr.register_step4(
                    kwargs.get('investor_password'),
                    kwargs.get('trade_password'),
                    kwargs.get('note'),
                    country
                )
                self.assertIn(kwargs.get('expect'), self.pr.get_title())
                pg.log.info('{}: 断言成功'.format(kwargs.get('desc')))
        except Exception as e:
            self.pr.img_screen('register_alive_{}'.format(kwargs.get('case_no')))
            pg.log.error('注册异常：' + str(e))
            raise

    @pg.ddt.data(*pg.ExcelUtil('register_step1.xlsx').dict_data())
    @pg.ddt.unpack
    def test_step_1_register(self, **kwargs):
        try:
            is_tip = int(kwargs.get('is_tip'))
            flag = int(kwargs.get('flag'))
            self.sql = kwargs.get('sql', None)
            self.pr.register_step1(
                kwargs.get('first_name'),
                kwargs.get('middle_name'),
                kwargs.get('last_name'),
                kwargs.get('email'),
                kwargs.get('country'),
                kwargs.get('phone'),
                kwargs.get('password'),
                is_tip, 0.5
            )
            if is_tip == 1:
                if flag == 3:
                    # 断言 按钮 为不可点击： disabled
                    self.assertEqual(kwargs.get('expect'), self.pr.get_step1_button_status())
                    pg.log.info('{}: 断言成功'.format(kwargs.get('desc')))
                else:
                    self.assertEqual(kwargs.get('expect'), self.pr.get_tip())
                    pg.log.info('{}: 断言成功'.format(kwargs.get('desc')))
            elif is_tip == 0:
                self.assertEqual(kwargs.get('expect'), self.pr.get_error_tip(flag))
                pg.log.info('{}: 断言成功'.format(kwargs.get('desc')))
        except Exception as e:
            self.pr.img_screen('register_step1_{}'.format(kwargs.get('case_no')))
            pg.log.error('step1异常：' + str(e))
            raise

    @pg.ddt.data(*pg.ExcelUtil('register_step2.xlsx').dict_data())
    @pg.ddt.unpack
    def test_step_2_register(self, **kwargs):
        try:
            self.sql = kwargs.get('sql', None)
            self.email = kwargs.get('email', 0)
            self.pr.register_step1(
                kwargs.get('first_name'),
                kwargs.get('middle_name'),
                kwargs.get('last_name'),
                kwargs.get('email'),
                kwargs.get('country'),
                kwargs.get('phone'),
                kwargs.get('password'),
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
                kwargs.get('country')
            )
            self.assertEqual(kwargs.get('expect'), self.pr.get_step2_button_status())
            pg.log.info('{}: 断言成功'.format(kwargs.get('desc')))
        except Exception as e:
            self.pr.img_screen('register_step2_{}'.format(kwargs.get('case_no')))
            pg.log.error('step2异常：' + str(e))
            raise

    @pg.ddt.data(*pg.ExcelUtil('register_finish_info.xlsx').dict_data())
    @pg.ddt.unpack
    def test_todolist(self, **kwargs):
        case_no = int(kwargs.get('case_no'))
        pg.log.info('case_no：：：' + str(case_no))
        try:
            self.sql = kwargs.get('sql', None)
            self.email = kwargs.get('email', 0)
            self.pr.register_step1(
                kwargs.get('first_name'),
                kwargs.get('middle_name'),
                kwargs.get('last_name'),
                kwargs.get('email'),
                kwargs.get('country'),
                kwargs.get('phone'),
                kwargs.get('password'),
            )
            if case_no == 2 or case_no == 3:
                self.pr.register_step2(
                    kwargs.get('address'),
                    kwargs.get('city'),
                    kwargs.get('state'),
                    kwargs.get('postcode'),
                    kwargs.get('id_number'),
                    kwargs.get('f_name'),
                    kwargs.get('l_name'),
                    kwargs.get('card_name'),
                    kwargs.get('country')
                )
                pg.time.sleep(5)
            if case_no == 3:
                pg.log.info('准备完成第三步：：：')
                self.pr.register_step3()
                pg.log.info('完成第三步：：：')
            self.pr._open(2)
            self.pr.close_pop_window_and_finish_info()
            self.assertEqual(kwargs.get('expect'), self.pr.get_progress())
            pg.log.info('{}: 断言成功'.format(kwargs.get('desc')))
        except Exception as e:
            self.pr.img_screen('register_todolist_{}'.format(case_no))
            pg.log.error('todolist异常：' + str(e))
            raise
