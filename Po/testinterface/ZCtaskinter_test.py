import unittest
import requests
import urllib3
import ddt
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
            can_task = requests.get(data[1], params=data[3], verify=False)
            assert_result = eval(data[4])
            self.assertEqual(can_task.status_code, assert_result['status_code'], msg='不相等，status_code:{0}'.format(can_task.status_code))
            log.info('{0}接口用例成功!'.format(data[0]))
            print('{0}接口用例成功!'.format(data[0]))
        except Exception as e:
            log.error('{0}接口报错:{1}.'.format(data[0], data[1]))
            log.error('test1_cantask_inter:{0}'.format(e))
            print('{0}接口报错.'.format(data[0]))
            raise

