import os
import xlrd
import time
from config import getProjectPath
from common.log import Logger


path = getProjectPath.get_project_path()
mobile_path = os.path.join(path, 'config', 'mobile.xlsx')
log = Logger('config.getMobile').get_logger()


def get_mobile(sheetname='android'):
    """
    获取配置的手机和app信息，在mobile.xlsx文件修改和增加配置元件
    :return:datas; 返回所有设备信息，dict格式
    """
    t1 = time.time()
    try:
        table = xlrd.open_workbook(mobile_path).sheet_by_name(sheetname)
        row = table.nrows   # 行
        col = table.ncols   # 列
        datas = {}
        for i in range(1, row):
            mobile_data = {}
            for j in range(1, col):
                if table.cell_value(i, j) == 'True' or table.cell_value(i, j) == 'true':
                    mobile_data[table.cell_value(0, j)] = True
                elif table.cell_value(i, j) == 'False' or table.cell_value(i, j) == 'false':
                    mobile_data[table.cell_value(0, j)] = False
                elif (table.cell_value(0, j) == 'chromeOptions') and (not table.cell_value(i, j)):
                    continue
                else:
                    mobile_data[table.cell_value(0, j)] = table.cell_value(i, j)
            if 'chromeOptions' in mobile_data.keys():
                mobile_data['chromeOptions'] = eval(mobile_data['chromeOptions'])
            datas[int(table.cell_value(i, 0))] = mobile_data
        log.info('Success get mobile data, spend {0} seconds'.format(time.time() - t1))
    except Exception as e:
        log.info('Fail get mobile data, spend {0} seconds'.format(time.time() - t1))
        log.error(e)
        raise
    return datas


if __name__ == '__main__':
    print(get_mobile('uiauto2_android'))
    # app = {'a': 'b'}
    # print(dict)
    # get_mobile()
    # pass
