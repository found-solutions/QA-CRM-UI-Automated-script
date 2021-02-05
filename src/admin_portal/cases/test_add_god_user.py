# import src.admin_portal as pg
# from selenium.webdriver.common.action_chains import ActionChains
#
#
# class TestGodUser(pg.unittest.TestCase):
#     def setUp(self):
#         pass
#
#     def tearDown(self):
#         pass
#
#     def test_add_god_user(self):
#         pass
#
#     def test_delete_user(self):
#         pass



# u = 'https://stag-crm-member-2.tm-nonprod.com/register'
#
# options = pg.webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# # Google 最新版本， 去除selenium机器人标识
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_experimental_option('useAutomationExtension', False)
# d = pg.webdriver.Chrome(options=options, executable_path=pg.Paths.driver_path)
#
# d.get(u)
#
# hk = d.find_element_by_xpath('//*[@id="nc_1_n1z"]')
# ip = d.find_element_by_xpath('//*[@id="nc_1__scale_text"]/span')
# size = ip.size
# print(size)
# ActionChains(d).drag_and_drop_by_offset(hk, size['width'], size['height']).perform()
#
# print('end -------- ')
# d.quit()




















