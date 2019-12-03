import os
from common.MyConfiParser import  MyConfigParser
from config import getProjectPath

config = MyConfigParser()        # 引入configParser类读取配置文件
path = getProjectPath.get_project_path()
config_path = os.path.join(path, 'config', 'config.ini')    # 配置config.ini文件路径
config.read(config_path, encoding='utf-8')


class readConfig():
    """
    读取config.ini文件
    """
    def get_email(self):
        """
        获取配置文件中email信息
        :return:values_dict;信息存入dict并返回
        """
        values = config.items('Email')
        values_dict = {}
        for i in values:
            values_dict[i[0]] = i[1]
        return values_dict

    def get_phone(self):
        """
        获取手机配置信息
        :return:
        """
        values = config.items('Phone')
        values_dict = {}
        for i in values:
            values_dict[i[0]] = i[1]
            if i[1] == 'True' or i[1] == 'False':
                values_dict[i[0]] = bool(i[1])
        return values_dict

    def get_log(self):
        """
        获取log配置信息
        :return:
        """
        values = config.items('Log')
        values_dict = {}
        for i in values:
            values_dict[i[0]] = i[1]
        return values_dict


if __name__ == '__main__':

    dict = readConfig().get_phone()
    print(dict)

