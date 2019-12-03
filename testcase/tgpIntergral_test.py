from common.Mymoible import Mymobile
from testpage.enterApp_page import enterApp_page
from testpage.tgpIntergral_page import tgpIntergral_page


class tgpIntergral_test(Mymobile):

    def test1_intergral_checkIn(self):
        """
        积分打卡
        :return:
        """
        app = tgpIntergral_page(self.dr)
        app.click_nav_recommend()
        app.click_intergral_icon()
        app.click_intergral_checkIn()
        app.click_intergral_annal()

    def test2_intergral_checkIn(self):
        """
        积分打卡
        :return:
        """
        app = tgpIntergral_page(self.dr)
        app.click_nav_recommend()
        app.click_intergral_icon()
        app.click_intergral_checkIn()
        app.click_intergral_annal()

