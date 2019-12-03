import os
import time
from config.getProjectPath import get_project_path
from common.log import Logger

path = get_project_path()
case_path = os.path.join(path, 'config', 'caselist.txt')
log = Logger('config.readCaselist').get_logger()


class read_caseList():

    def get_case(self):
        """
        读取txt，获取用例文件存入list
        :return:case_list
        """
        t1 = time.time()
        case_list = []
        try:
            txt = open(case_path, encoding='utf-8')
            for i in txt.readlines():
                if '#' in i or i == '\n':
                    continue
                case_list.append(i.replace('\n', '').split('/')[1])
            log.info('Success read the caseFile and save it to the list, spend {0} seconds'.format(time.time() - t1))
        except Exception as e:
            log.info('Fail read the caseFile. spend {0} seconds'.format(time.time() - t1))
            log.error(e)
            raise
        return case_list



