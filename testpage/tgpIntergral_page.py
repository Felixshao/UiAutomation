import time
from common.basePage import Page
from common.log import Logger

log = Logger('testpage.tgpIntergral_page').get_logger()

"""---------------------------------------------- element -------------------------------------------------"""
tgp_nav_recommend = 'uiautomator->推荐'
tgp_intergral_icon = 'id->com.tencent.tgp:id/signId'
tgp_intergral_checkIn = 'id->com.tencent.tgp:id/tv_sign2'
tgp_intergral_annal = 'id->com.tencent.tgp:id/record_layout'
tgp_intergral_num = 'id->com.tencent.tgp:id/coin_num'


class tgpIntergral_page(Page):

    def click_nav_recommend(self):
        """
        点击导航栏推荐
        :return:
        """
        self.dr.click(tgp_nav_recommend)

    def click_intergral_icon(self):
        """点击推荐页积分图标"""
        self.dr.click(tgp_intergral_icon)

    def click_intergral_checkIn(self):
        """点击积分页打卡按钮,并断言"""
        text = self.dr.get_ele_content(tgp_intergral_checkIn)
        if text == '打卡':
            current_intergral = self.dr.get_ele_content(tgp_intergral_num)
            self.dr.click(tgp_intergral_checkIn)
            time.sleep(1)
            intergral = self.dr.get_ele_content(tgp_intergral_num)
            if current_intergral == intergral:
                print('打卡前后积分一致，用例失败!')
                log.error('Fail case,msg: intergral not increased')
                raise Exception('打卡前后积分一致，用例失败!')
            log.info('Success checkIn, intergral num:{0}'.format(intergral))
        else:
            print('今日已打卡过，不可重复打卡!')
            log.info("Checked in today, don't check in again!")

    def click_intergral_annal(self):
        """点击积分页积分记录图标"""
        self.dr.click(tgp_intergral_annal)

