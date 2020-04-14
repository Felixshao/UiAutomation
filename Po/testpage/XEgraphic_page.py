from common.basePage import Page

xe_shop_one = 'xpath->//div[@class="shop-list-wrapper"]/div[2]/a[1]'    # 选择第一个店铺
xe_oneshop_graphic = 'xpath->//div[@class="leftsidebarWrap"]/div[4]/div[2]/ul/li[1]/span'   # 选择图书


class XEgraphic_page(Page):

    def xe_shop_one(self):

        self.dr.click(xe_shop_one)

    def xe_oneshop_graphic(self):

        self.dr.click(xe_oneshop_graphic)