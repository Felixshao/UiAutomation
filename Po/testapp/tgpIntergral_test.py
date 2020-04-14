from common.Mymoible import Mymobile
from Po.testpage.tgpIntergral_page import tgpIntergral_page


class tgpIntergral_test(Mymobile):

    def test1_intergral_checkIn(self):
        """
        积分商城打卡
        :return:
        """
        global app
        app = tgpIntergral_page(self.dr)
        app.click_nav_recommend()
        app.click_intergral_icon()
        # app.click_intergral_checkIn()
        # app.click_intergral_annal()

    def test2_intergral_treasure(self):
        """
        参与积分商城明日宝藏
        :return:
        """
        app = tgpIntergral_page(self.dr)
        app.click_nav_recommend()
        app.click_intergral_icon()
        # app.click_intergral_treasure()
        # app.click_treasure_rule()
        # app.click_rule_window()
        # app.click_treasure_join()

    def test3_intergral_exchange(self):
        """积分商城兑换商品"""
        app = tgpIntergral_page(self.dr)
        app.click_nav_recommend()
        app.click_intergral_icon()
        app.click_intergral_commodity()
        app.click_commodity_exchange()





