import os
import time
from common.basePage import Page
from common.log import Logger

log = Logger('testpage.weChatXiaoe_page').get_logger()
task_name = '移动自动化相关问题：'
task_content = '1.appium如何使用?\n' + '2.移动自动化如何实现?'
change_taskname = 'web自动化相关问题：'
change_taskcontent = '1.selenium如何使用?\n' + '2.unittest框架如何实现?'
"""--------------------------------------------------- element ---------------------------------------------------"""
wechat_nav_my = 'uiautomator->我'     # 导航栏我
wechat_my_favorite = 'uiautomator->收藏'  # 我的页面收藏按钮
wechat_favorite_search = 'accessibility id->搜索'     # 收藏页面搜索图标
wechat_search_input = 'id->com.tencent.mm:id/m7'    # 收藏中搜索页面输入框(真机，努比亚)
# wechat_search_input = 'id->com.tencent.mm:id/kh'    # 收藏中搜索页面输入(模拟器，夜神)
wechat_search_result = 'id->com.tencent.mm:id/bd'   # 选择搜索结果第一个(真机，努比亚)
# wechat_search_result = 'id->com.tencent.mm:id/bb'   # 选择搜索结果第一个(模拟器，夜神)
wechat_xiaoenav_my = 'xpath->//div[@class="micro_wrapper"]/div[1]/div[1]/div[4]'     # 准现网我的按钮
wechat_xiaoemy_task = 'xpath->//div[@class="function-card"]/div[3]'    # 准现网我的页面作业按钮
wechat_xiaoetask_createtask = 'class->exercise-set-wrapper'     # 作业页面布置作业按钮
wechat_xiaoetask_manualtask = 'xpath->//div[@class="exercise-choose__conent"]/div[2]'  # 作业页面手动布置作业按钮
wechat_manualtask_taskname = 'css->.title>input[data-v-3df158b6]'    # 手动布置作业页面作业名称
wechat_manualtask_taskcontent = 'id->mid_textarea'  # 手动布置作业页面作业内容
wechat_manualtask_taskcourse = 'class->choose'  # 手动布置作业页面关联课程按钮
wechat_taskcourse_one = 'xpath->//div[@class="link-courses-container"]/div[1]'  # 手动布置作业关联课程页面第一个课程
wechat_taskcourse_confirm = 'css->.save[data-v-54ac4107]'  # 手动布置作业关联课程页面确认按钮
wechat_manualtask_layout = 'class->white-bg'    # 手动布置作业页面布置作业按钮
wechat_taskdetails_taskname = 'class->task-name'    # 作业详情页作业名称
xiaoe_bottomnav_home = 'xpath->//ul[@class="ss-footer-nav"]/li[1]'  # 作业详情页底部导航店铺主页
wechat_xiaoetask_onetask = 'xpath->//div[@id="lShouldLoadMore"]/div[1]/div[1]'   # 点击作业列表页第一个作业
wechat_taskdetails_edit = 'xpath->//span[@class="c13 exercise-edit theme-customize-font"]'   # 作业详情页编辑按钮
wechat_manualtask_savechange = 'class->white-bg'     # 修改作业页面保存修改按钮


