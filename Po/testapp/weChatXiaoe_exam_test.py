# _*_ config: utf-8 _*_
# weChatXiaoe_exam_test.py

import unittest
from common.MyUiautomator import MyUiautomator2
from common.MySelenium import mySelenium
from Po.testpage.enterXiaoe_page import enterXiaoe_page
from Po.testpage.weChatXiaoe_exam_page import weChatXiaoe_exam_page


class weChatXiaoe_exam_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.uiau = MyUiautomator2()
        cls.dr = mySelenium()
        cls.uiau.connect_android()
        cls.app = cls.uiau.connect_app()
        cls.exam = weChatXiaoe_exam_page(driver=cls.dr, uiau=cls.uiau, app=cls.app)
        cls.entet = enterXiaoe_page(driver=cls.dr, uiau=cls.uiau, app=cls.app)
        cls.entet.wechat_xiaoe_zhunxianwang()

    @classmethod
    def tearDownClass(cls):

        cls.uiau.uiauto2_stop()

    def test1_view_exam(self):
        """查看已完成考试"""
        self.exam.xiaoe_nav_my()
        self.exam.click_my_exam()
        self.exam.click_exam_submitted()
        self.exam.click_submitted_one()

    def test2_join_exam(self):
        """参加一个考试"""
        self.exam.xiaoe_nav_my()
        self.exam.click_my_exam()
        self.exam.click_unsubmitted_text()
        self.exam.click_start_exam()
        self.exam.click_exam_submit()