from common import basePage
from common.log import Logger
from common.BeautifulReport import BeautifulReport

log = Logger('testpage.ZCtasg_page').get_logger()
"""-------------------------------------------------- element --------------------------------------------------"""
js_slide = 'window,scrollBy(0, 500)'    # js向下滑动命令，滑动500px
zc_task_can = 'xpath->//div[@class="zhall-wrap"]/div[1]/ul[2]/li[3]'    # 众测任务页面，筛选框中可参与
zc_cantask_result = 'xpath->//div[@class="no-data"]/p'      # 可参与任务筛选无结果时，提示文字的元素
zc_cantask_one = 'xpath->//ul[@class="hall-list-wrap"]/li[1]/a/ul'  # 可参与任务中第一个任务
zc_test_honor = 'xpath->//ul[@class="nav_ul"]/li[3]/a'   # 众测荣誉按钮
zc_honor_title = 'class->rangking_zhou'  # 众测荣誉页面榜单名称


class ZCtask_page(basePage.Page):

    def swipe_page(self):
        """兼职任务页面，向下滑动页面"""
        self.dr.js(js_slide)

    def click_filter_task(self):
        """兼职任务页面选择可参与筛选,并判断用例是否成功"""
        self.dr.click(zc_task_can)

    @BeautifulReport.add_test_img('test_筛选任务_有结果时', '筛选任务_无结果时')
    def check_filtertask_result(self):
        """筛选后选择第一个任务"""
        flag, ele = self.dr.judge_element(zc_cantask_result)   # 判断是否有可参与任务
        if flag:
            text = self.dr.get_ele_content(zc_cantask_result)
            print('用例成功!'.format(text))
            log.info('Success filter task case, result:"{0}"'.format(text))
            self.dr.get_page_screenshot(file_path=self.img_path, case_name='筛选任务_无结果时', source='other')
        else:
            print('用例成功!')
            log.info('Success filter task case,')
            self.dr.get_page_screenshot(file_path=self.img_path, case_name='筛选任务_有结果时', source='other')

    @BeautifulReport.add_test_img('test_众测荣誉_成功', 'test_众测荣誉_失败')
    def click_zc_honor(self):
        """点击测试荣誉按钮"""
        self.dr.click(zc_test_honor)
        flag, ele = self.dr.judge_element(zc_honor_title)
        if flag:
            self.dr.win_scroll_page('0, 300')   # 滑动页面
            print('用例成功!')
            log.info('Success case！')
            self.dr.get_page_screenshot(file_path=self.img_path, case_name='众测荣誉_成功',  source='other')
        else:
            print('用例失败!')
            log.info('fail case！')
            self.dr.get_page_screenshot(file_path=self.img_path, case_name='众测荣誉_失败',  source='other')
            assert flag



