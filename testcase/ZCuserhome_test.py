import time
import unittest
from common.log import Logger
from common.MySelenium import mySelenium
from testpage.enterZC_page import enterZC_page
from testpage.ZCuserhome_page import ZCuserhome_page

log = Logger('testcase.ZCuserhome_test').get_logger()


class ZCuserhome_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        log.info('****************************************  start  **************************************************')
        cls.dr = mySelenium()
        cls.dr.browser()
        cls.dr.max_window()
        cls.enterzc = enterZC_page(cls.dr)
        cls.enterzc.enter_zcAnd_login()
        cls.signin = ZCuserhome_page(cls.dr)

    @classmethod
    def tearDownClass(cls):
        # time.sleep(3)
        cls.dr.quit()
        log.info('****************************************  end  **************************************************')

    def test1_ZCsignin(self):
        """众测签到"""
        self.enterzc.hover_user_window()
        self.signin.click_user_home()
        self.signin.click_userhome_signin()

    def test2_view_myrecode(self):
        """查看战绩"""
        self.signin.click_userhome_myrecord()



