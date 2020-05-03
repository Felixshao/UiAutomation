import configparser


class MyConfigParser(configparser.ConfigParser):
    """继承configparser类"""

    def optionxform(self, optionstr):
        """重写optionxform方法，改变读取ini文件大写变小写问题"""
        return optionstr