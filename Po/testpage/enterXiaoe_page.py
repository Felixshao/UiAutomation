# _*_ config: utf-8 _*_
# enterXiaoe_poage.py

from common.basePage import Page


wechat_nav_my = [0.879, 0.955]      # 微信导航栏我的
wechat_my_shouc = 'text->收藏'    # 微信我的收藏
wechat_shouc_search = 'description->搜索'     # 微信收藏搜索图标
wechat_search_one = 'id->com.tencent.mm:id/bd'  # 搜索后第一个结果


class enterXiaoe_page(Page):

    def wechat_xiaoe_zhunxianwang(self):
        """进入微信小鹅通准线网"""
        self.uiau.click(wechat_nav_my)  # 点击我的
        self.uiau.click(wechat_my_shouc)
        self.uiau.click(wechat_shouc_search)
        self.uiau.send_keys('准线网')
        self.uiau.click(wechat_search_one)