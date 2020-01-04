import os
import time
import threading
from common.HTMLTestRunner2 import HTMLTestRunner
from common.caseSuite import caseSuite
from config.getProjectPath import get_project_path
from common.log import Logger
from selenium import webdriver
from common.BeautifulReport import BeautifulReport
from tomorrow import threads
from multiprocessing import Process
import multiprocessing as mp
import queue

path = get_project_path()
log = Logger('common.runReport').get_logger()
# lock = threading.Lock()
q = mp.Queue()


class run_report():
    """
    运行测试套件，并生成报告
    """
    def __init__(self):
        global suite_all2
        self.reportFile = os.path.join(path, 'report', 'report', 'report.html')     # 测试报告路径
        self.reportFile1 = os.path.join(path, 'report', 'report')  # 测试报告目录
        self.suite_all = caseSuite().set_case_suite()       # 获取测试套件
        self.report_result = []

    def run_html(self, report_name='report', suite=None, ):
        """单进程执行用例并输出报告"""
        try:
            # lock.acquire()
            file_name = os.path.join(self.reportFile1, report_name + '.html')
            date = time.strftime("%Y-%m-%d %H", time.localtime())
            report_file = open(file_name, 'wb')
            runny = HTMLTestRunner(stream=report_file, verbosity=2, title='自动化报告' + date)
            if suite is None:
                runny.run(self.suite_all)
            else:
                runny.run(suite)
            log.info('TestCase run end!!!\n')
        except Exception as e:
            log.info('TestCase run fail!!!')
            log.error(e, '\n')
            raise
        # finally:
        #     lock.release()

    def more_report(self):
        num = 1
        threads = []
        for i in self.suite_all:
            thread = threading.Thread(target=self.run_html, args=('report' + str(num), i))
            threads.append(thread)
            # self.run_html(suite=i, report_name='report' + str(num))
            # num += 1

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

# --------------------------------------------- process ---------------------------------------------------------------
    def thread_run_Beautifuhtml(self, suite=None, q=None, process=False):
        """执行用例并输出漂亮报告方法"""
        try:
            # lock.acquire()
            name = '\\report1'
            if not process:
                suite = self.suite_all
            result = BeautifulReport(suite, verbosity=2)
            results = result.report(filename=name, description='测试deafult报告', log_path=self.reportFile1, process=process)
            if process:
                q.put(results)
        except Exception as e:
            log.error(e)
            raise
        # finally:
        #     lock.release()

    def moreProcess_report(self):
        """多进程执行用例并输出报告"""
        log.info('start moreProcess!')
        threads = []
        for i in self.suite_all:
            thread = Process(target=self.thread_run_Beautifuhtml, args=(i, q, True))
            threads.append(thread)
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
            self.report_result.append(q.get())
        dict = {}
        total = []
        for i in range(len(self.report_result)):
            if i == 0:
                dict['testName'] = self.report_result[0]['testName']
                dict['beginTime'] = self.report_result[0]['beginTime']
                total.append((self.report_result[i]['totalTime']))
                dict['testPass'] = self.report_result[i]['testPass']
                dict['testResult'] = self.report_result[i]['testResult']
                dict['testAll'] = self.report_result[i]['testAll']
                dict['testFail'] = self.report_result[i]['testFail']
                dict['testSkip'] = self.report_result[i]['testSkip']
                dict['testError'] = self.report_result[i]['testError']
            else:
                total.append((self.report_result[i]['totalTime']))
                dict['testPass'] += self.report_result[i]['testPass']
                dict['testResult'] += self.report_result[i]['testResult']
                dict['testAll'] += self.report_result[i]['testAll']
                dict['testFail'] += self.report_result[i]['testFail']
                dict['testSkip'] += self.report_result[i]['testSkip']
                dict['testError'] += self.report_result[i]['testError']
        dict['totalTime'] = max(total)
        log.info('MoreProcess end.start Transfer data and generate reports...')
        result = BeautifulReport(self.suite_all)
        result.stop_output(log_path=self.reportFile1 + '\\', FIELDS=dict)
        log.info('End of the project.Please see the report!')