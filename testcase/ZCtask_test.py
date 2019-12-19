import time
import unittest
from common.log import Logger
from common.MySelenium import mySelenium
from testpage.enterZC_page import enterZC_page
from testpage.ZCtask_page import ZCtask_page

log = Logger('testcase.ZCtasg_test').get_logger()


class ZCtask_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        log.info('****************************************  start  **************************************************')
        cls.dr = mySelenium()
        # cls.dr.browser()
        cls.dr.caller_starup('browser')
        cls.dr.max_window()
        cls.enterzc = enterZC_page(cls.dr)
        cls.enterzc.enter_zcAnd_login()
        cls.task = ZCtask_page(cls.dr)

    @classmethod
    def tearDownClass(cls):
        # time.sleep(3)
        cls.dr.quit()
        log.info('****************************************  start  **************************************************')

    def test1_view_task(self):
        """查看可参与任务"""
        self.task.click_filter_task()
        self.task.check_filtertask_result()

    def test2_task_print(self):
        """进入测试荣誉页面"""
        self.task.click_zc_honor()





