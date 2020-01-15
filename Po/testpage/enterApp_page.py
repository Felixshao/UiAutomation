import time
from common.basePage import Page
from common.log import Logger
from config.getMobile import get_mobile

log = Logger('testpage.enterApp').get_logger()
phone = get_mobile()[1]
user = '2310563268'
password = '13691916244shaos'
nickname = '12345678998'

"""--------------------------------------- element ----------------------------------------------------"""
tgp_login_button = 'id->com.tencent.tgp:id/qqLogin'     # tgp登录页面qq登录按钮
tgp_nav_my = 'uiautomator->我的'      # tgp导航栏我的
tgp_loginPop_login = 'id->com.tencent.tgp:id/tv_positive'    # tgp内页弹窗马上登录按钮
tgp_updatePop_later = 'id->com.tencent.tgp:id/tv_negative'  # tgp更新弹窗以后再说按钮
tgp_infomation_confirm = 'id->com.tencent.tgp:id/registerOKButton'  # tgp完善资料页面确认按钮
tgp_infomation_prompt = 'id->com.tencent.tgp:id/registerNickTipId'  # tgp完善资料页面昵称提示文案
tgp_infomation_nickname = 'id->com.tencent.tgp:id/nickEditId'   # tgp完善资料页面昵称框
tgp_qq_warrant = 'uiautomator->登录'  # qq授权登录页面登录按钮
tgp_qqLogin_user = 'accessibility id->请输入QQ号码或手机或邮箱'    # qq登录页面账号框
tgp_qqLogin_pass = 'id->com.tencent.mobileqq:id/password'   # qq登录页面密码框
tgp_qqLogin_button = 'id->com.tencent.mobileqq:id/login'    # qq登录页面登录按钮


class enterApp_page(Page):

    def tgp_login_main(self):
        """
        tgp登录主函数
        :return:
        """
        flag, ele = self.dr.judge_element(tgp_login_button)     # 判断app是否已登录
        try:
            if flag:
                self.qq_login(ele)
                self.judeg_first_login()
                self.lgnore_update()
            else:
                self.lgnore_update()
                self.dr.click(tgp_nav_my)
                flag, loginPop_login = self.dr.judge_element(tgp_loginPop_login)
                if flag:
                    loginPop_login.click()
                    self.qq_login()
                    self.judeg_first_login()
                log.info('"{0}" is logged in!'.format(phone['Appname']))
        except Exception as e:
            log.info('An error occurred, please see the reason!')
            log.error(e)
            raise

    def lgnore_update(self):
        """
        首页判断有无更新弹窗，有则忽略
        :return:
        """
        # 首次登录的qq进入资料完善页面，找到确认按钮
        flag, ele = self.dr.judge_element(tgp_updatePop_later)  # 找到弹窗以后再说按钮
        if flag:
            ele.click()
            log.info('Success find update window, update later.')

    def judeg_first_login(self):
        """
        判断是否为首次登录，首次登录完善资料
        :return:
        """
        flag, infomation = self.dr.judge_element(tgp_infomation_confirm)  # 完善资料页面确认按钮
        if flag:
            infomation.click()
            try:
                while True:
                    text = self.dr.get_ele_content(tgp_infomation_prompt)    # 查看提交资料提示
                    if text == '已使用':
                        self.dr.send(tgp_infomation_nickname, nickname)     # 完善资料页面，输入新昵称
                        infomation.click()  # 确认资料
            except Exception as e:
                log.info('Success complete material!')
                log.error(e)
                raise

    def qq_login(self, ele=None):
        """
        使用qq登录tgp
        :param ele:
        :return:
        """
        if ele is None:
            ele = self.dr.find_element(tgp_login_button)
        log.info('"{0}" is not logged in, start the login operation.'.format(phone['Appname']))
        ele.click()
        flag, login_button = self.dr.judge_element(tgp_qq_warrant)  # 判断手机qq是否已登录,找到授权qq登录按钮
        flag2, qq_user = self.dr.judge_element(tgp_qqLogin_user)  # 找到qq登录页面账号框
        if flag:
            login_button.click()
            log.info('Success logged into the "{0}"'.format(phone['Appname']))
        elif flag2:
            qq_user.send_keys(user)
            self.dr.send(tgp_qqLogin_pass, password)  # 找到qq登录页面密码框
            self.dr.click('id->com.tencent.mobileqq:id/login')  # 点击登录
            log.info('Success log in to the "{0}" useing qq:{1}'.format(phone['Appname'], user))
        else:
            print('未找到qq，请手动下载并安装qq!')
            log.info('Fail: qq not found orthe unknown error! ')



