from common import basePage


class enterZC_page(basePage.Page):

    def into_ZC(self):
        """打开百度页"""
        url = 'https://www.ztestin.com/'
        self.dr.open_url(url)

    def click_login_button(self):
        """众测首页，点击登录按钮"""
        self.dr.click('class->nav_fff')

    def input_user_name(self):
        """众测登录页面，输入账号"""
        self.dr.send('id->login_email', '15779582092')

    def input_password(self):
        """众测登录页面，输入密码"""
        self.dr.send('id->login_password', '13691916244shao')

    def click_login(self):
        """众测登录页面，点击登录"""
        self.dr.click('class->lg-login')

    def click_parttime_task(self):
        """登录成功后的首页， 悬停在用户上点击兼职任务"""
        self.dr.hover_element('class->nav_per_wrap')     # 用户信息处元素
        self.dr.click('xpath->//div[@class="nav_per_wrap"]/ul/li[1]/a')     # 兼职任务

    def swipe_page(self):
        """兼职任务页面，向下滑动页面"""
        self.dr.js('window,scrollBy(0, 500)')   # 滑动500px

    def click_filter_task(self):
        """兼职任务页面，选择可参与筛选"""
        self.dr.click('xpath->//div[@class="zhall-wrap"]/div[1]/ul[2]/li[3]')

    def click_task(self):
        """筛选后选择第一个任务"""
        flag, ele = self.dr.judge_element('xpath->//div[@class="no-data"]/p')   # 判断是否有可参与任务
        if not flag:
            self.dr.click('xpath->//ul[@class="hall-list-wrap"]/li[1]/a/ul')    # 选择第一个任务
        else:
            print(ele.text)




