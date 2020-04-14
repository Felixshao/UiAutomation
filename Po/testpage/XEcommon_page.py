import time
from common.basePage import Page
from common.slider_captcha import slider_captcha

url = 'https://admin.xiaoe-tech.com/login_page?reg_source=0101&xeuti=ituex#/acount'
user = '15779582092'
password = '123456'
"""--------------------------------------------------- element ---------------------------------------------------"""
xe_user_name = 'xpath->//div[@class="phoneWrapper"]/div/input'      # 账号框
xe_pass_word = 'xpath->//div[@class="passwordWrapper"]/div/input'   # 密码框
xe_login_button = 'class->login-btn'    # 登录按钮
xe_captcha_iframe = 'tcaptcha_iframe'   # 滑块验证码iframe


class XEcommon_page(Page):

    def login(self):
        """登录小鹅通"""
        # 浏览器访问登录页面
        self.dr.open_url(url)
        handle = self.dr.get_current_handle()
        # 输入账号密码，点击登陆按钮
        self.dr.send(xe_user_name, user)
        self.dr.send(xe_pass_word, password)
        self.dr.click(xe_login_button)
        # 弹出滑动验证码，切换进入iframe
        time.sleep(2)
        self.dr.switch_iframe(xe_captcha_iframe)
        # 开始验证滑块验证码
        slider_captcha(self.dr, handle, xe_captcha_iframe)
