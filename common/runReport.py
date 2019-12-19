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

path = get_project_path()
log = Logger('common.runReport').get_logger()


class run_report():
    """
    运行测试套件，并生成报告
    """
    def __init__(self):
        self.reportFile = os.path.join(path, 'report', 'report', 'report.html')     # 测试报告路径
        self.reportFile1 = os.path.join(path, 'report', 'report')  # 测试报告目录
        self.suite_all = caseSuite().set_case_suite()       # 获取测试套件

    def run_html(self):
        """单进程执行用例并输出报告"""
        try:
            date = time.strftime("%Y-%m-%d %H", time.localtime())
            report_file = open(self.reportFile, 'wb')
            runny = HTMLTestRunner(stream=report_file, verbosity=2, title='自动化报告' + date)
            runny.run(self.suite_all)
            log.info('TestCase run end!!!\n')
        except Exception as e:
            log.info('TestCase run fail!!!')
            log.error(e, '\n')
            raise

    def thread_run_html(self):
        """多进程执行用例并输出报告"""
        thread_list = []    # 线程池
        try:
            date = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
            report_name = '\\report' + date + '.html'
            print('report_name', report_name)
            report_file = open(self.reportFile1 + report_name, 'wb')
            for suite in self.suite_all:
                thread = threading.Thread(target=self.thread_run_html2, args=(report_file, date, suite))
                thread_list.append(thread)  # 线程加入线程池

            for th in thread_list:
                th.start()  # 启动线程
                time.sleep(3)

            for th in thread_list:
                th.join()   # 等待线程结束
            log.info('TestCase run end!!!\n')
        except Exception as e:
            log.info('TestCase run fail!!!')
            log.error(e, '\n')
            raise

    def thread_run_html2(self, report_file, date, suite):
        """多进程执行用例并输出报告"""
        try:
            print('开始')
            runny = HTMLTestRunner(stream=report_file, verbosity=2, title='自动化报告' + date)
            runny.run(suite)
            log.info('TestCase run end!!!\n')
        except Exception as e:
            log.info('TestCase run fail!!!')
            log.error(e, '\n')
            raise

    @threads(2)
    def thread_run_Beautifuhtml(self, suite):
        """多进程执行用例并输出漂亮报告"""
        name = '\\' + time.strftime('%Y-%m-%d-%H_%M_%S')
        result = BeautifulReport(suite)
        result.report(filename=name, description='测试deafult报告', log_path=self.reportFile1)

    def more_threads2(self):
        for i in self.suite_all:
            print(i)
            self.thread_run_Beautifuhtml(i)

    def more_threads(self):
        """多线程函数"""
        thread_list = []  # 线程池
        for suite in self.suite_all:
            thread = threading.Thread(target=self.thread_run_Beautifuhtml, args=(suite))
            thread_list.append(thread)

        for thread in thread_list:
            thread.start()

        for thread in thread_list:
            thread.join()
