import os
from config.getProjectPath import get_project_path
from common.BeautifulReport import BeautifulReport
from common.log import Logger
url = 'https://www.ztestin.com/'
username = '15779582092'
password = '13691916244shao'
path = get_project_path()
log = Logger('testpage.enterZC_page').get_logger()
"""--------------------------------------------------- element ---------------------------------------------------"""
zc_home_login = 'class->nav_fff'    # 众测首页登录按钮
zc_login_user = 'id->login_email'   # 众测登录页面账号框
zc_login_pass = 'id->login_password'    # 众测登录页面密码框
zc_login_button = 'class->lg-login'     # 众测登录页面登录按钮
zc_home_user = 'class->nav_per_wrap'    # 登录后，右上角用户名处元素
zc_home_parttimeask = 'xpath->//div[@class="nav_per_wrap"]/ul/li[1]/a'  # 首页用户悬浮框的兼职任务
zc_task_banner = 'class->task-banner-main'  # 众测任务页面banner图


class enterZC_page():

    def __init__(self, driver):

        self.dr = driver
        self.img = os.path.join(path, 'report', 'screen_shot')

    def enter_zcAnd_login(self, name='test'):
        """打开众测登录,并进入兼职任务页面"""
        try:
            self.into_ZC()
            self.click_home_login()
            self.input_user_name()
            self.input_password()
            self.click_login()
            self.hover_user_window()
            self.click_parttime_task()
            flag, ele = self.dr.judge_element(zc_task_banner)
            if flag:
                pass
            else:
                self.dr.quit()
                self.enter_zcAnd_login()
            self.dr.get_page_screenshot(file_path=self.img, case_name=name + '_登录成功')
            # BeautifulReport.add_test_img3(name + '_登录成功')
        except Exception as e:
            log.error('Fail login')
            log.error(e)
            self.dr.get_page_screenshot(file_path=self.img, case_name=name + '_登录失败')
            # BeautifulReport.add_test_img3(name + '_登录失败')
            raise

    def into_ZC(self):
        """打开众测"""
        self.dr.open_url(url)

    def click_home_login(self):
        """众测首页，点击登录按钮"""
        self.dr.click(zc_home_login)

    def input_user_name(self):
        """众测登录页面，输入账号"""
        self.dr.send(zc_login_user, username)

    def input_password(self):
        """众测登录页面，输入密码"""
        self.dr.send(zc_login_pass, password)

    def click_login(self):
        """众测登录页面，点击登录"""
        self.dr.click(zc_login_button)

    def hover_user_window(self):
        """选择用户名并悬停鼠标"""
        self.dr.hover_element(zc_home_user)     # 用户信息处元素

    def click_parttime_task(self):
        """在用户名鼠标悬停窗口上点击兼职任务"""
        self.dr.click(zc_home_parttimeask)     # 兼职任务

    def check_login(self):
        """"""
        flag, ele = self.dr.judge_element()
        return flag






