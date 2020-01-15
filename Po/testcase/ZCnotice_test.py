import time
import unittest
from common.log import Logger
from common.MySelenium import mySelenium
from Po.testpage.enterZC_page import enterZC_page
from Po.testpage.ZCnotice_page import ZCnotice_page

log = Logger('testcase.ZCnotice_test').get_logger()


class ZCnotice_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        log.info('**************************************** ZCnotice_test start  **************************************')
        cls.dr = mySelenium()
        # cls.dr.browser()
        cls.dr.caller_starup('browser')
        cls.dr.max_window()
        cls.enterzc = enterZC_page(cls.dr)
        cls.enterzc.enter_zcAnd_login(name='ZCnotice_test')
        cls.notice = ZCnotice_page(cls.dr)

    @classmethod
    def tearDownClass(cls):
        # time.sleep(3)
        cls.dr.quit()
        log.info('**************************************** ZCnotice_test end  ****************************************')

    def test1_view_unreadnotice(self):
        """查看新任务推荐未读消息"""
        self.notice.hover_notice_button()
        self.notice.click_notice_button()
        self.notice.click_notice_newtask()
        self.notice.click_newtask_unread()

    def test2_view_operationnotice(self):
        """查看最新运营活动通知"""
        self.notice.hover_notice_button()
        self.notice.click_notice_button()
        self.notice.click_notice_operation()

    def test3_view_officialnotice(self):
        """查看最新官方公告通知"""
        self.notice.hover_notice_button()
        self.notice.click_notice_button()
        self.notice.click_notice_official()




