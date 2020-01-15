import time
import unittest
from common.log import Logger
from common.MySelenium import mySelenium
from Po.testpage.enterZC_page import enterZC_page
from Po.testpage.ZChonor_page import ZChonor_page

log = Logger('testcase.ZChonor_test').get_logger()


class ZChonor_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        log.info('*********************************** ZChonor_test start  *******************************************')
        cls.dr = mySelenium()
        # cls.dr.browser()
        cls.dr.caller_starup('browser')     # 打开浏览器
        cls.dr.max_window()
        cls.enterzc = enterZC_page(cls.dr)  # 获取公共元素
        cls.enterzc.enter_zcAnd_login(name='ZChonor_test')      # 登录众测并进入到测试任务页面
        cls.honor = ZChonor_page(cls.dr)

    @classmethod
    def tearDownClass(cls):
        # time.sleep(30)
        cls.dr.quit()
        log.info('**************************************** ZChonor_test end  ****************************************')

    def test1_view_newhonor(self):
        """查看最新一期荣誉榜单"""
        self.honor.click_zc_honor()
        self.honor.chick_zc_honor()

    def test2_view_learterm(self):
        """查看上期荣誉榜单"""
        self.honor.click_zc_honor()
        self.honor.click_zchonor_filter()
        self.honor.select_honor_lastterm()

    def test3_view_learissue(self):
        """查看上上期荣誉榜单"""
        self.honor.click_zc_honor()
        self.honor.click_zchonor_filter()
        self.honor.select_honor_lastissue()








