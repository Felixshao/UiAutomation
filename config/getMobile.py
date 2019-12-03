import os
import xlrd
import time
from config import getProjectPath
from common.log import Logger


path = getProjectPath.get_project_path()
mobile_path = os.path.join(path, 'config', 'mobile.xlsx')
log = Logger('config.mobile').get_logger()


def get_mobile():
    """
    获取配置的手机和app信息，在mobile.xlsx文件修改和增加配置元件
    :return:
    """
    t1 = time.time()
    try:
        table = xlrd.open_workbook(mobile_path).sheet_by_name('android')
        row = table.nrows   # 行
        col = table.ncols   # 列
        datas = {}
        for i in range(1, row):
            dict = {}
            for j in range(1, col):
                if table.cell_value(i, j) == 'True':
                    dict[table.cell_value(0, j)] = True
                elif table.cell_value(i, j) == 'False':
                    dict[table.cell_value(0, j)] = False
                else:
                    dict[table.cell_value(0, j)] = table.cell_value(i, j)
            datas[int(table.cell_value(i, 0))] = dict
        log.info('Success get mobile data, spend {0} seconds'.format(time.time() - t1))
    except Exception as e:
        log.info('Fail get mobile data, spend {0} seconds'.format(time.time() - t1))
        log.error(e)
        raise

    return datas

