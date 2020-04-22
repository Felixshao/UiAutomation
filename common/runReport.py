import os
import platform
import time
import threading
import multiprocessing as mp
from multiprocessing import Process
from common.HTMLTestRunner2 import HTMLTestRunner
from common.caseSuite import caseSuite
from config.getProjectPath import get_project_path
from common.log import Logger
from common.BeautifulReport import BeautifulReport
from config.readConfig import readConfig


path = get_project_path()
log = Logger('common.runReport').get_logger()
# lock = threading.Lock()
lock = mp.RLock()


class run_report():
    """
    运行测试套件，并生成报告
    """
    def __init__(self):
        self.caselist = readConfig().get_caselist()
        self.reportFile = os.path.join(path, 'report', 'report', 'report.html')     # 测试报告路径
        self.reportFile1 = os.path.join(path, 'report', 'report')  # 测试报告目录
        self.suite_all = caseSuite().set_case_suite()       # 获取测试套件
        self.report_result = []

    def run_html(self, report_name='report', suite=None, ):
        """单进程执行用例并输出报告"""
        try:
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
# --------------------------------------------- process ---------------------------------------------------------------

    def process_run_Beautifuhtml(self, suite=None, q=None, process=False):
        """执行用例并输出漂亮报告方法"""
        # global results
        try:
            lock.acquire()
            name = '\\report1'
            if not process:
                suite = self.suite_all
            result = BeautifulReport(suite, verbosity=2)
            results = result.report(filename=name, description='测试deafult报告', log_path=self.reportFile1, process=process)
            if process:
                q.put(results)
                # q.send(results)
                # q.close()
        except Exception as e:
            log.error(e)
            raise
        finally:
            lock.release()

    def moreProcess_report(self):
        """多进程执行用例并输出报告"""
        log.info('start moreProcess!')
        pros = []
        q = mp.Queue(maxsize=len(self.caselist))
        for i in self.suite_all:
            pro = Process(target=self.process_run_Beautifuhtml, args=(i, q, True))
            pros.append(pro)
        for pro in pros:
            pro.start()
        for pro in pros:
            self.report_result.append(q.get())
            # time.sleep(1)
            # print(self.report_result)
            # pro.join()
            # try:
            #     self.report_result.append(q.get_nowait())
            #     print(self.report_result)
            #     pro.join()
            # except _queue.Empty as queue:
            #     log.error('异常,_queue.Empty:"{0}"'.format(queue))
            #     pro.terminate()
            #     raise
        dict = {}
        log.info('start data processing!')
        for i in range(len(self.report_result)):
            if i == 0:
                dict['testName'] = self.report_result[0]['testName']
                dict['beginTime'] = self.report_result[0]['beginTime']
                dict['testPass'] = self.report_result[i]['testPass']
                dict['testResult'] = self.report_result[i]['testResult']
                dict['testAll'] = self.report_result[i]['testAll']
                dict['testFail'] = self.report_result[i]['testFail']
                dict['testSkip'] = self.report_result[i]['testSkip']
                dict['testError'] = self.report_result[i]['testError']
            else:
                dict['testPass'] += self.report_result[i]['testPass']
                dict['testResult'] += self.report_result[i]['testResult']
                dict['testAll'] += self.report_result[i]['testAll']
                dict['testFail'] += self.report_result[i]['testFail']
                dict['testSkip'] += self.report_result[i]['testSkip']
                dict['testError'] += self.report_result[i]['testError']
            dict['totalTime'] = self.report_result[i]['totalTime']
        log.info('MoreProcess end.start Transfer data and generate reports...')
        result = BeautifulReport(self.suite_all)
        result.stop_output(log_path=self.reportFile1 + '\\', FIELDS=dict)
        log.info('End of the project.Please see the report!')

# --------------------------------------------- process pool ---------------------------------------------

    def pool_run_Beautifuhtml(self, suite=None, q=None, process=False):
        """执行用例并输出漂亮报告方法"""
        try:
            name = '/report1' if platform.system() != 'Windows' else '\\report1'
            if not process:
                suite = self.suite_all
            result = BeautifulReport(suite, verbosity=2)
            results = result.report(filename=name, description='测试众测报告', log_path=self.reportFile1, process=process)
            if process:
                q.put(results)
        except Exception as e:
            log.error(e)
            raise

    def pool_report(self):
        """使用进程池执行用例并输出报告"""
        log.info('start pool!')
        q = mp.Manager().Queue()
        pool = mp.Pool()
        for i in self.suite_all:
            pool.apply_async(self.pool_run_Beautifuhtml, args=(i, q, True))
        pool.close()
        pool.join()
        for i in range(q.qsize()):
            self.report_result.append(q.get())
        dict = {}
        log.info('start data processing!')
        for i in range(len(self.report_result)):
            if i == 0:
                dict['testName'] = self.report_result[0]['testName']
                dict['beginTime'] = self.report_result[0]['beginTime']
                dict['testPass'] = self.report_result[i]['testPass']
                dict['testResult'] = self.report_result[i]['testResult']
                dict['testAll'] = self.report_result[i]['testAll']
                dict['testFail'] = self.report_result[i]['testFail']
                dict['testSkip'] = self.report_result[i]['testSkip']
                dict['testError'] = self.report_result[i]['testError']
            else:
                dict['testPass'] += self.report_result[i]['testPass']
                dict['testResult'] += self.report_result[i]['testResult']
                dict['testAll'] += self.report_result[i]['testAll']
                dict['testFail'] += self.report_result[i]['testFail']
                dict['testSkip'] += self.report_result[i]['testSkip']
                dict['testError'] += self.report_result[i]['testError']
            dict['totalTime'] = self.report_result[i]['totalTime']
        log.info('MoreProcess end.start Transfer data and generate reports...')
        result = BeautifulReport(self.suite_all)
        slash = '/' if platform.system() != 'Windows' else '//'   # 判断系统，给出不同路径连接符
        result.stop_output(log_path=self.reportFile1 + slash, FIELDS=dict)
        log.info('End of the project.Please see the report!')
        print('用例结束，在{0}查看报告!'.format(self.reportFile1))