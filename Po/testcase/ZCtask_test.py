import time
import unittest
from common.log import Logger
from common.MySelenium import mySelenium
from Po.testpage.enterZC_page import enterZC_page
from Po.testpage.ZCtask_page import ZCtask_page

log = Logger('testcase.ZCtasg_test').get_logger()


class ZCtask_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        log.info('**************************************** ZCtask_test start  ***************************************')
        cls.dr = mySelenium()
        # cls.dr.browser()
        cls.dr.caller_starup('browser')     # 打开浏览器
        cls.dr.max_window()
        cls.enterzc = enterZC_page(cls.dr)  # 获取公共元素
        cls.enterzc.enter_zcAnd_login(name='ZCtask_test')      # 登录众测并进入到测试任务页面
        cls.task = ZCtask_page(cls.dr)

    @classmethod
    def tearDownClass(cls):
        # time.sleep(3)
        cls.dr.quit()
        log.info('**************************************** ZCtask_test end  ******************************************')

    def test1_view_cantask(self):
        """查看可参与任务"""
        self.task.click_filter_cantask()

    def test2_view_protask(self):
        """查看进行中任务"""
        self.task.click_filter_protask()

    def test3_view_endtask(self):
        """查看已结束任务"""
        self.task.click_filter_endtask()

    def test4_view_bugexplore(self):
        """查看bug探索任务"""
        self.task.click_nav_zctask()
        self.task.click_filter_bugexplore()

    def test5_view_caserun(self):
        """查看用例执行任务"""
        self.task.click_nav_zctask()
        self.task.click_filter_caserun()

    def test6_view_casedesign(self):
        """查看用例设计任务"""
        self.task.click_nav_zctask()
        self.task.click_filter_casedesign()

    def test7_view_functest(self):
        """查看功能测试任务"""
        self.task.click_nav_zctask()
        self.task.click_filter_functest()

    def test8_view_residenttask(self):
        """查看驻场任务"""
        self.task.click_nav_zctask()
        self.task.click_filter_resident()
        self.task.click_resident_task()

    def test9_view_hardware(self):
        """查看硬件连通任务"""
        self.task.click_nav_zctask()
        self.task.click_filter_resident()
        self.task.click_resident_hardware()

    def testA_view_compatible(self):
        """查看遍历兼容任务"""
        self.task.click_nav_zctask()
        self.task.click_filter_resident()
        self.task.click_resident_compatible()







