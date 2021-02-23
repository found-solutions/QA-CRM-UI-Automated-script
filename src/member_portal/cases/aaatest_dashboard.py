# import src.member_portal as pg
#
#
# class TestDashboard(pg.unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         pg.log.info('********** test start **********')
#         cls.data = pg.ExcelUtil('dashboard.xlsx').dict_data()
#         if int(pg.cf.get_global('is_headless')) == 1:
#             cls.driver = pg.webdriver.Chrome(options=pg.selenium_option, executable_path=pg.Paths.driver_path)
#         else:
#             cls.driver = pg.webdriver.Chrome(executable_path=pg.Paths.driver_path)
#         cls.pd = pg.PageDashboard(cls.driver)
#         cls.pd._open(2)
#         pg.PageLogin(cls.driver).my_login()
#
#     def test_1_add_live_account(self):
#         try:
#             self.pd.add_live_account(
#                 self.data[0].get('trade_pwd', 0),
#                 self.data[0].get('invest_pwd', 0),
#                 self.data[0].get('note', 0)
#             )
#             self.assertIn(self.pd.get_add_live_tip(), self.data[0].get('expect', 0))
#             pg.log.info('断言成功：' + self.data[0].get('desc', 0))
#         except Exception as e:
#             self.pd.img_screen('add_live_account')
#             pg.log.error('添加live账号异常：' + str(e))
#         pg.time.sleep(2)
#
#     def test_2_add_demo_account(self):
#         try:
#             self.pd.add_demo_account(self.data[1].get('trade_pwd', 0))
#             pg.time.sleep(4.4)
#             self.assertEqual(self.pd.get_add_demo_tip(), self.data[1].get('expect', 0))
#             pg.log.info('断言成功：' + self.data[1].get('desc', 0))
#         except Exception as e:
#             self.pd.img_screen('add_demo_account')
#             pg.log.error('添加demo账号异常：' + str(e))
#
#     def test_3_update_live_account(self):
#         try:
#             self.pd.update_live_account_trade_pwd(self.data[2].get('trade_pwd', 0))
#             self.assertEqual(self.pd.get_update_live_tip(), self.data[2].get('expect', 0))
#             pg.log.info('断言成功：' + self.data[2].get('desc', 0))
#         except Exception as e:
#             self.pd.img_screen('update_live_account')
#             pg.log.error('修改live账号trade密码异常：' + str(e))
#         pg.time.sleep(2)
#
#     def test_4_update_demo_account(self):
#         try:
#             self.pd.update_demo_pwd(self.data[3].get('trade_pwd', 0))
#             self.assertEqual(self.pd.get_update_demo_tip(), self.data[3].get('expect', 0))
#             pg.log.info('断言成功：' + self.data[3].get('desc', 0))
#         except Exception as e:
#             self.pd.img_screen('update_demo_account')
#             pg.log.error('修改live账号trade密码异常：' + str(e))
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()
#         pg.log.info('********** test end **********')
#
#
# if __name__ == '__main__':
#     pg.unittest.main()
