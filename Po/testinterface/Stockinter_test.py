import json
import time
import multiprocessing as mp
import unittest, ddt, requests, urllib3, re, datetime, os
from common.operateExcel import operateExcel
from common.log import Logger
from common import SMS
from config.getProjectPath import get_project_path

fill_name = 'stock_interface.xlsx'
sheet_name = 'stock'
stock = operateExcel(file_name=fill_name, sheet_name=sheet_name).get_excel_list()
log = Logger('testinterface.Stockinter_test').get_logger()
path = get_project_path()
file_path = os.path.join(path, 'file', 'stock.xlsx')


class Stockinter_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        log.info('------------------------ Stockinter_test 开始 -------------------------------------------------')
        urllib3.disable_warnings()

    @classmethod
    def tearDownClass(cls):
        log.info('------------------------ Stockinter_test 结束 -------------------------------------------------')

    def test1_Lushang_stock(self):
        """查看鲁商发展（600223）股票情况"""
        data = stock[0]
        try:
            data[3] = eval(data[3])
            data[4] = eval(data[4])
        except TypeError:
            pass
        self.collection_stock_prices('600223', data)

    def test2_chinaSatcom_stock(self):
        """查看中国卫通（601698）股票情况"""
        data = stock[1]
        try:
            data[3] = eval(data[3])
            data[4] = eval(data[4])
        except TypeError:
            pass
        self.collection_stock_prices('601698', data)

    def test3_xinlong_stock(self):
        """查看金健米业（600127）股票情况"""
        data = stock[2]
        try:
            data[3] = eval(data[3])
            data[4] = eval(data[4])
        except TypeError:
            pass
        self.collection_stock_prices('600127', data)

    def test4_chinabaoan_stock(self):
        """查看华北制药（600812）股票情况"""
        data = stock[3]
        try:
            data[3] = eval(data[3])
            data[4] = eval(data[4])
        except TypeError:
            pass
        self.collection_stock_prices('600812', data)

    def test5_twosixthree_stock(self):
        """查看农产品（000061）股票情况"""
        data = stock[4]
        try:
            data[3] = eval(data[3])
            data[4] = eval(data[4])
        except TypeError:
            pass
        return self.collection_stock_prices('000061', data)

    def test6_ningbo_stock(self):
        """查看宁波建工（601789）股票情况"""
        data = stock[4]
        try:
            data[3] = eval(data[3])
            data[4] = eval(data[4])
        except TypeError:
            pass
        return self.collection_stock_prices('601789', data)

    def test7_ningbo_stock(self):
        """查看深粮控股（000019）股票情况"""
        data = stock[4]
        try:
            data[3] = eval(data[3])
            data[4] = eval(data[4])
        except TypeError:
            pass
        return self.collection_stock_prices('000019', data)

    def collection_stock_prices(self, stock, data, filepath=file_path):
        """采集股票数据"""
        new_data = {}
        t = time.strftime("%Y-%m-%d", time.localtime())
        reques = requests.get(url=data[1], params=data[3], verify=False)
        text = eval(reques.text.replace('showStockData', ''))
        prices = {}
        prices['当前'] = text['data'][stock]['10']
        prices['最高'] = text['data'][stock]['8']
        prices['最低'] = text['data'][stock]['9']
        prices['今开'] = text['data'][stock]['7']
        prices['昨收'] = text['data'][stock]['6']
        prices['涨跌幅度'] = text['data'][stock]['199112'] + '%'
        self.check_hororlist_inter(text, prices, stock, data)
        # new_data[t] = prices
        # excel = operateExcel(filepath, stock)
        # old_data = excel.get_excel_dict()
        # if old_data:
        #     all_data = {**old_data, **new_data}
        # else:
        #     all_data = new_data
        # excel.input_excel(all_data)
        # print('采集成功，在{0}中查看'.format(filepath))

    def check_hororlist_inter(self, text, prices, stock, data):
        """断言接口"""
        now_time = datetime.datetime.now()
        if (now_time.hour >= 15) or (13 > now_time.hour >= 12):
            print('{}采集{}股票结束!'.format(now_time, stock))
        else:
            if float(text['data'][stock]['199112']) >= 5.0:
                body = 'stock:' + stock + ', up warning' + prices['涨跌幅度'] + ', price:' + prices['当前']
                SMS.send_msg(body)
                time.sleep(1800)
            elif float(text['data'][stock]['199112']) <= -5.0:
                body = 'stock:' + stock + ', fall warning:' + prices['涨跌幅度'] + ', price:' + prices['当前']
                SMS.send_msg(body)
                time.sleep(1800)
            else:
                time.sleep(300)
            self.collection_stock_prices(stock, data)

