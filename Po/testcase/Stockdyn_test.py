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

    def test1_Lushang_stock(self):
        """查看鲁商发展（600223）股票情况"""
        self.dyn.open_stock_dynamic('sh600223')

    def test2_chinaSatcom_stock(self):
        """查看中国卫通（601698）股票情况"""
        self.dyn.open_stock_dynamic('sh601698')

    def test3_xinlong_stock(self):
        """查看欣龙控股（000955）股票情况"""
        self.dyn.open_stock_dynamic('sz000955')

    def test4_chinabaoan_stock(self):
        """查看中国宝安（000009）股票情况"""
        self.dyn.open_stock_dynamic('sz000009')

    def test5_twosixthree_stock(self):
        """查看二六三（002467）股票情况"""
        self.dyn.open_stock_dynamic('sz002467')