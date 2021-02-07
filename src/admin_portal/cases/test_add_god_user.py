import src.admin_portal as pg
from selenium.webdriver.common.action_chains import ActionChains
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



u = 'https://stag-crm-member-2.tm-nonprod.com/register'

options = pg.webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
# Google 最新版本， 去除selenium机器人标识
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_experimental_option('useAutomationExtension', False)
# d = pg.webdriver.Chrome(options=options, executable_path=pg.Paths.driver_path)
driver = pg.webdriver.Chrome(executable_path=pg.Paths.driver_path)

pl = pg.PageLogin(driver)

pl._open(1)
pl.click_login_type()
pl.login()
pg.time.sleep(3)
driver.find_element_by_xpath("//*[text()='CLOSE']").click()
pg.time.sleep(1)
driver.find_element_by_xpath('//*[text()="Leverage Change"]').click()
pg.time.sleep(2)

js = "document.querySelector().style.top = 1"


print('end -------- ')
driver.quit()




















