import unittest, re
import requests
import urllib3
import ddt
from bs4 import BeautifulSoup
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

    @ddt.data(user[0])
    def test1_user_income(self, data):
        """用户基本资料接口"""
        try:
            basic = s.get(data[1], params=data[3], verify=False)
            assert_result = eval(data[4])
            self.assertEqual(basic.status_code, assert_result['status_code'],
                             msg='不相等，status_code:{0}'.format(basic.status_code))
            soup = BeautifulSoup(basic.text, 'lxml')
            dict = {}
            dict['账号'] = soup.find('p', class_='bas-per-account').get_text()  # 账号
            dict['身份证认证状态'] = soup.find('span', class_='upfail').get_text()    # 身份证认证状态
            dict['账户余额'] = soup.find('span', style='color: #f99c00;').get_text()     # 账户余额
            dict['昵称'] = soup.find('input', id="nickname")['value']    # 昵称
            dict['qq'] = soup.find('input', id='qq')['value']     # qq
            select = soup.find_all('option', selected='selected')   # 性别
            for i in range(len(select)):
                if i == 0:
                    dict['性别'] = select[i].get_text().replace('\n', '').replace(' ', '')
                elif i == 1:
                    dict['生日'] = select[i].get_text().replace('\n', '').replace(' ', '')
                elif i == 2:
                    dict['地址'] = select[i].get_text().replace('\n', '').replace(' ', '')
                elif i == 3:
                    dict['职业'] = select[i].get_text().replace('\n', '').replace(' ', '')
                elif i == 4:
                    dict['测试经验'] = select[i].get_text().replace('\n', '').replace(' ', '')
                elif i == 5:
                    dict['管理经验'] = select[i].get_text().replace('\n', '').replace(' ', '')
            print('用例成功，用户{0}为:{1}'.format(data[0], dict))
            log.info('用例成功，用户{0}为:{1}'.format(data[0], dict))
        except Exception as e:
            print('{0}接口失败!'.format(data[0]))
            log.error('{0}接口失败!'.format(data[0]))
            login.error(e)
            raise

    @ddt.data(user[1])
    def test2_user_income(self, data):
        """用户测试设备接口"""
        try:
            basic = s.get(data[1], params=data[3], verify=False)
            assert_result = eval(data[4])
            self.assertEqual(basic.status_code, assert_result['status_code'],
                             msg='不相等，status_code:{0}'.format(basic.status_code))
            soup = BeautifulSoup(basic.text, 'lxml')
            dicts = {}
            num = soup.find_all('span', class_='fr delete-equts')   # 查看设备个数
            cont = soup.find_all('span', class_='equip-cont')  # 账号
            it = 0
            for i in range(len(num)):
                dict = {}
                dict['品牌型号'] = cont[it].get_text()
                dict['操作系统'] = cont[it+1].get_text()
                dict['运营商网络'] = cont[it+2].get_text()
                dicts['设备' + str(i+1)] = dict
                it += 3
            print('用例成功，用户{0}为:{1}'.format(data[0], dicts))
            log.info('用例成功，用户{0}为:{1}'.format(data[0], dicts))
        except Exception as e:
            print('{0}接口失败!'.format(data[0]))
            log.error('{0}接口失败!'.format(data[0]))
            login.error(e)
            raise