import time, requests, openpyxl, os
import multiprocessing as mp
from common.operateExcel import operateExcel
from config.getProjectPath import get_project_path


path = get_project_path()
file = os.path.join(path, 'file', 'stock2.xlsx')
fill_name = 'stock_interface.xlsx'
sheet_name = 'stock'
stock = operateExcel(file_name=fill_name, sheet_name=sheet_name).get_excel_list()
prices = {}


def monitor_stock_inter(data, q):
    """"股票接口请求"""
    data[3] = eval(data[3])
    reques = requests.get(url=data[1], params=data[3], verify=False)
    result = eval(reques.text.replace('showStockData', ''))
    q.put(result)


def process():
    """
    多进程运行用例，并提取数据存入文件中
    :return:
    """
    pool = mp.Pool()
    q = mp.Manager().Queue()
    stock_result = []
    for i in range(len(stock)):
        pool.apply_async(monitor_stock_inter, args=(stock[i], q))
    pool.close()
    pool.join()
    for i in range(q.qsize()):
        stock_result.append(q.get())
    prices = {}
    num = 0
    for i in stock_result:
        stock_name = list(i['data'])[0]
        price = {}
        price['当前'] = i['data'][stock_name]['10']
        price['最高'] = i['data'][stock_name]['8']
        price['最低'] = i['data'][stock_name]['9']
        price['今开'] = i['data'][stock_name]['7']
        price['昨收'] = i['data'][stock_name]['6']
        price['涨跌幅度'] = i['data'][stock_name]['199112'] + '%'
        prices[stock_name] = price
        num += 1
    t = time.strftime("%Y-%m-%d", time.localtime())
    table = openpyxl.load_workbook(file)
    for i in prices.keys():
        if i not in table.sheetnames:
            shell = table.create_sheet(i)
            shell.cell(1, 1, i)
            shell.cell(2, 1, '时间')
            shell.cell(2, 2, '当前')
            shell.cell(2, 3, '最高')
            shell.cell(2, 4, '最低')
            shell.cell(2, 5, '今开')
            shell.cell(2, 6, '昨收')
            shell.cell(2, 7, '幅度')
        else:
            shell = table[i]
        row = shell.max_row     # max_row获取最大行数
        # col = table.max_column  # max_row获取最大列数
        shell.cell(row + 1, 1, t)
        col = 2
        for n in prices[i]:
            shell.cell(row+1, col, str(prices[i][n]))
            col += 1
    table.save(file)
    print('成功写入:{}'.format(file))


if __name__ == '__main__':
    process()

