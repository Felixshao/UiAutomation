import unittest
import time
from common.MySelenium import mySelenium
from common.log import Logger
from Po.testpage.enterApp_page import enterApp_page

log = Logger('common.Mymobile').get_logger()


class Mymobile(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        log.info("****************************************  start  **************************************************")
        cls.dr = mySelenium()
        cls.dr.mobile()
        # enterApp_page(cls.dr).tgp_login_main()  # 登录app

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        log.info("****************************************  end  **************************************************\n")
        cls.dr.quit()
