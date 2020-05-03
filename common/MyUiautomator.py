# _*_ config: utf-8 _*_
# python3的MyUiautomator

import time, subprocess, os
import uiautomator2 as u2
from common.MyChromedriver import ChromeDriver


def isconnect(ips: list):
    """
    电脑连接手机ip并断言
    :param ips:传入需要连接的ip，类型为list
    :return:
    """
    for ip in ips:
        res = subprocess.Popen('adb connect ' + ip, stdout=subprocess.PIPE)
        print(res.stdout.read().decode('utf-8'))
        res.kill()
    time.sleep(2)
    cmd_text = os.popen('adb devices').read()   # 获取adb devices结果，数据为str

    def isconnect_child():
        results = []
        for num in range(len(ips)):
            ip_position = cmd_text.rfind(ips[num])  # rfind方法，从右开始匹配字符，找到返回字符在字符串中的位置，否则返回-1
            if ip_position != -1:
                if not cmd_text.endswitch('device', ip_position+20, ip_position+26):    # endswitch方法断言指定位置字符是否匹配
                    result = '"{}"连接状态不是device，状态为: {}, 请重新连接!'.\
                        format(ips[num], cmd_text[ip_position+20, ip_position+26])
                    results.append(result)
            else:
                result = '未找到配置的ip: "{}", 请检查连接配置'.format(ips[num])
                results.append(result)
        if len(results) > 0:    # 存在连接不正确的ip抛出异常
            raise results
    return isconnect_child


def connect_android():
    """连接设备"""
    ips = ['192.168.31.199:5555']
    isconnect(ips)

    app = u2.connect('192.168.31.199:5555')  # 连接设备
    app.session('com.tencent.mm')   # 连接app
    # app.app_start('com.tencent.mm')
    #
    time.sleep(4)
    app.click(0.879, 0.955)  # 点击我的
    # app(xpath='com.tencent.mm:id/tb').click()
    app(text='收藏').click()
    app(description='搜索').click()

    app.set_fastinput_ime(True)  # 切换成FastInputIME输入法
    app.send_keys('准线网')  # adb广播输入，在光标处输入
    # app.clear_text()  # 清除输入框所有内容(Require android-uiautomator.apk version >= 1.0.7)
    app.set_fastinput_ime(False)  # 切换成正常的输入法

    app(resourceId='com.tencent.mm:id/bd').click()
    print(app.info)
    print(app.current_app())
    time.sleep(8)
    dr = ChromeDriver(app).driver(device_ip='192.168.31.199:5555')
    dr.find_element_by_xpath("//div[@class='xe-navigation bottom_nav']/div[2]").click()
    print(dr.page_source())


if __name__ == '__main__':

    connect_android()