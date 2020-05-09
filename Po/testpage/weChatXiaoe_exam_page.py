# _*_ config: utf-8 _*_
# weChatXiaoe_exam_page.py
import time
from common.basePage import Page
from config.getMobile import get_mobile


uiauto_phone_data = get_mobile('uiauto2_android')[1]
""" ------------------------------------ element --------------------------------------------------------------"""
xiaoe_nav_my = 'xpath->//div[@class="xe-navigation bottom_nav"]/div[4]'     # 准线网导航栏我的
xiaoe_my_exam = 'xpath->//div[@class="MyInfo"]/div[3]/div[2]/div[1]/div'   # 准线网导航栏我的中考试
xiaoe_exam_submitted = 'xpath->//section[@id="page-content"]/section[1]/div[2]'     # 考试页面选择已提交
xiaoe_submitted_one = 'xpath->//section[@class="examine-list"]/div[1]'      # 考试页面选择第一个
xiaoe_unsubmitted_six = 'xpath->//section[@class="examine-list"]/div[6]'
xiaoe_startexam_start = 'xpath->//div[@class="start-exam-btn-wrap"]/div'    # 考试介绍页点击开始考试
xiaoe_exam_submit = 'css->.submit-button[data-v-3aafa0ec]'  # 点击提交考试


class weChatXiaoe_exam_page(Page):

    def xiaoe_nav_my(self):
        """点击我的导航栏"""
        self.dr.uiauto2_webview(self.app)
        self.dr.click(xiaoe_nav_my)

    def click_my_exam(self):
        """点击我的页面的考试"""
        self.dr.click(xiaoe_my_exam)

    def click_exam_submitted(self):
        """考试页面点击已提交"""
        self.dr.click(xiaoe_exam_submitted)

    def click_submitted_one(self):
        """考试页面点击第一个"""
        self.dr.click(xiaoe_submitted_one)
        time.sleep(2)
        self.dr.back_button(2)  # 返回到我的页面
        self.dr.quit()

    def click_unsubmitted_text(self):
        """考试页面按名称点击考试"""
        self.dr.click(xiaoe_unsubmitted_six)

    def click_start_exam(self):
        """点击开始考试并滑动至底部"""
        self.dr.click(xiaoe_startexam_start)
        self.dr.quit(2)
        self.uiau.swipe_up(5)
        self.dr.uiauto2_webview(self.app, secs=3)

    def click_exam_submit(self):
        """点击提交考试"""
        self.dr.click(xiaoe_exam_submit)
        self.dr.back_button(2, 2)  # 返回到我的页面
        self.dr.quit(2)


