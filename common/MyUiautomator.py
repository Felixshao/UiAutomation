# _*_ config: utf-8 _*_
# python3的MyUiautomator

import time, subprocess, os
import uiautomator2 as u2
from common.MyChromedriver import ChromeDriver
from common.MySelenium import mySelenium
from config.getMobile import get_mobile

# 获取设备信息
mobile_data = get_mobile('uiauto2_android')[1]


class MyUiautomator2(mySelenium):

    def connect_android(self, ip=mobile_data['ip'], start='session', appPackage=mobile_data['appPackage'], secs=4):
        """
        连接设备和app
        :param ip: 设备ip，数据线连接传入None
        :param appPackage:包名
        :param secs:
        :return:
        """
        self.isconnect(ip)
        self.app = u2.connect(ip)  # 连接设备
        self.app.healthcheck()  # 解锁屏幕(但无法解开锁屏密码)并开启uiautomator2服务
        if start == 'session':
            self.app.session(appPackage)  # 连接app
        elif start == 'app_start':
            self.app.app_start(appPackage)
        self.app.toast.show('测试开始', 2)  # toast.show方法，手机显示toast提示
        time.sleep(secs)
        return self.app

    def uiauto2_stop(self, service='uiautomator'):
        """
        关闭服务
        :param service: 服务名称，默认关闭‘uiautomator’
        :return:
        """
        self.app.service(service).stop()  # 关闭服务，默认关闭'uiautomator', 允许其他测试框架使用uiautomator服务

    def isconnect(self, ip):
        """
        电脑连接手机ip并断言
        :param ip:传入需要连接的ip
        :return:
        """
        res = subprocess.Popen('adb connect ' + ip, stdout=subprocess.PIPE)
        print(res.stdout.read().decode('utf-8'))
        res.kill()
        time.sleep(2)
        cmd_text = os.popen('adb devices').read()   # 获取adb devices结果，数据为str

        def isconnect_child():
            ip_position = cmd_text.rfind(ip)  # rfind方法，从右开始匹配字符，找到返回字符在字符串中的位置，否则返回-1
            if ip_position != -1:
                if not cmd_text.endswitch('device', ip_position+20, ip_position+26):    # endswitch方法断言指定位置字符是否匹配
                    result = '"{}"连接状态不是device，状态为: {}, 请重新连接!'.\
                        format(ip, cmd_text[ip_position+20, ip_position+26])
                    raise result
            else:
                result = '未找到配置的ip: "{}", 请检查连接配置'.format(ip)
                raise result
        return isconnect_child

    def switch_chromedriver(self, app, device_ip=None, package=None, attach=True, activity=None, process=None, secs=2):
        """
        uiautomator2工具切换进入webview
        :param app: uiautomatro2的device
        :param ip:  设备ip(usb连接不用传ip)
        :return:
        """
        self.driver = ChromeDriver(self.app).driver(device_ip, package, attach, activity, process)
        time.sleep(secs)

    def get_app_info(self):
        """
        获取设备信息
        :return:app_info
        """
        app_info = self.app.info
        return app_info

    def get_app_current(self):
        """
        获取app包名和当前activity
        :return:
        """
        app_current = self.app.app_current()
        return app_current

    def connect_android1(self, secs=4):
        """连接设备"""
        self.isconnect(mobile_data['ip'])
        app = u2.connect(mobile_data['ip'])  # 连接设备
        app.healthcheck()   # 解锁屏幕(但无法解开锁屏密码)并开启uiautomator2服务
        app.session(mobile_data['appPackage'])   # 连接app
        app.toast.show('测试开始', 2)   # toast.show方法，手机显示toast提示
        time.sleep(secs)
        app.click(0.879, 0.955)  # 点击我的
        app(text='收藏').click()
        app(description='搜索').click()
        #
        app.set_fastinput_ime(True)  # 切换成FastInputIME输入法
        app.send_keys('准线网')  # adb广播输入，在光标处输入
        # app.clear_text()  # 清除输入框所有内容(Require android-uiautomator.apk version >= 1.0.7)
        app.set_fastinput_ime(False)  # 切换成正常的输入法

        app(resourceId='com.tencent.mm:id/bd').click()
        print(app.info)
        print(app.current_app())
        time.sleep(8)
        dr = mySelenium()
        dr.uiauto2_webview(app, device_ip=mobile_data['ip'])
        dr.get_page_source('homeAndmy.html')
        dr.click("xpath->//div[@class='xe-navigation bottom_nav']/div[4]")
        app.toast.show('测试结束', 3)
        app.service('uiautomator').stop()   # 关闭uiautomator服务，允许其他测试框架使用uiautomator服务

    def connect_app_webview(self):
        ips = ['192.168.31.199:5555']
        self.isconnect(ips)
        d = u2.connect('192.168.31.199:5555')
        print(type(d))
        # d.app_start('com.github.android_app_bootstrap')
        # d.session('com.github.android_app_bootstrap')
        # d(text='Login').click()
        # d(text='Baidu').click()
        # time.sleep(3)

        # print(d.info)
        # print(d.app_current())

    def test(self):
        pass


if __name__ == '__main__':
   uiau = MyUiautomator2()
   app = uiau.connect_android(start='app_start')

   uiau.uiauto2_webview(app)

   uiau.send('id->index-kw', 'python')
   uiau.click('id->index-bn')
   uiau.get_page_source('wxbaidu3.html')
   # print(app.get_app_info())
   uiau.quit()
   uiau.uiauto2_stop()