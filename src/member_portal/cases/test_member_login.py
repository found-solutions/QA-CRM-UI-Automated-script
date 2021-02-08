import src.member_portal as pg


@pg.ddt.ddt
class TestLogin(pg.unittest.TestCase):
    def setUp(self):
        pg.log.info('********** test start member login **********')
        if int(pg.cf.get_global('is_headless')) == 1:
            self.driver = pg.webdriver.Chrome(options=pg.selenium_option, executable_path=pg.Paths.driver_path)
        else:
            self.driver = pg.webdriver.Chrome(pg.Paths.driver_path)
        self.pl = pg.PageLogin(self.driver)
        self.pl._open(2)

    def tearDown(self):
        self.driver.quit()
        pg.log.info('********** test end member login **********')

    @pg.ddt.data(*pg.ExcelUtil('member_login.xlsx').dict_data())
    @pg.ddt.unpack
    def test_member_login(self, **kwargs):
        try:
            self.pl.my_login(kwargs.get('email'), kwargs.get('pwd'))
            if int(kwargs.get('case_no')) == 1:
                pg.time.sleep(3.3)
                self.assertEqual(kwargs.get('expect'), self.pl.get_home_title())
                pg.log.info('【{}】断言成功'.format(kwargs.get('desc')))
            elif int(kwargs.get('case_no')) == 2 or int(kwargs.get('case_no')) == 3:
                self.assertEqual(kwargs.get('expect'), self.pl.get_tip())
                pg.log.info('【{}】断言成功'.format(kwargs.get('desc')))
        except Exception as e:
            pg.log.error('【{}】断言失败: {}'.format(kwargs.get('case_no'), str(e)))
            self.pl.img_screen('登录 case {}'.format(kwargs.get('case_no')))
            raise


if __name__ == '__main__':
    pg.unittest.main()
