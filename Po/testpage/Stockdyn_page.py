import time, os
from common.BeautifulReport import BeautifulReport
from common.basePage import Page
from common.log import Logger
from common.operateExcel import operateExcel
from config.getProjectPath import get_project_path

path = get_project_path()
log = Logger('testpage.Stockdyn_page').get_logger()
stock_dynamic_url = 'http://quote.eastmoney.com/'   # 股票动态查询网址
file_path = os.path.join(path, 'file', 'stock.xlsx')
"""------------------------------------------- element --------------------------------------------------------"""
stock_search_bar = 'id->search_box'     # 股票搜索按钮
stock_search_butten = 'xpath->//input[@id="search_box"]/../input[2]'     # 股票搜索按钮
stock_search_result = 'xpath->//div[@class="module module-share"]/div[1]/a[1]'  # 股票搜索结果第一条
stock_new_prices = 'id->price9'  # 股票当前价格
# stock_opentoday_money = 'xpath->//table[@class="yfw"]/tbody/tr[1]/td[2]'  # 股票今开价格
# stock_highest_money = 'xpath->//table[@class="yfw"]/tbody/tr[1]/td[4]'  # 股票最高价格
# stock_closeyes_money = 'xpath->//table[@class="yfw"]/tbody/tr[2]/td[2]'  # 股票昨收价格
# stock_lowest_money = 'xpath->//table[@class="yfw"]/tbody/tr[2]/td[4]'  # 股票最低价格
stock_opentoday_prices = 'id->gt1'  # 股票今开价格
stock_highest_prices = 'id->gt2'  # 股票最高价格
stock_closeyes_prices = 'id->gt8'  # 股票昨收价格
stock_lowest_prices = 'id->gt9'  # 股票最低价格


class Stockdyn_page(Page):

    def open_stock_dynamic(self):
        """打开股票动态页面"""
        self.dr.open_url(stock_dynamic_url)

    def send_stock_search(self, stock_name):
        """输入股票代码"""
        self.dr.send(stock_search_bar, stock_name)
        self.dr.switch_new_window(stock_search_butten)
        self.dr.switch_new_window(stock_search_result)
        self.collection_stock_prices(stock_name=stock_name, filepath=file_path)

    def collection_stock_prices(self, stock_name, filepath):
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

