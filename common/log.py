import os
import logging
import time
from config import getProjectPath
from config.readConfig import  readConfig
from logging.handlers import TimedRotatingFileHandler

path = getProjectPath.get_project_path()
log = readConfig().get_log()


class Logger():
    """
    Logger类
    """
    def __init__(self, logger_name='log...'):
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)   # 设置日志总级别，不设置默认WARNING
        self.log_path = os.path.join(path, 'report', 'log', 'logs')     # 日志文件路径
        self.log_file_name = 'logs.txt'
        self.backup_Count = 5  # log文件数量

        # 设置日志级别，日志级别：CRITICAL > ERROR > WARNING > INFO > DEBUG
        self.file_output_lever = log['file_output_lever']
        self.console_output_lever = log['console_output_lever']

        # 设置日志格式
        self.Formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def get_logger(self):

        if not self.logger.handlers:
            console_handle = logging.StreamHandler()    # 创建控制台日志句柄
            console_handle.setFormatter(self.Formatter)     # 设置格式
            console_handle.setLevel(self.console_output_lever)      # 设置级别
            self.logger.addHandler(console_handle)      # 句柄加入logging对象
            file = self.log_path + time.strftime("%Y-%m-%d") + '.log'
            # 日志写入文件，每天创建一个新的日志文件，最多创建5个，后续文件新的覆盖旧的
            file_handle = TimedRotatingFileHandler(filename=file, when='D',
                                                   interval=1, backupCount=self.backup_Count,
                                                   delay=True, encoding='utf-8')
            file_handle.setFormatter(self.Formatter)
            file_handle.setLevel(self.file_output_lever)
            self.logger.addHandler(file_handle)
        return self.logger





