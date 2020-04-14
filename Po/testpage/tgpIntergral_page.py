import time
from common.basePage import Page
from common.log import Logger

log = Logger('testpage.tgpIntergral_page').get_logger()

"""---------------------------------------------- element -------------------------------------------------"""
tgp_nav_recommend = 'uiautomator->推荐'   # 导航栏积分按钮
tgp_intergral_icon = 'id->com.tencent.tgp:id/gift_entry_view'    # 积分商城图标
tgp_intergral_checkIn = 'id->com.tencent.tgp:id/tv_sign2'   # 积分商城打卡按钮
tgp_intergral_annal = 'id->com.tencent.tgp:id/record_layout'    # 积分商城记录图标
tgp_intergral_num = 'id->com.tencent.tgp:id/coin_num'   # 积分商城积分总额
tgp_checkIn_window = 'id->com.tencent.tgp:id/tv_paper_score'    # 积分商城打卡成功窗口的积分图标
tgp_intergral_treasure = 'id->com.tencent.tgp:id/lottery_layout'    # 积分商城明日宝藏按钮
tgp_treasure_rule = 'uiautomator->查看详细归规则说明'   # 明日宝藏活动页规则
tgp_rule_window = 'uiautomator->关闭'   # 明日宝藏规则窗口关闭按钮
tgp_treasure_join = 'uiautomator->我要参加'    # 明日宝藏我要参加按钮
tgp_treasure_join2 = 'text->我要参加'    # 明日宝藏我要参加按钮
tgp_intergral_commodity = 'id->com.tencent.tgp:id/gift_img_1'   # 积分商城页第一个积分商品
# 礼包详情页面兑换按钮
tgp_commodity_exchange = \
    'xpath->//android.webkit.WebView[@class="android.webkit.WebView"]/android.view.View/android.view.View[3]'
tgp_commodity_exchange1 = 'uiautomator->10积分兑换'


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
        text = self.dr.get_ele_content(tgp_intergral_checkIn)   # 获取打卡按钮文本，判断今日有无打卡
        if text == '打卡':
            self.dr.click(tgp_intergral_checkIn)    # 选择打卡
            time.sleep(1)
            flag, ele = self.dr.judge_element(tgp_checkIn_window)   # 获取打卡成功窗口，断言是否打卡成功
            if flag:
                num = ele.text
                log.info('Success checkIn, reward intergral :"{0}"'.format(num))
                ele.click()     # 关闭打卡成功窗口
            else:
                log.error('Fail case,msg: not checkIn success window!')
                raise Exception('没有弹出打卡成功窗口，用例失败!')
        else:
            print('今日已打卡过，不可重复打卡!')
            log.info("Checked in today, don't check in again!")

    def click_intergral_annal(self):
        """点击积分页积分记录图标"""
        self.dr.click(tgp_intergral_annal)
        self.dr.back_button(2)
        log.info('Success intergral checkIn, checkIn case end!')

    def click_intergral_treasure(self):
        """点击积分页明日宝藏按钮"""
        print(self.dr.get_app_context())
        self.dr.click(tgp_intergral_treasure)
        print(self.dr.get_app_contexts())

    def click_treasure_rule(self):
        """点击明日宝藏规则"""
        # self.dr.switch_app_context()
        print(self.dr.get_app_contexts())
        self.dr.click(tgp_treasure_rule)

    def click_rule_window(self):
        """点击明日宝藏规则窗口的关闭按钮"""
        self.dr.click(tgp_rule_window)

    def click_treasure_join(self):
        """点击明日宝藏我要参加按钮"""
        self.dr.switch_app_context()
        print(self.dr.get_page_source())
        self.dr.click(tgp_treasure_join2)

    def click_intergral_commodity(self):
        """选择第一个积分商品"""
        print(self.dr.get_app_context())
        self.dr.click(tgp_intergral_commodity)

    def click_commodity_exchange(self):
        """商品页点击兑换"""
        print(self.dr.get_app_contexts())
        self.dr.switch_app_context()
        self.dr.get_page_source()
        self.dr.click(tgp_commodity_exchange1)
