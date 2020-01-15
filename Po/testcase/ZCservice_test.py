import unittest
import time
from common.MySelenium import mySelenium
from Po.testpage.enterZC_page import enterZC_page
from Po.testpage.ZCservice_page import ZCservice_page
from common.log import Logger

log = Logger('testcase.ZCservice_test').get_logger()


class ZCservice_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        log.info("""--------------------------------- ZCservice_test stark -------------------------------""")
        cls.dr = mySelenium()
        cls.dr.caller_starup('browser')
        cls.dr.max_window()
        cls.zc = enterZC_page(cls.dr)
        cls.zc.enter_zcAnd_login(name='ZCservice_test')
        cls.service = ZCservice_page(cls.dr)

    @classmethod
    def tearDownClass(cls):
        # time.sleep(30)
        cls.dr.quit()
        log.info("""--------------------------------- ZCservice_test end -------------------------------""")

    def test1_enter_zcservice(self):
        """进入众测服务页面"""
        self.service.click_nav_service()
