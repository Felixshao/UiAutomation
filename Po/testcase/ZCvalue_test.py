import unittest
import time
from common.MySelenium import mySelenium
from Po.testpage.enterZC_page import enterZC_page
from Po.testpage.ZCvalue_page import ZCvalue_page
from common.log import Logger

log = Logger('testcase.ZCvalue_test').get_logger()


class ZCvalue_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        log.info("""--------------------------------- ZCvalue_test stark -------------------------------""")
        cls.dr = mySelenium()
        cls.dr.caller_starup('browser')
        cls.dr.max_window()
        cls.zc = enterZC_page(cls.dr)
        cls.zc.enter_zcAnd_login(name='ZCvalue_test')
        cls.value = ZCvalue_page(cls.dr)

    @classmethod
    def tearDownClass(cls):
        # time.sleep(30)
        cls.dr.quit()
        log.info("""--------------------------------- ZCvalue_test end -------------------------------""")

    def test1_enter_zcvalue(self):
        """进入众测价值页面"""
        self.value.click_nav_value()
