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
        cls.dr.caller_starup('browser')     # 打开浏览器
        cls.dr.max_window()
        cls.enterzc = enterZC_page(cls.dr)  # 获取公共元素
        cls.enterzc.enter_zcAnd_login()      # 登录众测并进入到测试任务页面
        cls.task = ZCtask_page(cls.dr)

    @classmethod
    def tearDownClass(cls):
        # time.sleep(3)
        cls.dr.quit()
        log.info('****************************************  end  **************************************************')

    def test1_view_cantask(self):
        """查看可参与任务"""
        self.task.click_filter_cantask()
        self.task.check_filtertask_result('can')

    def test2_view_protask(self):
        """查看进行中任务"""
        self.task.click_filter_protask()
        self.task.check_filtertask_result('pro')

    def test3_view_endtask(self):
        """查看已结束任务"""
        self.task.click_filter_endtask()
        self.task.check_filtertask_result('end')







