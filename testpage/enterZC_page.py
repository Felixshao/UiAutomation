from common import basePage

url = 'https://www.ztestin.com/'
username = '15779582092'
password = '13691916244shao'
"""--------------------------------------------------- element ---------------------------------------------------"""
zc_home_login = 'class->nav_fff'    # 众测首页登录按钮
zc_login_user = 'id->login_email'   # 众测登录页面账号框
zc_login_pass = 'id->login_password'    # 众测登录页面密码框
zc_login_button = 'class->lg-login'     # 众测登录页面登录按钮
zc_home_user = 'class->nav_per_wrap'    # 登录后，右上角用户名处元素


class enterZC_page(basePage.Page):

    def enter_zcAnd_login(self):
        """打开众测登录,并进入兼职任务页面"""
        self.into_ZC()
        self.click_home_login()
        self.input_user_name()
        self.input_password()
        self.click_login()
        self.hover_user_window()
        self.click_parttime_task()

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
        self.dr.click('xpath->//div[@class="nav_per_wrap"]/ul/li[1]/a')     # 兼职任务






