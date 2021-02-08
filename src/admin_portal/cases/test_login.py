import src.admin_portal as pg


@pg.ddt.ddt
class TestLogin(pg.unittest.TestCase):
    def setUp(self):
        pg.log.info('********** test start **********')
        if int(pg.cf.get_global('is_headless')) == 1:
            self.driver = pg.webdriver.Chrome(options=pg.selenium_option, executable_path=pg.Paths.driver_path)
        else:
            self.driver = pg.webdriver.Chrome(pg.Paths.driver_path)
        self.pl = pg.PageLogin(self.driver)
        self.pl._open(1)

    def tearDown(self):
        self.driver.quit()
        pg.log.info('清理环境成功')
        pg.log.info('********** test end **********')

    @pg.ddt.data(*pg.ExcelUtil('admin_login.xlsx').dict_data())
    @pg.ddt.unpack
    def test_login(self, **kwargs):
        try:
            self.pl.click_login_type()
            self.pl.login(kwargs.get('user'), kwargs.get('pwd'))
            if int(kwargs.get('case_no')) == 1:
                self.assertIn(kwargs.get('expect'), self.pl.driver.title)
                pg.log.info('断言成功: case {}'.format(kwargs.get('case_no')))
            elif int(kwargs.get('case_no')) == 2:
                self.assertEqual(kwargs.get('expect'), self.pl.get_none_user_tip())
                pg.log.info('断言成功: case {}'.format(kwargs.get('case_no')))
            elif int(kwargs.get('case_no')) == 3:
                self.assertEqual(kwargs.get('expect'), self.pl.get_none_pwd_tip())
                pg.log.info('断言成功: case {}'.format(kwargs.get('case_no')))
        except Exception as e:
            pg.log.error('case {} 断言失败: {}'.format(kwargs.get('case_no'), str(e)))
            self.pl.img_screen('登录 case {}'.format(kwargs.get('case_no')))
            raise


if __name__ == '__main__':
    pg.unittest.main()
