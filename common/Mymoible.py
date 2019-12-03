import unittest
import time
from common.mySelenium import mySelenium
from common.log import Logger

log = Logger('common.Mymobile').get_logger()


class Mymobile(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        log.info("****************************************  start  **************************************************")
        cls.dr = mySelenium()
        cls.dr.mobile()

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        log.info("****************************************  end  **************************************************")
        cls.dr.quit()
