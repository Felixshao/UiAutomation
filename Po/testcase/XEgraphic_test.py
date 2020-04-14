import unittest
from common.log import Logger
from common.MySelenium import mySelenium
from Po.testpage.XEcommon_page import XEcommon_page
from Po.testpage.XEgraphic_page import XEgraphic_page

log = Logger('Po.testcase.XEgraphic_test.py').get_logger()


class XEgraphic_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        log.info('---------------------------------- XEgraphic_test 开始 -----------------------------------------')
        cls.dr = mySelenium()
        cls.dr.browser()
        cls.dr.max_window()
        cls.common = XEcommon_page(cls.dr)
        cls.common.login()
        cls.graphic = XEgraphic_page(cls.dr)
        pass

    @classmethod
    def tearDownClass(cls):
        log.info('---------------------------------- XEgraphic_test 结束 -----------------------------------------')

    def test1_view_graphic(self):

        self.graphic.xe_shop_one()
        self.graphic.xe_oneshop_graphic()