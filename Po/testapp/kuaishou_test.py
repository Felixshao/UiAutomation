import unittest, time
from common.MySelenium import mySelenium
from Po.testpage.kuaishou_page import kuaishou_page
from common import openPC
from common.Myadb import Myadb
from config.getMobile import get_mobile
from common.log import Logger

log = Logger('Po.testpc.kuaishou_test').get_logger()
mobile = get_mobile()[5]
command = 'adb connect ' + mobile['deviceName']     # 连接设备


class kuaishou_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        log.info('------------------------------------  kuaishou_test strat  --------------------------------------')
        # openPC.open_pc_yesheng()  # 打开夜神模拟器
        # openPC.open_pc_appium()     # 打开Appium
        # time.sleep(40)
        # Myadb().call_adb(command)
        # time.sleep(5)
        cls.app = mySelenium()
        cls.app.mobile(data=mobile)
        cls.ks = kuaishou_page(cls.app)

    @classmethod
    def tearDownClass(cls):
        cls.app.quit()
        log.info('------------------------------------  kuaishou_test end  --------------------------------------')

    def test1_slide_window(self):
        """滑动窗口"""
        # 14:38 5435 14:19 9840  1.25 14:59
        # self.ks.ks_click_comment()]
        self.ks.ks_slide_window()