import os
import unittest
import time
from config.readCaselist import read_caseList
from config.getProjectPath import get_project_path
from common.log import Logger

path = get_project_path()
log = Logger('common.caseSuite').get_logger()


class caseSuite():
    """
    测试套件类
    """
    def __init__(self):
        self.caseList = read_caseList().get_case()     # 测试用例文件
        self.caseFile = os.path.join(path, 'Po', 'testcase')  # 测试用例目录

    def set_case_suite(self):
        """
        将指定用例加入到测试套件中
        :return:
        """
        t1 = time.time()
        case_suite = unittest.TestSuite()   # 创建一个测试套件
        suite_list = []
        for suite in self.caseList:
            # 创建测试集合
            suiteSet = unittest.defaultTestLoader.discover(self.caseFile, pattern=suite)
            suite_list.append(suiteSet)
        if len(suite_list) > 0:
            for suite in suite_list:
                # 加入指定的测试集合到测试套件
                case_suite.addTest(suite)
            log.info('Success get caseSuite, spend {0} seconds'.format(time.time() - t1))
        else:
            log.error('Fail case_suite is "air",Please add case to the caseFile, spend {0} seconds'.format(time.time() - t1))
            raise Exception('Case_suite is air,  Please add case to the caseFile.')
        return case_suite   # 返回测试套件

    def set_caseSet(self):
        """
        测试集合，使指定目录所有文件为用例
        :return:
        """
        t1 = time.time()
        suiteset = unittest.defaultTestLoader.discover(self.caseFile, pattern='*_test.py')
        log.info('Success get suiteSet, spend {0} seconds'.format(time.time() - t1))
        return suiteset


if __name__ == '__main__':

    suite = caseSuite().set_case_suite()
    num = 1
    print(type(suite))
    for i in suite:
        print('{0}:{1}'.format(num, i))
        num += 1
        print(type(i))



