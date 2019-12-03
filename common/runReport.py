import os
import time
from common.HTMLTestRunner import HTMLTestRunner
from common.caseSuite import caseSuite
from config.getProjectPath import get_project_path
from common.log import Logger

path = get_project_path()
log = Logger('common.runReport').get_logger()


class run_report():
    """
    运行测试套件，并生成报告
    """
    def __init__(self):
        self.reportFile = os.path.join(path, 'report', 'report', 'report.html')     # 测试报告路径
        self.suite = caseSuite().set_case_suite()       # 获取测试套件

    def run_html(self):
        try:
            date = time.strftime("%Y-%m-%d %H", time.localtime())
            report_file = open(self.reportFile, 'wb')
            runny = HTMLTestRunner(stream=report_file, verbosity=2, title='自动化报告' + date)
            runny.run(self.suite)
            log.info('TestCase run end!!!\n')
        except Exception as e:
            log.info('TestCase run fail!!!')
            log.error(e, '\n')
            raise

