import unittest
import time
from common.log import Logger
from common.MySelenium import mySelenium
from Po.testpage.weChatXiao_page import weChatXiaoe_page

log = Logger('testcase.weChatXiaoe_test').get_logger()


class weChatXiaoe_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        log.info("****************************************  start  **************************************************")
        cls.dr = mySelenium()
        cls.dr.caller_starup(source='mobile')
        cls.xiaoe = weChatXiaoe_page(cls.dr)
        cls.xiaoe.click_nav_my()
        cls.xiaoe.click_my_favorite()
        cls.xiaoe.click_favorite_search()
        cls.xiaoe.input_search_content()

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        log.info("****************************************  end  **************************************************\n")
        cls.dr.quit()

    def test1_vlayout_workbook(self):
        """布置手动作业"""
        self.xiaoe.click_xiaoe_my()
        self.xiaoe.click_xiaoemy_task()
        self.xiaoe.click_xiaoetask_createtask()
        self.xiaoe.click_xiaoetask_manualtask()
        self.xiaoe.input_manualtask_taskname(1)
        self.xiaoe.input_manualtask_taskcontent(1)
        # self.xiaoe.click_manualtask_taskcourse()
        # self.xiaoe.click_taskcourse_one()
        # self.xiaoe.click_manualtask_layout()
        # self.xiaoe.check_task(1)
        # self.xiaoe.click_buttomnav_home()

    def test2_vlayout_workbook(self):
        """修改手动作业"""
        self.xiaoe.click_xiaoe_my()
        self.xiaoe.click_xiaoemy_task()
        self.xiaoe.click_xiaoetask_onetask()
        self.xiaoe.click_taskdetails_edit()
        self.xiaoe.input_manualtask_taskname(2)
        self.xiaoe.input_manualtask_taskcontent(2)
        self.xiaoe.click_manualtask_savechange()
        self.xiaoe.check_task(2)
        self.xiaoe.click_buttomnav_home()

    def test3_tiaos(self):
        """"""






