import unittest
import time
from common.MySelenium import mySelenium
from Po.testpage.Stockdyn_page import Stockdyn_page
from common.log import Logger

log = Logger('testcase.Stockdyn_test').get_logger()


class Stockdyn_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        log.info("""--------------------------------- Stockdyn_test stark -------------------------------""")
        cls.dr = mySelenium()
        cls.dr.caller_starup('browser')
        cls.dr.max_window()
        cls.dyn = Stockdyn_page(cls.dr)

    @classmethod
    def tearDownClass(cls):
        # time.sleep(30)
        cls.dr.quit()
        log.info("""--------------------------------- Stockdyn_test end -------------------------------""")

    def test1_view_stock(self):
        """查看600223股票情况"""
        self.dyn.open_stock_dynamic()
        self.dyn.send_stock_search()
