from common.basePage import Page
from common.BeautifulReport import BeautifulReport
from common.log import Logger

log = Logger('testpage.ZCnotice_page').get_logger()
"""---------------------------------------------------- element --------------------------------------------------"""
zc_notice_icon = 'xpath->//li[@class="pc_i_s fr"]/div/i'     # 众测任务页面通知图标
zc_notice_button = 'xpath->//div[@class="nav_mes_wrap "]/div/a'     # 众测任务页面任务通知按钮
zc_notice_newtask = 'class->push-part-4'    # 通知页面新任务推荐按钮
zc_newtask_unread_content = 'xpath->//span[@class="push-unread"]/../../td[3]/p/span'  # 新任务推荐栏下第一条未读通知的内容
zc_newtask_unread_button = 'xpath->//span[@class="push-unread"]/../../td[2]/p/a'  # 新任务推荐栏下第一条未读通知的推荐按钮
zc_unread_taskname = 'class->app-name'  # 兼职任务页面任务名称
zc_notice_operation = 'class->push-part-2'  # 通知页面运营活动按钮
zc_notice_onecontent = 'xpath->//p[@class="push-limit-p"]/span'  # 通知页面第一条通知内容(每个目录下都适用)
zc_notice_nonews = 'class->m-t-15'  # 通知栏无消息时提示文案
zc_notice_official = 'class->push-part-3'  # 通知页面官方活动按钮


class ZCnotice_page(Page):

    def hover_notice_button(self):
        """悬浮在通知图标上"""
        self.dr.hover_element(zc_notice_icon)

    def click_notice_button(self):
        """兼职任务点击通知按钮"""
        self.dr.click(zc_notice_button)

    def click_notice_newtask(self):
        """通知页面点击新任务推荐按钮"""
        self.dr.click(zc_notice_newtask)

    @BeautifulReport.add_test_img2('阅读未读消息_成功', '阅读未读消息_失败', '新任务推荐暂无未读消息')
    def click_newtask_unread(self):
        """新任务推荐按钮栏下点击第一条未读消息的任务推荐按钮"""
        flag, ele = self.dr.judge_element(zc_newtask_unread_content)
        if flag:
            try:
                unread_content = self.dr.get_ele_content(zc_newtask_unread_content)
                self.dr.click(zc_newtask_unread_button)
                print('用例成功，任务内容:', unread_content)
                log.info('Success view unreadn_task case， unread_content:"{}"'.format(unread_content))
                self.dr.get_page_screenshot(case_name='阅读未读消息_成功', source='other')
            except Exception as e:
                log.error('Fali view unreadn_task case.')
                log.error(e)
                print('用例失败!')
                self.dr.get_page_screenshot(case_name='阅读未读消息_失败', source='other')
                assert flag
                raise
        else:
            print('当前页无未读消息')
            self.dr.get_page_screenshot(case_name='新任务推荐暂无未读消息', source='other')

    @BeautifulReport.add_test_img2('查看运营活动_成功', '查看运营活动_失败', '运营活动暂无此类消息')
    def click_notice_operation(self):
        """通知页面点击运营活动按钮"""
        self.dr.click(zc_notice_operation)
        flag, ele = self.dr.judge_element(zc_notice_nonews)
        if not flag:
            try:
                notice_content = self.dr.get_ele_content(zc_notice_onecontent)
                print('用例成功，第一条运营活动内容为:', notice_content)
                log.info('Success view operation case, notice_content:"{}"'.format(notice_content))
                self.dr.get_page_screenshot(case_name='查看运营活动_成功', source='other')
            except Exception as e:
                log.info('Fail view operation case.')
                log.error(e)
                self.dr.get_page_screenshot(case_name='查看运营活动_失败', source='other')
                assert flag
                raise
        else:
            prompt = self.dr.get_ele_content(zc_notice_nonews)
            print('运营活动通知栏，提示为:', prompt)
            log.info('Success view operation case, promat:"{}"'.format(prompt))
            self.dr.get_page_screenshot(case_name='运营活动暂无此类消息', source='other')

    @BeautifulReport.add_test_img2('查看官方公告_成功', '查看官方公告_失败', '官方公告暂无此类消息')
    def click_notice_official(self):
        """通知页面点击官方公告按钮"""
        self.dr.click(zc_notice_official)
        flag, ele = self.dr.judge_element(zc_notice_nonews)
        if not flag:
            try:
                notice_content = self.dr.get_ele_content(zc_notice_onecontent)
                print('用例成功，第一条官方公告内容为:', notice_content)
                log.info('Success view official case, notice_content:"{}"'.format(notice_content))
                self.dr.get_page_screenshot(case_name='查看官方公告_成功', source='other')
            except Exception as e:
                log.info('Fail view official case.')
                log.error(e)
                self.dr.get_page_screenshot(case_name='查看官方公告_失败', source='other')
                assert flag
                raise
        else:
            prompt = self.dr.get_ele_content(zc_notice_nonews)
            print('官方公告通知栏，提示为:', prompt)
            log.info('Success view official case, promat:"{}"'.format(prompt))
            self.dr.get_page_screenshot(case_name='官方公告暂无此类消息', source='other')
