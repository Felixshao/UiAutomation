import unittest
import time
from common.MySelenium import mySelenium
from common.log import Logger
from config.getMobile import get_mobile
from config.readConfig import readConfig

log = Logger('common.Mymobile').get_logger()
phone_data = get_mobile()[1]
phone_data2 = readConfig().get_App()


class Mymobile(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        log.info("****************************************  start  **************************************************")
        cls.dr = mySelenium()
        cls.dr.mobile(phone_data)
        # enterApp_page(cls.dr).tgp_login_main()  # 登录app

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        log.info("****************************************  end  **************************************************\n")
        cls.dr.quit()
