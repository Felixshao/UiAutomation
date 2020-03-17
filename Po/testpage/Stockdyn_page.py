import datetime
import time, os
from common.BeautifulReport import BeautifulReport
from common.basePage import Page
from common.log import Logger
from common.operateExcel import operateExcel
from config.getProjectPath import get_project_path
from common import SMS

path = get_project_path()
log = Logger('testpage.Stockdyn_page').get_logger()
stock_url = 'http://quote.eastmoney.com/'
file_path = os.path.join(path, 'file', 'stock.xlsx')
"""------------------------------------------- element --------------------------------------------------------"""
stock_search_bar = 'id->search_box'     # 股票搜索按钮
stock_search_butten = 'xpath->//input[@id="search_box"]/../input[2]'     # 股票搜索按钮
stock_search_result = 'xpath->//div[@class="module module-share"]/div[1]/a[1]'  # 股票搜索结果第一条
stock_new_prices = 'id->price9'  # 股票当前价格
stock_opentoday_prices = 'id->gt1'  # 股票今开价格
stock_highest_prices = 'id->gt2'  # 股票最高价格
stock_closeyes_prices = 'id->gt8'  # 股票昨收价格
stock_lowest_prices = 'id->gt9'  # 股票最低价格
stock_increase = 'id->km2'  # 股票涨低百分比


class Stockdyn_page(Page):

    def open_stock_dynamic(self, stock_name):
        """打开股票动态页面"""
        self.dr.open_url(stock_url + stock_name + '.html??from=BaiduAladdin')
        self.collection_stock_prices(stock_name=stock_name)

    def collection_stock_prices(self, stock_name, filepath=file_path):
        """
        收集股票信息
        :param stock_name:股票代码
        :param filepath:excel文件路径
        :return:
        """
        new_data = {}
        prices = {}
        t = time.strftime("%Y-%m-%d", time.localtime())
        prices['当前'] = self.dr.get_ele_content(stock_new_prices)
        prices['今开'] = self.dr.get_ele_content(stock_opentoday_prices)
        prices['最高'] = self.dr.get_ele_content(stock_highest_prices)
        prices['昨收'] = self.dr.get_ele_content(stock_closeyes_prices)
        prices['最低'] = self.dr.get_ele_content(stock_lowest_prices)
        prices['涨跌幅度'] = self.dr.get_ele_content(stock_increase)
        self.stock_police(stock_name, prices)
        new_data[t] = prices
        excel = operateExcel(filepath, stock_name)
        old_data = excel.get_excel_dict()
        if old_data:
            all_data = {**old_data, **new_data}
        else:
            all_data = new_data
        excel.input_excel(all_data)
        print('采集成功，在{0}中查看'.format(filepath))
        self.dr.get_page_screenshot(case_name=stock_name + '股票_详情')
        BeautifulReport.add_test_img3(stock_name + '股票_详情')

    def stock_police(self, stock_name: str, prices):
        """股票报警"""
        increase = float(prices['涨跌幅度'].replace('%', ''))
        if increase >= 5.0:
            body = 'stock:' + stock_name + 'up warning' + prices['涨跌幅度'] + ', price:' + prices['当前']
            SMS.send_msg(body)
        elif increase <= -5.0:
            body = 'stock:' + stock_name + 'fall warning:' + prices['涨跌幅度'] + ', price:' + prices['当前']
            SMS.send_msg(body)
        else:
            now_time = datetime.datetime.now()
            if now_time.hour >= 15:
                print('{}采集{}股票结束!'.format(now_time, stock_name))
            elif (now_time.hour >= 12) and (now_time.hour <= 13):
                print('{}采集{}股票结束!'.format(now_time, stock_name))
            else:
                time.sleep(300)
                self.collection_stock_prices(stock_name)
