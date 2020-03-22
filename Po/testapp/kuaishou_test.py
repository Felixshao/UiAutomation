import unittest, time
from common.log import Logger
from common.MySelenium import mySelenium
from Po.testpage.kuaishou_page import kuaishou_page
from common import openPC
from common.Myadb import Myadb
from config.getMobile import get_mobile

log = Logger('Po.testpc.kuaishou_test').get_logger()
mobile = get_mobile()[4]
command = 'adb connect ' + mobile['deviceName']     # 连接设备


class kuaishou_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        log.info('------------------------------------  kuaishou_test strat  --------------------------------------')
        openPC.open_pc_yesheng()    # 打开夜神模拟器
        openPC.open_pc_appium()     # 打开Appium
        time.sleep(60)
        Myadb().call_adb(command)
        time.sleep(5)
        cls.app = mySelenium()
        cls.app.mobile()
        cls.ks = kuaishou_page(cls.app)

    @classmethod
    def tearDownClass(cls):
        cls.app.quit()
        log.info('------------------------------------  kuaishou_test end  --------------------------------------')

    def test1_slide_window(self):
        """滑动窗口"""
        # self.ks.ks_click_comment()
        self.ks.ks_slide_window()