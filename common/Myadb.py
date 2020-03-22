import subprocess
from common.log import Logger

log = Logger('common.Myadb.py').get_logger()


class Myadb():

    def call_adb(self, command: str):
        """
        发送adb命令
        :param command: 传入adb命令
        :return:
        """
        subprocess.call(command)
        log.info('start run adb command: {}'.format(command))