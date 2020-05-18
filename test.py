# _*_ config: utf-8 _*_
# 关键字驱动调试，test.py
import time
from selenium import webdriver

driver = ''


def open_browse():
    global driver
    driver = webdriver.Chrome()


def open_url(url):
    global driver
    driver.get(url)


def quit():
    global driver
    time.sleep(2)
    driver.quit()


if __name__ == '__main__':

    with open('./test.txt') as fp:
        datalist = fp.readlines()   # 读取关键字

    for data in datalist:
        action, value = data.split('||')    # 按行切割关键字
        if value and value != '\n':     # 判断参数是否为空
            command = '%s(\"%s\")' % (action.strip(), value.strip())    # 拼接操作语句
        else:
            command = '%s()' % (action.strip())
        exec(command)   # 运行操作语句
    print('git')
