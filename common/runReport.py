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
lock = threading.Lock()


class run_report():
    """
    运行测试套件，并生成报告
    """
    def __init__(self):
        self.reportFile = os.path.join(path, 'report', 'report', 'report.html')     # 测试报告路径
        self.reportFile1 = os.path.join(path, 'report', 'report')  # 测试报告目录
        self.suite_all = caseSuite().set_case_suite()       # 获取测试套件

    def run_html(self, suite=None, report_name='report'):
        """单进程执行用例并输出报告"""
        try:
            lock.acquire()
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
        finally:
            lock.release()

    def more_report(self):
        num = 1
        threads = []
        for i in self.suite_all:
            thread = threading.Thread(target=self.thread_run_Beautifuhtml, args=(i, 'report' + str(num)))
            threads.append(thread)
            # self.run_html(suite=i, report_name='report' + str(num))
            # num += 1

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

# --------------------------------------------- threads ---------------------------------------------------------------

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
            runny = HTMLTestRunner(stream=report_file, verbosity=2, title='自动化报告' + date)
            runny.run(suite)
            log.info('TestCase run end!!!\n')
        except Exception as e:
            log.info('TestCase run fail!!!')
            log.error(e, '\n')
            raise

    def thread_run_Beautifuhtml(self, suite, file_name):
        """多进程执行用例并输出漂亮报告"""
        try:
            lock.acquire()
            name = '\\' + file_name
            result = BeautifulReport(suite, verbosity=2)
            result.report(filename=name, description='测试deafult报告', log_path=self.reportFile1)
        except Exception as e:
            log.error(e)
            raise
        finally:
            lock.release()

