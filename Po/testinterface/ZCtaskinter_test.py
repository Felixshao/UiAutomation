import unittest, re
import requests
import urllib3
import ddt
from bs4 import BeautifulSoup
from common.log import Logger
from common.operateExcel import operateExcel

log = Logger('Po.testinterface.ZCtaskinter_test').get_logger()
task = operateExcel(file_name='zc_interface.xlsx', sheet_name='task').get_excel_list()


@ddt.ddt
class ZCtaskinter_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        log.info('--------------------------------- ZCtaskinter_test start ---------------------------------------')
        urllib3.disable_warnings()


    @classmethod
    def tearDownClass(cls):
        log.info('--------------------------------- ZCtaskinter_test end ---------------------------------------')

    @ddt.data(*task)
    def test1_cantask_inter(self, data):
        """任务筛选接口"""
        try:
            task = requests.get(data[1], params=data[3], verify=False)
            assert_result = eval(data[4])
            self.assertEqual(task.status_code, assert_result['status_code'], msg='不相等，status_code:{0}'.format(task.status_code))
            soup = BeautifulSoup(task.text, 'lxml')
            name = soup.find_all('p', class_='h_logo_name')
            if len(name) > 0:
                results = []
                for i in range(len(name)):
                    name[i] = str(name[i]).replace('\n', '')
                    task_name = re.match(pattern='<p class="h_logo_name"><span>(.*)</span></p>',
                                         string=name[i])
                    results.append(task_name.group(1))
                log.info('用例成功，{0}结果为:{1}'.format(data[0], results))
                print('用例成功，{0}结果为:{1}'.format(data[0], results))
            else:
                log.info('用例成功，{0}结果为:{1}'.format(data[0], '暂无测试任务'))
                print('用例成功, {0}结果为:{1}'.format(data[0], '暂无测试任务'))
        except Exception as e:
            log.error('{0}接口报错:{1}.'.format(data[0], data[1]))
            log.error('test1_cantask_inter:{0}'.format(e))
            print('{0}接口报错.'.format(data[0]))
            raise

