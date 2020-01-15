from common.BeautifulReport import BeautifulReport
from common.basePage import Page
from common.log import Logger

log = Logger('testpage.ZCservice_page').get_logger()
zc_service_url = 'https://www.ztestin.com/zc'   # 众测服务页面网址
"""------------------------------------------- element --------------------------------------------------------"""
zc_nav_service = 'xpath->//ul[@class="nav_ul"]/li[4]/a'     # 众测任务页面，导航栏众测服务


class ZCservice_page(Page):

    def click_nav_service(self):
        """ 众测任务页面，点击导航栏众测服务"""
        self.dr.click(zc_nav_service)
        self.check_case()

    def check_case(self, name='进入众测服务'):
        """检查是否成功"""
        url = self.dr.get_page_url()
        if url == zc_service_url:
            print('{0}用例成功!'.format(name))
            log.info('{0}用例成功!'.format(name))
            self.dr.get_page_screenshot(file_path=self.img_path, case_name=name + '_成功')
            BeautifulReport.add_test_img3(name + '_成功')
        else:
            print('{0}用例失败'.format(name))
            log.info('{0}用例失败!'.format(name))
            self.dr.get_page_screenshot(file_path=self.img_path, case_name=name + '_失败')
            BeautifulReport.add_test_img3(name + '_失败')
