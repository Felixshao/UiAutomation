import time

from common import basePage
from common.log import Logger
from common.BeautifulReport import BeautifulReport

log = Logger('testpage.ZChonor_page').get_logger()
"""-------------------------------------------------- element --------------------------------------------------"""
zc_test_honor = 'xpath->//ul[@class="nav_ul"]/li[3]/a'   # 任务页面，众测荣誉tab
zc_honor_title = 'class->rangking_zhou'  # 众测荣誉页面榜单名称
zc_honor_tablename = 'class->rank_table_name'   # 榜单上的用户昵称
zc_honor_listdate = 'class->testin-select-set'  # 筛选榜单日期
zc_honor_lastterm = 'xpath->//div[@class="testin-select"]/ul/li[2]'  # 筛选上一期榜单
zc_honor_lastissue = 'xpath->//div[@class="testin-select"]/ul/li[3]'  # 筛选上上期榜单


class ZChonor_page(basePage.Page):

    def click_zc_honor(self):
        """点击测试荣誉按钮"""
        self.dr.click(zc_test_honor)

    def click_zchonor_filter(self):
        """点击荣誉榜单期数筛选按钮"""
        self.dr.click(zc_honor_listdate)

    def select_honor_lastterm(self):
        """选择上一期榜单"""
        flag = self.dr.judge_element_visibility(zc_honor_lastterm)  # 等待元素为可见
        if flag:
            self.dr.win_scroll_page('0, 300')  # 向下滑动300px
            text = self.dr.get_ele_content(zc_honor_lastterm)
            self.dr.click(zc_honor_lastterm)
            self.chick_zc_honor(text)
        else:
            raise Exception('Not find or Not click zc_honor_lastterm:"{0}"'.format(zc_honor_lastterm))

    def select_honor_lastissue(self):
        """选择上上期榜单"""
        flag = self.dr.judge_element_visibility(zc_honor_lastissue)  # 等待元素为可见
        if flag:
            self.dr.win_scroll_page('0, 300')  # 向下滑动300px
            text = self.dr.get_ele_content(zc_honor_lastissue)
            self.dr.click(zc_honor_lastissue)
            self.chick_zc_honor(text)
        else:
            raise Exception('Not find or Not click zc_honor_lastterm:"{0}"'.format(zc_honor_lastissue))

    def chick_zc_honor(self, name='最新一期'):
        """
        检查是否成功获取到荣誉榜单
        param:name, 输入需要检查的榜单期数
        """
        try:
            honor_list = {}
            eles = self.dr.finds_element(zc_honor_tablename)
            for num in range(1, len(eles)+1):
                text = self.dr.get_ele_content(eles[num-1])
                honor_list[num] = text
            print('用例成功,"{0}荣誉榜单"为:\n{1}'.format(name, honor_list))
            log.info('Success case！')
            self.dr.get_page_screenshot(file_path=self.img_path, case_name=name + '荣誉榜单_成功')
            BeautifulReport.add_test_img3(name + '荣誉榜单_成功')
        except Exception as e:
            print('查看"{0}荣誉榜单"用例失败!'.format(name))
            log.error('Fail view newhonor case！')
            log.error(e)
            self.dr.get_page_screenshot(file_path=self.img_path, case_name=name + '荣誉榜单_失败')
            BeautifulReport.add_test_img3(name + '荣誉榜单_失败')
            raise



