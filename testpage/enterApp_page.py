from common.basePage import Page


class enterApp_page(Page):

    def qq_login(self):
        flag = self.dr.judge_element('id->com.tencent.tgp:id/qqLogin')
        print(flag)
        if flag[0]:
            flag[1].click()
            # self.dr.judge_element('id->com.tencent.tgp:id/qqLogin')
            # self.dr.click('uiautomator->登录')
