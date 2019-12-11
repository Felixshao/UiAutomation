import unittest
import time
from common.MySelenium import mySelenium
from common.log import Logger

log = Logger('Mytest.Mytest').get_logger()


class Mybrowser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        log.info('****************************************  start  **************************************************')
        cls.dr = mySelenium()
        cls.dr.browser()
        cls.dr.max_window()

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.dr.quit()
        log.info('****************************************  end  **************************************************')


