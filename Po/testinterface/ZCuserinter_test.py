import unittest
import requests
import urllib3
import ddt
from common.operateExcel import operateExcel
from common.log import Logger

log = Logger('Po.testinterface.ZCuserinter_test').get_logger()
s = requests.Session()  # 定义一个全局session对象
login = operateExcel(file_name='zc_interface.xlsx', sheet_name='login').get_excel_list()[0]
user = operateExcel(file_name='zc_interface.xlsx', sheet_name='user').get_excel_list()


@ddt.ddt
class ZCuserinter_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        log.info('---------------------------- ZCuserinter_test start ---------------------------------------------')
        urllib3.disable_warnings()
        s.post(login[1], data=eval(login[3]), verify=False)

    @classmethod
    def tearDownClass(cls):
        log.info('---------------------------- ZCuserinter_test end ---------------------------------------------')

    @ddt.data(*user)
    def test1_user_income(self, data):
        """用户资料设置接口"""
        income = s.get(data[1], params=data[3], verify=False)
        print('{0}接口status_code:{1}'.format(data[0], income.status_code))
        print('{0}接口响应时间:{1}'.format(data[0], income.elapsed))
        # print('{0}响应内容:{1}'.format(data[0], income.text))
