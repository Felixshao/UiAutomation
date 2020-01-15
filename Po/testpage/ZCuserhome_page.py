import time
from common.basePage import Page
from common.log import Logger
from common.BeautifulReport import BeautifulReport

log = Logger('testpage.ZCusehome_page').get_logger()
"""----------------------------------------------------- element --------------------------------------------------"""
zc_user_home = 'xpath->//ul[@class="per_family clearboth"]/li[2]/a'  # 众测任务页面用户需悬浮框的个人主页按钮
zc_userhome_signin = 'id->sign_in_button'   # 个人主页的签到按钮
zc_signin_window = 'xpath->//div[@id="sign_result_box"]/div/span'   # 签到成功窗口关闭按钮
zc_signin_window1 = 'xpath->//div[@id="sign_result_box"]/div/span1'   # 签到成功窗口关闭按钮
zc_userhome_myrecord = 'xpath->//ul[@class="ability_tab"]/li[2]/a'      # 个人主页我的战绩按钮
zc_myrecord_devote = 'xpath->//li[@class="statistic_t_li1"]/p/span'        # 我的战绩页面平均贡献率


class ZCuserhome_page(Page):

    def click_user_home(self):
        """点击个人主页按钮"""
        self.dr.click(zc_user_home)

    @BeautifulReport.add_test_img2('签到成功', '签到失败_无弹窗', '签到成功_今日已签到', '签到失败_未知原因')
    def click_userhome_signin(self):
        """点击签到按钮,并判断是否成功"""
        text = self.dr.get_ele_content(zc_userhome_signin)
        if text == '签到':
            self.dr.click(zc_userhome_signin)
            flag, ele = self.dr.judge_element(zc_signin_window)
            if flag:
                self.dr.get_page_screenshot(case_name='签到成功', source='other')
                self.dr.click(zc_signin_window)
                print('签到成功，用例通过')
                log.info('Success signin case!')
            else:
                self.dr.get_page_screenshot(case_name='签到失败_无弹窗', source='other')
                print('未弹出签到成功弹窗，用例失败!')
                log.error('Fail signin case, msg:signin success window does not pop up!')
                assert flag
        elif text == '今日已签到':
            print('今日已签到，用例成功!')
            self.dr.get_page_screenshot(file_path=self.img_path, case_name='签到成功_今日已签到', source='other')
            log.info('Success signin case!')
        else:
            self.dr.get_page_screenshot(file_path=self.img_path, case_name='签到失败_未知原因', source='other')
            print('未知原因，用例失败!')
            log.error('Fail signin case, msg:unkonwn reason!')
            assert False

    @BeautifulReport.add_test_img2('查看战绩_失败', '查看战绩_成功')
    def click_userhome_myrecord(self):
        """点击我的战绩,并输出贡献率"""
        self.dr.click(zc_userhome_myrecord)
        flag, ele = self.dr.judge_element(zc_myrecord_devote)
        if flag:
            devote = self.dr.get_ele_content(zc_myrecord_devote)
            print('用例通过,贡献率为:{0}'.format(devote))
            log.info('Success case, devote:"{0}"'.format(devote))
            self.dr.get_page_screenshot(file_path=self.img_path, case_name='查看战绩_成功', source='other')
        else:
            print('用例失败')
            log.info('Fail case!')
            self.dr.get_page_screenshot(file_path=self.img_path, case_name='查看战绩_失败', source='other')
            BeautifulReport.add_test_img('test_查看战绩_失败')
            assert flag