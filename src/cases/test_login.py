import src.package as pg


@pg.ddt.ddt
class TestLogin(pg.unittest.TestCase):
    def setUp(self):
        self.ss = []
        pg.log.info('********** test start **********')
        self.driver = pg.webdriver.Chrome(pg.Paths.driver_path)
        self.pl = pg.PageLogin(self.driver)
        self.pl._open()

    def tearDown(self):
        self.pl.driver.quit()
        if len(self.ss) != 0:
            for s in self.ss:
                pg.log.info('sql:::: {}'.format(s))
            pg.log.info('清理环境成功')
        pg.log.info('********** test end **********')
        import time
        time.sleep(3)

    @pg.ddt.data(*pg.ExcelUtil('login.xlsx').dict_data())
    @pg.ddt.unpack
    def test_login(self, **kwargs):
        try:
            self.pl.click_login_type()
            self.pl.login(kwargs.get('user'), kwargs.get('pwd'))
            if int(kwargs.get('case_no')) == 1:
                self.assertIn(kwargs.get('expect'), self.pl.driver.title)
                pg.log.info('断言成功: case {}'.format(kwargs.get('case_no')))
                if kwargs.get('sql') != '' or kwargs.get('sql') is not None:
                    self.ss.append(kwargs.get('sql'))
            elif int(kwargs.get('case_no')) == 2:
                self.assertEqual(kwargs.get('expect'), self.pl.get_none_user_tip())
                pg.log.info('断言成功: case {}'.format(kwargs.get('case_no')))
                if kwargs.get('sql') != '' or kwargs.get('sql') is not None:
                    self.ss.append(kwargs.get('sql'))
            elif int(kwargs.get('case_no')) == 3:
                self.assertEqual(kwargs.get('expect'), self.pl.get_none_pwd_tip())
                pg.log.info('断言成功: case {}'.format(kwargs.get('case_no')))
                if kwargs.get('sql') != '' or kwargs.get('sql') is not None:
                    self.ss.append(kwargs.get('sql'))
        except Exception as e:
            pg.log.error('case {} 断言失败: {}'.format(kwargs.get('case_no'), str(e)))
            self.pl.img_screen('登录 case {}'.format(kwargs.get('case_no')))
            raise


if __name__ == '__main__':
    pg.unittest.main()
