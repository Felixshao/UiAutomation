# _*_ config: utf-8 _*_
# python3的MyUiautomator

import time, subprocess, os
import uiautomator2 as u2
from config.getMobile import get_mobile
from config.readConfig import readConfig
from common.log import Logger

# 获取设备信息
mobile_data = get_mobile('uiauto2_android')[1]
unlock_data = readConfig().get_unlock()
log = Logger().get_logger()


class MyUiautomator2(object):

    def connect_android(self, ip=mobile_data['ip']):
        """
        连接设备
        :param ip: 设备ip，数据线连接传入None
        """
        self.isconnect(ip)
        self.app = u2.connect(ip)  # 连接设备
        self.app.unlock()
        # self.app.healthcheck()  # 解锁屏幕(但无法解开锁屏密码)并开启uiautomator2服务

    def connect_app(self, start='session', appPackage=mobile_data['appPackage'], secs=4):
        """
        连接app
        :param ip: 设备ip，数据线连接传入None
        :param appPackage:包名
        :param secs:
        :return:
        """
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
        self.app.toast.show('测试结束', 2)
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

    def find_ele(self, css):
        """
        uiautomator2点击元素
        :param css:元素类型和元素定位,如: text->收藏
        :return:
        """
        if '->' not in css:
            log.error('Positioning syntax errors. element:"{0}" lack of "->"'.format(css))
            raise NameError('Positioning syntax errors. lack of "->"')
        by = css.split('->')[0]
        ele = css.split('->')[1]
        if by == 'text':
            app_ele = self.app(text=ele)
        elif by == 'description':
            app_ele = self.app(description=ele)
        elif by == 'id':
            app_ele = self.app(resourceId=ele)
        elif by == 'className':
            app_ele = self.app(className=ele)
        else:
            log.error('无此类型: {}，请输入一下类型: text、 description、 resourceId、 className'.format(by))
            raise NameError('无此类型: {}，请输入一下类型: text、 description、 resourceId、 className'.format(by))
        return app_ele

    def find_ele_all(self, css):
        """
        uiautomator2点击元素
        :param css:元素类型和元素定位,如: text->收藏
        :return:
        """
        if '->' not in css:
            log.error('Positioning syntax errors. element:"{0}" lack of "->"'.format(css))
            raise NameError('Positioning syntax errors. lack of "->"')
        by = css.split('->')[0]
        ele = css.split('->')[1]
        if by == 'text':
            app_eles = self.app(text=ele).all()
        elif by == 'description':
            app_eles = self.app(description=ele).all()
        elif by == 'id':
            app_eles = self.app(resourceId=ele).all()
        elif by == 'className':
            app_eles = self.app(className=ele).all()
        elif by == 'xpath':
            app_eles = self.app.xpath(ele).all()
        else:
            log.error('无此类型: {}，请输入一下类型: text、 description、 resourceId、 className'.format(by))
            raise NameError('无此类型: {}，请输入一下类型: text、 description、 resourceId、 className'.format(by))
        return app_eles

    def click(self, css):
        """
        uiautomator2点击事件
        :param css:传入定位元素或坐标,元素如:text->收藏; 坐标如:[1, 2]/(1, 2)
        :return:
        """
        if type(css) is str:
            self.find_ele(css).click()
            log.info('sucess click ele: {}'.format(css))
        elif type(css) is list or type(css) is tuple:
            self.app.click(css[0], css[1])
            log.info('sucess click coordinate: {}'.format(css))
        else:
            log.error('click Positioning syntax errors: {}, 请传入以下类型: str、 list、 tuble'.format(css))
            raise NameError('click Positioning syntax errors: {}, 请传入以下类型: str、 list、 tuble'.format(css))

    def double_click(self, css, secs=0.1):
        """
        uiautomator2两次点击事件
        :param css:传入定位元素或坐标,元素如:text->收藏; 坐标如:[1, 2]/(1, 2)
        :param secs:两次点击间隔时间
        :return:
        """
        if type(css) is str:
            self.find_ele(css).double_click(duration=secs)
            log.info('sucess double_click ele: {}'.format(css))
        elif type(css) is list or type(css) is tuple:
            self.app.double_click(css[0], css[1], duration=secs)
            log.info('sucess double_click coordinate: {}'.format(css))
        else:
            log.error('double_click Positioning syntax errors: {}, 请传入以下类型: str、 list、 tuble'.format(css))
            raise NameError('double_click Positioning syntax errors: {}, 请传入以下类型: str、 list、 tuble'.format(css))

    def long_click(self, css, secs=0.5):
        """
        uiautomator2长按点击事件
        :param css:传入定位元素或坐标,元素如:text->收藏; 坐标如:[1, 2]/(1, 2)
        :param secs;长按时间
        :return:
        """
        if type(css) is str:
            self.find_ele(css).long_click(duration=secs)
            log.info('sucess long_click ele: {}'.format(css))
        elif type(css) is list or type(css) is tuple:
            self.app.long_click(css[0], css[1], duration=secs)
            log.info('sucess long_click coordinate: {}'.format(css))
        else:
            log.error('long_click Positioning syntax errors: {}, 请传入以下类型: str、 list、 tuble'.format(css))
            raise NameError('long_click Positioning syntax errors: {}, 请传入以下类型: str、 list、 tuble'.format(css))

    def set_text(self, css, text):
        """输入值，不调用输入法输入"""
        app_element = self.find_ele(css)
        app_element.set_text(text)
        log.info('sucess set text: "{}" / "{}"'.format(css, text))

    def send_keys(self, text):
        """
        无法定位时，使用输入法输入，在光标处输入
        :param text: 文本
        :return:
        """
        self.app.set_fastinput_ime(True)  # 切换成FastInputIME输入法
        self.app.send_keys(text)  # adb广播输入，在光标处输入
        # app.clear_text()  # 清除输入框所有内容(Require android-uiautomator.apk version >= 1.0.7)
        self.app.set_fastinput_ime(False)  # 切换成正常的输入法
        log.info('sucess send keys: "{}"'.format(text))

    def swipe_up(self, num=1):
        """向上滑动"""
        size = self.app.window_size()
        for i in range(num):
            x = size[0] * 0.5
            y1 = size[1] * 0.8
            y2 = size[1] * 0.2

            self.app.swipe(x, y1, x, y2)

    def swipe_down(self, num=1):
        """向上滑动"""
        size = self.app.window_size()
        for i in range(num):
            x = size[0] * 0.5
            y1 = size[1] * 0.8
            y2 = size[1] * 0.2

            self.app.swipe(x, y1, x, y2)
        self.uiauto2_stop()

    def swipe_points(self, points=unlock_data['felix'], secs=0.2):
        """"拖动"""
        print(unlock_data['felix'], type(unlock_data['felix']))
        points = list(points)
        print(points)
        self.app.swipe_points(points, secs)

    def touch_down(self, x1, y1):
        """模拟按下"""
        self.app.touch.down(x1, y1)

    def touch_up(self):
        """模拟抬起"""
        self.app.touch.up()

    def ele_center(self, ele):
        """获取元素中心坐标"""
        ele_coor = []
        if type(ele) is str:
            ele_coor.append(ele.center())
        elif type(ele) is list:
            for i in ele:
                ele_coor.append(i.center())
        else:
            raise NameError('类型错误，请输入定位元素或元素list')

        return ele_coor


if __name__ == '__main__':
    uiau = MyUiautomator2()
    uiau.connect_android()
    ele_list = uiau.find_ele_all('xpath->//android.view.View')
    ele_coor = uiau.ele_center(ele_list)
    print(ele_coor)
    print(unlock_data['felix'])
    uiau.swipe_points()
    # uiau.drag(0.24, 0.477, 0.231, 0.773)
    # uiau.drag(0.231, 0.773, 0.759, 0.775)
    time.sleep(2)
    # uiau.swipe_down(5)