from common import basePage
from common.log import Logger
from common.BeautifulReport import BeautifulReport

log = Logger('testpage.ZCtasg_page').get_logger()
"""-------------------------------------------------- element --------------------------------------------------"""
js_slide = 'window,scrollBy(0, 500)'    # js向下滑动命令，滑动500px
zc_nav_task = 'xpath->//ul[@class="nav_ul"]/li[2]/a'    # 任务页面导航栏众测任务
zc_task_can = 'xpath->//div[@class="zhall-wrap"]/div[1]/ul[2]/li[3]/a'    # 众测任务页面，项目状态选可参与
zc_task_processing = 'xpath->//div[@class="zhall-wrap"]/div[1]/ul[2]/li[4]/a'     # 众测任务页面，项目状态选进行中
zc_task_end = 'xpath->//div[@class="zhall-wrap"]/div[1]/ul[2]/li[5]/a'  # 众测任务页面，项目状态选已结束
zc_task_bugexplore = 'xpath->//div[@class="zhall-wrap"]/div[1]/ul[1]/li[3]/a'  # 众测任务页面，项目类型选bug探索
zc_task_caserun = 'xpath->//div[@class="zhall-wrap"]/div[1]/ul[1]/li[4]/a'  # 众测任务页面，项目类型选用例执行
zc_task_casedesign = 'xpath->//div[@class="zhall-wrap"]/div[1]/ul[1]/li[5]/a'  # 众测任务页面，项目类型选用例设计
zc_task_functest = 'xpath->//div[@class="zhall-wrap"]/div[1]/ul[1]/li[6]/a'  # 众测任务页面，项目类型选功能测试
zc_task_resident = 'name->resident'     # 众测任务页面，项目类型选驻场任务
zc_resident_task = 'xpath->//select[@name="resident"]/option[1]'     # 众测任务页面，项目类型选驻场任务下拉框的驻场任务
zc_resident_hardware = 'xpath->//select[@name="resident"]/option[2]'     # 众测任务页面，项目类型选驻场任务下拉框的硬件连通
zc_resident_compatible = 'xpath->//select[@name="resident"]/option[3]'     # 众测任务页面，项目类型选驻场任务下拉框的遍历兼容
zc_cantask_result = 'xpath->//div[@class="no-data"]/p'      # 可参与任务筛选无结果时，提示文字的元素
zc_cantask_one = 'xpath->//ul[@class="hall-list-wrap"]/li[1]/a/ul'  # 可参与任务中第一个任务


class ZCtask_page(basePage.Page):

    def click_nav_zctask(self):
        """众测任务页面，众测任务按钮"""
        self.dr.click(zc_nav_task)

    def swipe_page(self):
        """兼职任务页面，向下滑动页面"""
        self.dr.js(js_slide)

    def click_filter_cantask(self):
        """兼职任务页面选择可参与筛选"""
        self.dr.click(zc_task_can)
        self.check_filtertask_result1('筛选可参与任务')

    def click_filter_protask(self):
        """兼职任务页面选择进行中筛选"""
        self.dr.click(zc_task_processing)
        self.check_filtertask_result1('筛选进行中任务')

    def click_filter_endtask(self):
        """兼职任务页面选择已结束筛选"""
        self.dr.click(zc_task_end)
        self.check_filtertask_result1('筛选已结束任务')

    def click_filter_bugexplore(self):
        """兼职任务页面选择Bug探索筛选"""
        self.dr.click(zc_task_bugexplore)
        self.check_filtertask_result1('筛选Bug探索任务')

    def click_filter_caserun(self):
        """兼职任务页面选择用例执行筛选"""
        self.dr.click(zc_task_caserun)
        self.check_filtertask_result1('筛选用例执行任务')

    def click_filter_casedesign(self):
        """兼职任务页面选择用例设计筛选"""
        self.dr.click(zc_task_casedesign)
        self.check_filtertask_result1('筛选用例设计任务')

    def click_filter_functest(self):
        """兼职任务页面选择功能测试筛选"""
        self.dr.click(zc_task_functest)
        self.check_filtertask_result1('筛选功能测试任务')

    def click_filter_resident(self):
        """兼职任务页面点击驻场任务"""
        self.dr.click(zc_task_resident)

    def click_resident_task(self):
        """兼职任务页面点击驻场任务下拉框的驻场任务"""
        self.dr.click(zc_resident_task)
        self.check_filtertask_result1('筛选驻场任务')

    def click_resident_hardware(self):
        """兼职任务页面点击驻场任务下拉框的硬件连通"""
        self.dr.click(zc_resident_hardware)
        self.check_filtertask_result1('筛选硬件连通任务')

    def click_resident_compatible(self):
        """兼职任务页面点击驻场任务下拉框的遍历兼容"""
        self.dr.click(zc_resident_compatible)
        self.check_filtertask_result1('筛选遍历兼容任务')

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

    def check_filtertask_result1(self, name='筛选可参与任务'):
        """判断用例是否成功"""
        flag, ele = self.dr.judge_element(zc_cantask_result)   # 判断是否有可参与任务
        if flag:
            text = self.dr.get_ele_content(zc_cantask_result)
            print('用例成功,目前无任务，提示文案为:'.format(text))
            log.info('Success filter task case, result:"{0}"'.format(text))
            self.dr.get_page_screenshot(file_path=self.img_path, case_name=name + '_无结果时')
            BeautifulReport.add_test_img3(name + '_无结果时')
        else:
            print('用例成功,{0}完成!'.format(name))
            log.info('用例成功,{0}完成!'.format(name))
            self.dr.get_page_screenshot(file_path=self.img_path, case_name=name + '_有结果时')
            BeautifulReport.add_test_img3(name + '_有结果时')



