import unittest, sys, os
import time
from common.MySelenium import mySelenium
from Po.testpage.enterZC_page import enterZC_page
from Po.testpage.ZCschool_page import ZCschool_page
from common.log import Logger

log = Logger('testcase.ZCschool_test').get_logger()


class ZCschool_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        log.info("""--------------------------------- ZCschool_test stark -------------------------------""")
        cls.dr = mySelenium()
        cls.dr.caller_starup('browser')
        cls.dr.max_window()
        cls.zc = enterZC_page(cls.dr)
        cls.zc.enter_zcAnd_login(name='ZCschool_test')
        cls.school = ZCschool_page(cls.dr)

    @classmethod
    def tearDownClass(cls):
        # time.sleep(30)
        cls.dr.quit()
        log.info("""--------------------------------- ZCschool_test end -------------------------------""")

    def test1_enter_zcschool(self):
        """进入众测学院页面"""
        self.school.click_nav_school()
