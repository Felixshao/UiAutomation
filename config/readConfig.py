import os
from common.MyConfiParser import MyConfigParser
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

    def get_App(self):
        """
        获取app配置信息
        :return:
        """
        values = config.items('App')
        values_dict = {}
        for i in values:
            if i[0] == 'chromeOptions':
                values_dict[i[0]] = eval(i[1])
            else:
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

    def get_browser(self):
        """
        获取log配置信息
        :return:
        """
        values = config.items('Browser')
        values_dict = {}
        for i in values:
            values_dict[i[0]] = i[1]
        return values_dict

    def get_caselist(self):
        """
        获取测试用例信息
        :return:
        """
        values = config.items('Case_Path')
        values_list = []
        for i in values:
            values_list.append(i[1].split('/'))
        return values_list

    def get_sms(self):
        """
        获取sms配置信息
        :return:
        """
        values = config.items('SMS')
        values_dict = {}
        for i in values:
            values_dict[i[0]] = i[1]
        return values_dict

    def get_exe(self):
        """
        获取exe配置信息
        :return:
        """
        values = config.items('EXE')
        values_dict = {}
        for i in values:
            values_dict[i[0]] = i[1]
        return values_dict

    def get_unlock(self):
        """
        获取Unlock配置信息
        :return:
        """
        values = config.items('Unlock')
        values_dict = {}
        for i in values:
            values_dict[i[0]] = i[1]
        return values_dict


if __name__ == '__main__':

    exe = readConfig().get_unlock()
    print(exe['felix'], type(exe['felix']))
    a = exe['felix'].replace(' ', '').split(';')
    b = []
    for i in a:
        b.append(i.split(')'))
    print(a, type(a))
    print(b, type(b))
    # print(type(exe['chromeOptions']))

