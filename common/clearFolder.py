import os
import shutil
from config.getProjectPath import get_project_path
from common.log import Logger

path = get_project_path()
log = Logger('common.clearFolder').get_logger()


class clearFolder():

    def __init__(self):

        self.screen_shot_path = os.path.join(path, 'report', 'screen_shot')
        self.log_path = os.path.join(path, 'report', 'log')
        self.report_path = os.path.join(path, 'report', 'report')

    def clear_screenshot(self):
        """清空截图文件夹内容"""
        try:
            for i in os.listdir(self.screen_shot_path):     # 循环取出文件内容
                file = os.path.join(self.screen_shot_path, i)
                if os.path.isfile(file):    # 判断是否为文件
                    os.remove(file)     # 移除文件
                else:
                    for f in os.listdir(file):
                        file2 = os.path.join(file, f)
                        if os.path.isfile(file2):
                            os.remove(file2)
            log.info('Success clear folder;"{0}" content'.format(self.screen_shot_path))
        except FileNotFoundError as file:
            os.mkdir(self.screen_shot_path)
            log.info('Success mkdir folder;"{0}"'.format(self.screen_shot_path))
            log.info(file)

    def clear_report(self):
        """清空报告内容"""
        try:
            for i in os.listdir(self.report_path):     # 循环取出文件内容
                file = os.path.join(self.report_path, i)
                if os.path.isfile(file):    # 判断是否为文件
                    os.remove(file)     # 移除文件
            log.info('Success clear folder;"{0}" content'.format(self.report_path))
        except FileNotFoundError as file:
            os.mkdir(self.report_path)
            log.info('Success mkdir folder;"{0}"'.format(self.report_path))
            log.info(file)
    """----------------------------------------------------------------------------------------------------------"""
    def rmove_folder(self):
        """通过删除文件夹方式实现清空文件夹内容"""
        try:
            shutil.rmtree(self.screen_shot_path)    # 删除文件夹
            # os.removedirs(self.screen_shot_path)
            os.mkdir(self.screen_shot_path)     # 创建文件夹
            log.info('Success rmove and mkdir folder:"{0}" content'.format(self.screen_shot_path))
        except FileNotFoundError as file:
            os.mkdir(self.screen_shot_path)
            log.info('Success mkdir folder;"{0}"'.format(self.screen_shot_path))
            log.info(file)


if __name__ == '__main__':

    cle = clearFolder()
    cle.clear_report()
