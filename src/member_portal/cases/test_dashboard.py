import src.member_portal as pg


class TestRegister(pg.unittest.TestCase):
    def setUp(self):
        pg.log.info('********** test start **********')
        # self.data = pg.ExcelUtil().dict_data()
        driver = pg.webdriver.Chrome(executable_path=pg.Paths.driver_path)

        self.pr = pg.PageRegister(driver)
        self.pr._open(2)

    def tearDown(self):
        pass

    def test_add_live_account(self):
        pass