class weChatXiaoe_page(Page):

    def click_nav_my(self):
        """点击微信首页导航栏我的"""
        self.dr.click(wechat_nav_my)

    def click_my_favorite(self):
        """点击微信我的页面收藏按钮"""
        self.dr.click(wechat_my_favorite)

    def click_favorite_search(self):
        """点击微信收藏页面搜索图标"""
        self.dr.click(wechat_favorite_search)

    def input_search_content(self):
        """在微信收藏页面搜索框输入内容,并点击"""
        # self.dr.get_page_source('我的收藏搜索页面.xml')
        n = 0
        while True:
            self.dr.send(wechat_search_input, '准现网', default='搜索')
            flag, ele = self.dr.judge_element(wechat_search_result)
            self.dr.get_page_source('微信我的收藏搜索结果页.xml')
            if flag:
                ele.click()
                break
            elif n == 3:
                break
            n = n+1
        self.dr.switch_app_context()

    def click_xiaoe_my(self):
        """点击小鹅通准现网我的按钮"""
        self.dr.click(wechat_xiaoenav_my, secs=12)

    def click_xiaoemy_task(self):
        """点击小鹅通我的页面作业按钮"""
        self.dr.click(wechat_xiaoemy_task)

    def click_xiaoetask_createtask(self):
        """点击作业页面创建按钮"""
        self.dr.click(wechat_xiaoetask_createtask)

    def click_xiaoetask_manualtask(self):
        """点击作业页面手动布置按钮"""
        self.dr.click(wechat_xiaoetask_manualtask)

    def input_manualtask_taskname(self, num=1):
        """
        输入手动作业名称
        :param num: 1or2
        :return:
        """
        if num == 1:
            self.dr.send(wechat_manualtask_taskname, task_name)     # 创建时输入的名称
        elif num == 2:
            print(self.dr.get_ele_content(wechat_manualtask_taskcontent))
            self.dr.send(wechat_manualtask_taskname, change_taskname)   # 修改时输入的名称
            print(self.dr.get_ele_content(wechat_manualtask_taskcontent))

    def input_manualtask_taskcontent(self, num=1):
        """输入手动作业内容"""
        if num == 1:
            self.dr.send(wechat_manualtask_taskcontent, task_content)
        elif num == 2:
            self.dr.send(wechat_manualtask_taskcontent, change_taskcontent)

    def click_manualtask_taskcourse(self):
        """点击手动作业关联课程"""
        self.dr.click(wechat_manualtask_taskcourse)

    def click_taskcourse_one(self):
        """选择手动作业关联课程第一个"""
        self.dr.click(wechat_taskcourse_one)
        self.dr.click(wechat_taskcourse_confirm)

    def click_manualtask_layout(self):
        """点击手动布置作业页面布置按钮"""
        self.dr.click(wechat_manualtask_layout)
        self.dr.get_page_source('tiaos2.html')

    def click_buttomnav_home(self):
        """点击作业详情页底部导航店铺首页按钮"""
        self.dr.click(xiaoe_bottomnav_home)

    def click_xiaoetask_onetask(self):
        """作业列表页点击作业进入详情页"""
        self.dr.click(wechat_xiaoetask_onetask)

    def click_taskdetails_edit(self):
        """作业详情页点击编辑按钮"""
        self.dr.click(wechat_taskdetails_edit)

    def click_manualtask_savechange(self):
        """点击修改作业页面保存修改按钮"""
        self.dr.click(wechat_manualtask_savechange)

    def check_task(self, num=1):
        """检查作业用例是否成功"""
        flag, ele = self.dr.judge_element(wechat_taskdetails_taskname)
        if flag:
            name = self.dr.get_ele_content(wechat_taskdetails_taskname)
            if num == 1:    # 断言创建作业用例
                if name == task_name:
                    print('用例成功，作业名称为：{0}'.format(name))
                    self.dr.get_page_screenshot(self.img_path, case_name='创建作业成功', source='webview')  # 截取当前图片并写入报告
                    log.info('Success find task:"{0}" .'.format(task_name))
                else:
                    print('用例失败')
                    self.dr.get_page_screenshot(self.img_path, case_name='创建作业失败',  source='webview')
                    log.error('Fail user case,not find task:"{0}",The task is:"{1}"'.format(task_name, name))
                    raise Exception('用例失败，没有找到此作业:"{0}"，此页面作业名称为:"{1}"'.format(task_name, name))
            elif num == 2:  # 断言修改作业用例
                if name == change_taskname:
                    print('用例成功，作业名称为：{0}'.format(name))
                    self.dr.get_page_screenshot(self.img_path, case_name='修改作业成功', source='webview')  # 截取当前图片并写入报告
                    log.info('Success find task:"{0}".'.format(change_taskname))
                else:
                    print('用例失败')
                    self.dr.get_page_screenshot(self.img_path, case_name='修改作业失败', source='webview')
                    log.error('Fail user case,not find task:"{0}",The task is:"{1}"'.format(change_taskname, name))
                    raise Exception('用例失败，没有找到此作业:"{0}"，此页面作业名称为:"{1}"'.format(change_taskname, name))
        else:
            self.dr.get_page_screenshot(self.img_path, case_name='用例失败', source='webview')  # 截取当前图片
            log.error('Fail find element:"{0}"'.format(ele))
            raise Exception('用例失败，未找到此元素!')


