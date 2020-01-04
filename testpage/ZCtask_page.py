from common import basePage
from common.log import Logger
from common.BeautifulReport import BeautifulReport

log = Logger('testpage.ZCtasg_page').get_logger()
"""-------------------------------------------------- element --------------------------------------------------"""
js_slide = 'window,scrollBy(0, 500)'    # js向下滑动命令，滑动500px
zc_task_can = 'xpath->//div[@class="zhall-wrap"]/div[1]/ul[2]/li[3]/a'    # 众测任务页面，项目状态选可参与
zc_task_processing = 'xpath->//div[@class="zhall-wrap"]/div[1]/ul[2]/li[4]/a'     # 众测任务页面，项目状态选进行中
zc_task_end = 'xpath->//div[@class="zhall-wrap"]/div[1]/ul[2]/li[5]/a'  # 众测任务页面，项目状态选已结束
zc_cantask_result = 'xpath->//div[@class="no-data"]/p'      # 可参与任务筛选无结果时，提示文字的元素
zc_cantask_one = 'xpath->//ul[@class="hall-list-wrap"]/li[1]/a/ul'  # 可参与任务中第一个任务


class ZCtask_page(basePage.Page):

    def swipe_page(self):
        """兼职任务页面，向下滑动页面"""
        self.dr.js(js_slide)

    def click_filter_cantask(self):
        """兼职任务页面选择可参与筛选"""
        self.dr.click(zc_task_can)

    def click_filter_protask(self):
        """兼职任务页面选择进行中筛选"""
        self.dr.click(zc_task_processing)

    def click_filter_endtask(self):
        """兼职任务页面选择已结束筛选"""
        self.dr.click(zc_task_end)

    def check_filtertask_result(self, source='can'):
        """判断用例是否成功"""
        flag, ele = self.dr.judge_element(zc_cantask_result)   # 判断是否有可参与任务
        if flag:
            text = self.dr.get_ele_content(zc_cantask_result)
            print('用例成功,目前无任务，提示文案为:'.format(text))
            log.info('Success filter task case, result:"{0}"'.format(text))
            if source == 'can':
                self.dr.get_page_screenshot(file_path=self.img_path, case_name='筛选可参与任务_无结果时', source='other')
                BeautifulReport.add_test_img3('筛选可参与任务_无结果时')
            elif source == 'pro':
                self.dr.get_page_screenshot(file_path=self.img_path, case_name='筛选进行中任务_无结果时', source='other')
                BeautifulReport.add_test_img3('筛选进行中任务_无结果时')
            elif source == 'end':
                self.dr.get_page_screenshot(file_path=self.img_path, case_name='筛选已结束任务_无结果时', source='other')
                BeautifulReport.add_test_img3('筛选已结束任务_无结果时')
        else:
            if source == 'can':
                print('用例成功,成功筛选出可参与任务!')
                log.info('Success filter canjoin task case,')
                self.dr.get_page_screenshot(file_path=self.img_path, case_name='筛选可参与任务_有结果时', source='other')
                BeautifulReport.add_test_img3('筛选可参与任务_有结果时')
            elif source == 'pro':
                print('用例成功,成功筛选出进行中任务!')
                log.info('Success filter processing task case,')
                self.dr.get_page_screenshot(file_path=self.img_path, case_name='筛选进行中任务_有结果时', source='other')
                BeautifulReport.add_test_img3('筛选进行中任务_有结果时')
            elif source == 'end':
                print('用例成功,成功筛选出已结束任务!')
                log.info('Success filter end task case,')
                self.dr.get_page_screenshot(file_path=self.img_path, case_name='筛选已结束任务_有结果时', source='other')
                BeautifulReport.add_test_img3('筛选已结束任务_有结果时')
            else:
                print('用例失败，判断来源不详,source:"{0}"'.format(source))
                log.info('Fali filter task case,unknown source:"{0}"'.format(source))
                self.dr.get_page_screenshot(file_path=self.img_path, case_name='筛选任务_来源未知', source='other')
                BeautifulReport.add_test_img3('筛选任务_来源未知')
                assert flag



