import os, platform
import time
from pyvirtualdisplay import Display
from selenium.common.exceptions import InvalidElementStateException, WebDriverException
from urllib3.exceptions import MaxRetryError
from config.getMobile import get_mobile
from common.log import Logger
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy as By
from selenium.webdriver.common.action_chains import ActionChains
from config.getProjectPath import get_project_path
from config.readConfig import readConfig
from common.BeautifulReport import BeautifulReport
# from pywinauto.application import Application

path = get_project_path()
phone_data = get_mobile()[2]    # 选择设备和app
# phone_data = readConfig().get_App()
browser_data = readConfig().get_browser()
log = Logger('common.mySelenium').get_logger()
screenshot_path = os.path.join(path, 'report', 'screen_shot')
success = 'Success'
fail = 'Fail'
install_unicode = 'id->com.android.packageinstaller:id/btn_install_confirm'
img_path = os.path.join(path, 'report', 'screen_shot')


class mySelenium():

    def __init__(self):
        pass

    # def open_pc_exe(self, file_path, title=None, class_name=None,backend='win32'):
    #     """
    #     打开pc中exe应用
    #     :param file_path:   # 应用路径
    #     :param title:   # 窗口标题
    #     :param backend:     # 窗口backend类型
    #     :return:
    #     """
    #     try:
    #         self.driver = Application(backend=backend)
    #         self.driver.connect(title_re=title, class_name=class_name)
    #     except BaseException :
    #         self.driver.start(file_path)
    #     log.info('Success open:"{}"'.format(file_path))

    def browser(self, browser=browser_data['chrome']):
        """
        配置浏览器
        :param browser:
        """
        if platform.system() != 'Windows':
            display = Display(visible=0, size=(900, 800))
            display.start()
        log.info('Start a new browser: {0}'.format(browser))
        if browser == 'chrome' or browser == 'CHROME':
            desired_capabilities = DesiredCapabilities.CHROME   # 页面加载策略，设置为none，不等待页面加载完成
            desired_capabilities['pageLoadStrategy'] = 'none'
            self.driver = webdriver.Chrome()
        elif browser == 'firefox' or browser == 'FIREFOX':
            desired_capabilities = DesiredCapabilities.FIREFOX
            desired_capabilities['pageLoadStrategy'] = 'none'
            self.driver = webdriver.Firefox()
        elif browser == 'ie' or browser == 'IE':
            desired_capabilities = DesiredCapabilities.INTERNETEXPLORER
            desired_capabilities['pageLoadStrategy'] = 'none'
            self.driver = webdriver.Ie()
        else:
            log.error("Not found '{0}' browser.you can enter 'chrome' 'firefox' or 'ie'".format(browser))
            raise NameError("Not found '{0}' browser.you can enter 'chrome' 'firefox' or 'ie'".format(browser))
        log.info('{0} Open "{1}" browser.'.format(success, browser))
        # return self.driver

    def mobile(self, data=phone_data, secs=3):
        """
        配置app
        :return:
        """
        t1 = time.time()
        time.sleep(secs)
        from appium import webdriver
        try:
            self.driver = webdriver.Remote(data['appium_url'], data)
            log.info('{0} Open "{1}" app, spend {2} seconds'.format(success, data['Appname'], time.time() - t1))
        except MaxRetryError as max:
            print('msg: 远程服务器未打开')
            log.error('{0} to open "{1}" app, msg: 远程服务器未打开'.format(fail, data['Appname']))
            log.error(max)
            raise
        except WebDriverException as web:
            log.error('{0} to open "{1}" app, msg: 无法连接设备或无法安装Unicode'.format(fail, data['Appname']))
            log.error(web)
            return web

    def caller_starup(self, source='browser', num=3):
        """
        回调函数,回调启动app/浏览器方法
        source:browser(浏览器) or mobile(app) (打开设备类型,默认为browser)
        num:循环测试
        """
        for i in range(num):
            if source == 'mobile':
                error = self.mobile(data=phone_data)
                if error == '' or error is None:
                    break
                elif i == num-1:
                    print('msg: 无法连接设备或无法安装Unicode')
                    raise WebDriverException(error)
            elif source == 'browser':
                self.browser(browser=browser_data['chrome'])
                break

    # @BeautifulReport.add_test_img2('打开url失败')
    def open_url(self, url):
        t1 = time.time()
        try:
            self.driver.get(url)
            log.info('{0} Open url: {1}, spend {2} seconds'.format(success, url, time.time() - t1))
        except Exception as e:
            log.info('Open link {0}: {1}, spend {2} seconds'.format(fail, url, time.time() - t1))
            log.error(e)
            self.get_page_screenshot(file_path=screenshot_path, case_name=url + '_打开url失败')
            BeautifulReport.add_test_img3(url + '_打开url失败')
            raise

    def max_window(self, source='web'):
        """
        最大化窗口
        :return:
        """
        t1 = time.time()
        try:
            self.driver.maximize_window()
            log.info('{0} Maximize window, spend {1} seconds'.format(success, time.time() - t1))
        except Exception as e:
            log.info('{0} Maximize window, spend {1} seconds'.format(fail, time.time() - t1))
            log.error(e)
            url = self.get_page_url()
            self.get_page_screenshot(case_name=url + '_最大化窗口失败', source=source)
            BeautifulReport.add_test_img3(url + '_最大化窗口失败')
            raise

    def find_element(self, css, secs=8, source='web'):
        """
        封装查找元素方法，加入WebDriverWait,判断元素是否在dom树中
        :param css:传入css， 格式:元素类型->定位元素(id->nvn)
        :param secs:
        :return:
        """
        t1 = time.time()
        if '->' not in css:
            log.error('Positioning syntax errors. element:"{0}" lack of "->"'.format(css))
            raise NameError('Positioning syntax errors. lack of "->"')
        by = css.split('->')[0]
        if by == 'uiautomator':
            element = 'new UiSelector().text(\"' + css.split('->')[1] + '\")'
        else:
            element = css.split('->')[1]
        message = 'Element: "{0}" not fount in {1} seconds'.format(element, secs)
        try:
            if by == 'id':
                webElement = \
                    WebDriverWait(self.driver, secs).until(EC.visibility_of_element_located((By.ID, element)), message=message)
            elif by == 'class':
                webElement = \
                    WebDriverWait(self.driver, secs).until(EC.visibility_of_element_located((By.CLASS_NAME, element)), message=message)
            elif by == 'name':
                webElement = \
                    WebDriverWait(self.driver, secs).until(EC.visibility_of_element_located((By.NAME, element)), message=message)
            elif by == 'xpath':
                webElement = \
                    WebDriverWait(self.driver, secs).until(EC.visibility_of_element_located((By.XPATH, element)), message=message)
            elif by == 'text':
                webElement = \
                    WebDriverWait(self.driver, secs).until(EC.visibility_of_element_located((By.LINK_TEXT, element)), message=message)
            elif by == 'css':
                webElement = WebDriverWait(self.driver, secs).until(EC.visibility_of_element_located
                                                                    ((By.CSS_SELECTOR, element)), message=message)
            elif by == 'uiautomator':
                webElement = WebDriverWait(self.driver, secs).until(EC.visibility_of_element_located
                                                                    ((By.ANDROID_UIAUTOMATOR, element)), message=message)
            elif by == 'accessibility id':
                webElement = WebDriverWait(self.driver, secs).until(EC.visibility_of_element_located
                                                                    ((By.ACCESSIBILITY_ID, element)), message=message)
            else:
                log.error('{0} Targeting elements error:"{1}", spend {2} seconds'.format(fail, css, time.time() - t1))
                # self.get_page_screenshot(case_name=element + '_元素错误', source=source)
                # BeautifulReport.add_test_img3(element + '_元素错误')
                raise NameError('Please enter the correct targeting elements,"id"、"class"、"name"、"xpath"、'
                                '"text"、"uiautomator"、"accessibility id"')
            log.info('{0} Find element "{1}" through "{2}", spend {3} seconds'.format(success, element, by, time.time() - t1))
        except Exception as e:
            log.info('{0} Unable to find element "{1}" through "{2}", spend {3} seconds'.format(fail, element, by, time.time() - t1))
            log.error(e)
            # self.get_page_screenshot(case_name=element + '_元素错误', source=source)
            # BeautifulReport.add_test_img3(element + '_元素错误')
            raise
        return webElement

    def finds_element(self, css, secs=8, source='web'):
        """
        查找元素集，加入WebDriverWait
        :param css:
        :param secs:
        :return:
        """
        t1 = time.time()
        if '->' not in css:
            log.error('Positioning syntax errors. element:"{0}" lack of "->"'.format(css))
            raise NameError('Positioning syntax errors. lack of "->"')
        by = css.split('->')[0]
        if by == 'uiautomator':
            element = 'new UiSelector().text(\"' + css.split('->')[1] + '\")'
        else:
            element = css.split('->')[1]
        message = 'Element: "{0}" not fount in {1} seconds'.format(element, secs)
        try:
            if by == 'id':
                webElements = \
                    WebDriverWait(self.driver, secs).until(EC.presence_of_all_elements_located((By.ID, element)), message=message)
            elif by == 'class':
                webElements = \
                    WebDriverWait(self.driver, secs).until(EC.presence_of_all_elements_located((By.CLASS_NAME, element)), message=message)
            elif by == 'name':
                webElements = \
                    WebDriverWait(self.driver, secs).until(EC.presence_of_all_elements_located((By.NAME, element)), message=message)
            elif by == 'xpath':
                webElements = \
                    WebDriverWait(self.driver, secs).until(EC.presence_of_all_elements_located((By.XPATH, element)), message=message)
            elif by == 'text':
                webElements = \
                    WebDriverWait(self.driver, secs).until(EC.presence_of_all_elements_located((By.LINK_TEXT, element)), message=message)
            elif by == 'css':
                webElements = WebDriverWait(self.driver, secs).until(EC.presence_of_all_elements_located
                                                                    ((By.CSS_SELECTOR, element)), message=message)
            elif by == 'uiautomator':
                webElements = WebDriverWait(self.driver, secs).until(EC.presence_of_all_elements_located
                                                                    ((By.ANDROID_UIAUTOMATOR, element)), message=message)
            elif by == 'accessibility id':
                webElements = WebDriverWait(self.driver, secs).until(EC.presence_of_all_elements_located
                                                                    ((By.ACCESSIBILITY_ID, element)), message=message)
            else:
                log.error('{0} Targeting elements error:"{1}", spend {2} seconds'.format(fail, css, time.time() - t1))
                # self.get_page_screenshot(case_name=element + '_元素错误', source=source)
                # BeautifulReport.add_test_img3(element + '_元素错误')
                raise NameError('Please enter the correct targeting elements,"id"、"class"、"name"、"xpath"、'
                                '"text"、"uiautomator"、"accessibility id"')
            log.info('{0} Find element "{1}" through "{2}", spend {3} seconds'.format(success, element, by, time.time() - t1))
        except Exception as e:
            log.info('{0} Unable to find element "{1}" through "{2}", spend {3} seconds'.format(fail, element, by, time.time() - t1))
            log.error(e)
            # self.get_page_screenshot(case_name=element + '_元素错误', source=source)
            # BeautifulReport.add_test_img3(element + '_元素错误')
            raise
        return webElements

    def judge_element(self, css, secs=8, source='web'):
        """
        判断元素是否存在，返回bool值和元素位置
        :param css: 定位方式和元素
        :param secs: 显示等待时间
        :return:  fla, webElement
        """
        t1 = time.time()
        if '->' not in css:
            log.info('{0} Positioning syntax errors:"{1}", lack of "->"'.format(fail, css))
            raise NameError('Positioning syntax errors, lack of "->"')
        by = css.split('->')[0]
        if by == 'uiautomator':
            ele = 'new UiSelector().text(\"' + css.split('->')[1] + '\")'
        else:
            ele = css.split('->')[1]
        flag = True
        webElement = None
        try:
            if by == 'id':
                webElement = WebDriverWait(self.driver, secs).until(EC.visibility_of_element_located((By.ID, ele)))
            elif by == 'class':
                webElement = WebDriverWait(self.driver, secs).until(EC.visibility_of_element_located((By.CLASS_NAME, ele)))
            elif by == 'text':
                webElement = WebDriverWait(self.driver, secs).until(EC.visibility_of_element_located((By.LINK_TEXT, ele)))
            elif by == 'name':
                webElement = WebDriverWait(self.driver, secs).until(EC.visibility_of_element_located((By.NAME, ele)))
            elif by == 'xpath':
                webElement = WebDriverWait(self.driver, secs).until(EC.visibility_of_element_located((By.XPATH, ele)))
            elif by == 'uiautomator':
                webElement = WebDriverWait(self.driver, secs).until(EC.visibility_of_element_located
                                                                    ((By.ANDROID_UIAUTOMATOR, ele)))
            elif by == 'accessibility id':
                webElement = WebDriverWait(self.driver, secs).until(EC.visibility_of_element_located
                                                                    ((By.ACCESSIBILITY_ID, ele)))
            else:
                flag = False
                log.info('{0} Targeting elements error:"{1}", spend {2} seconds'.format(fail, css, time.time() - t1))
                # self.get_page_screenshot(case_name=ele + '_元素错误', source=source)
                # BeautifulReport.add_test_img3(ele + '_元素错误')
                raise NameError('Please enter the correct targeting elements,"id"、"class"、"name"、"xpath"、'
                                '"text"、"uiautomator"、"accessibility id"')
            log.info('{0} Find targeting element:"{1}", spend {2} seconds'.format(success, css, time.time() - t1))
        except:
            flag = False
            log.info('{0} Unable to find element:"{1}", spend {2} seconds'.format(fail, css, time.time() - t1))

        return flag, webElement

    def judge_element_visibility(self, css, secs=5, source='web'):
        """
        判断元素是否可见（隐藏），返回bool值
        :return:
        """
        t1 = time.time()
        if '->' not in css:
            log.info('{0} Positioning syntax errors:"{1}", lack of "->"'.format(fail, css))
            raise NameError('Positioning syntax errors, lack of "->"')
        by = css.split('->')[0]
        if by == 'uiautomator':
            ele = 'new UiSelector().text(\"' + css.split('->')[1] + '\")'
        else:
            ele = css.split('->')[1]
        flag = True
        try:
            if by == 'id':
                webElement = WebDriverWait(self.driver, secs).until(EC.visibility_of_element_located((By.ID, ele)))
            elif by == 'class':
                webElement = WebDriverWait(self.driver, secs).until(EC.visibility_of_element_located((By.CLASS_NAME, ele)))
            elif by == 'text':
                webElement = WebDriverWait(self.driver, secs).until(EC.visibility_of_element_located((By.LINK_TEXT, ele)))
            elif by == 'name':
                webElement = WebDriverWait(self.driver, secs).until(EC.visibility_of_element_located((By.NAME, ele)))
            elif by == 'xpath':
                webElement = WebDriverWait(self.driver, secs).until(EC.visibility_of_element_located((By.XPATH, ele)))
            elif by == 'uiautomator':
                webElement = WebDriverWait(self.driver, secs).until(EC.visibility_of_element_located
                                                                    ((By.ANDROID_UIAUTOMATOR, ele)))
            elif by == 'accessibility id':
                webElement = WebDriverWait(self.driver, secs).until(EC.visibility_of_element_located
                                                                    ((By.ACCESSIBILITY_ID, ele)))
            else:
                log.info('{0} Targeting elements error:"{1}", spend {2} seconds'.format(fail, css, time.time() - t1))
                # self.get_page_screenshot(case_name=ele + '_元素错误', source=source)
                # BeautifulReport.add_test_img3(ele + '_元素错误')
                raise NameError('Please enter the correct targeting elements,"id"、"class"、"name"、"xpath"、'
                                '"text"、"uiautomator"、"accessibility id"')
            log.info('{0} Find targeting element:"{1}", spend {2} seconds'.format(success, css, time.time() - t1))
        except:
            flag = False
            log.info('{0} Unable to find element:"{1}", spend {2} seconds'.format(fail, css, time.time() - t1))

        return flag

    def judge_element_clickable(self, css, secs=5, source='web'):
        """
        判断元素是否可点击，返回bool值和元素位置
        :return:
        """
        t1 = time.time()
        if '->' not in css:
            log.info('{0} Positioning syntax errors:"{1}", lack of "->"'.format(fail, css))
            raise NameError('Positioning syntax errors, lack of "->"')
        by = css.split('->')[0]
        if by == 'uiautomator':
            ele = 'new UiSelector().text(\"' + css.split('->')[1] + '\")'
        else:
            ele = css.split('->')[1]
        flag = True
        webElement = None
        try:
            if by == 'id':
                webElement = WebDriverWait(self.driver, secs).until(EC.element_to_be_clickable((By.ID, ele)))
            elif by == 'class':
                webElement = WebDriverWait(self.driver, secs).until(EC.element_to_be_clickable((By.CLASS_NAME, ele)))
            elif by == 'text':
                webElement = WebDriverWait(self.driver, secs).until(EC.element_to_be_clickable((By.LINK_TEXT, ele)))
            elif by == 'name':
                webElement = WebDriverWait(self.driver, secs).until(EC.element_to_be_clickable((By.NAME, ele)))
            elif by == 'xpath':
                webElement = WebDriverWait(self.driver, secs).until(EC.element_to_be_clickable((By.XPATH, ele)))
            elif by == 'uiautomator':
                webElement = WebDriverWait(self.driver, secs).until(EC.element_to_be_clickable
                                                                    ((By.ANDROID_UIAUTOMATOR, ele)))
            elif by == 'accessibility id':
                webElement = WebDriverWait(self.driver, secs).until(EC.element_to_be_clickable
                                                                    ((By.ACCESSIBILITY_ID, ele)))
            else:
                flag = False
                log.info('{0} Targeting elements error:"{1}", spend {2} seconds'.format(fail, css, time.time() - t1))
                # self.get_page_screenshot(case_name=ele + '_元素错误', source=source)
                # BeautifulReport.add_test_img3(ele + '_元素错误')
                raise NameError('Please enter the correct targeting elements,"id"、"class"、"name"、"xpath"、'
                                '"text"、"uiautomator"、"accessibility id"')
            log.info('{0} The element:"{1}" is clickable, spend {2} seconds'.format(success, css, time.time() - t1))
        except:
            flag = False
            log.info('{0} The element:"{1}" is not clickable, spend {2} seconds'.format(fail, css, time.time() - t1))

        return flag, webElement

    def click(self, css, secs=8, source='web'):
        """
        重写click方法
        :param css:
        :param secs:
        :return:
        """
        t1 = time.time()
        try:
            ele = self.find_element(css, secs)
            ele.click()
            log.info('{0} Click element:"{1}", spend {2} seconds'.format(success, css, time.time() - t1))
        except Exception as e:
            log.info('{0} Unable to the element:"{1}", spend {2} seconds'.format(fail, css, time.time() - t1))
            log.error(e)
            self.get_page_screenshot(case_name=css + '_点击失败', source=source)
            BeautifulReport.add_test_img3(css + '_点击失败')
            raise

    def switch_new_window(self, css, secs=8):
        """
        打开新窗口并切换到新窗口
        :param css:
        :param sces:
        :return:
        """
        t1 = time.time()
        try:
            current_handle = self.driver.current_window_handle
            self.click(css, secs)
            time.sleep(2)
            all_handles = self.driver.window_handles
            for handle in all_handles:
                if handle != current_handle:
                    self.driver.switch_to.window(handle)
            log.info('{0} Click element:"css" open a new window and switch into. spend {1} seconds'.format(success, time.time() - t1))
        except Exception as e:
            log.info('{0} Click element:"css" open a new window and switch into. spend {1} seconds'.format(success, time.time() - t1))
            log.error(e)
            # self.get_page_screenshot(file_path=screenshot_path, case_name=css + '_切换新窗口失败', source='web')
            # BeautifulReport.add_test_img3(css + '_切换新窗口失败')
            raise

    def send(self, css, text, default=None, secs=8, source='web'):
        """
        输入框写入文本方法
        :param css:定位方式和元素
        :param test:输入文本
        :param default:输入框默认文本
        :param secs:查询时间
        :return:
        """
        t1 = time.time()
        try:
            ele = self.find_element(css, secs)
            self.clear_text(ele, default=default)
            ele.send_keys(text)
            log.info('{0} Send keys:"{1}" content: "{2}", spend {3} seconds'.format(success, css, text, time.time() - t1))
        except Exception as e:
            log.info('{0} Send keys:"{1}" content: "{2}", spend {3} seconds'.format(fail, css, text, time.time() - t1))
            log.error(e)
            # self.get_page_screenshot(case_name=css + '_写入失败', source=source)
            # BeautifulReport.add_test_img3(css + '_写入失败')
            raise

    def js_send(self, css, text, secs=8, source='web'):
        """使用ActionChains库操作输入框输入"""
        t1 = time.time()
        if '->' not in css:
            log.error('Positioning syntax errors. element:"{0}" lack of "->"'.format(css))
            raise NameError('Positioning syntax errors. lack of "->"')
        try:
            by = css.split('->')[0]
            element = css.split('->')[1]
            flag, ele = self.judge_element(css, secs)
            if flag:
                if by == 'id':
                    js = "document.getElementById('" + element + "').value='" + text + "';"
                elif by == 'class':
                    js = "document.getElementsByClassName('" + element + "')[0].value='" + text + "';"
                elif by == 'name':
                    js = "document.getElementByNme('" + element + "').value='" + text + "';"
                elif by == 'tagname':
                    js = "document.getElementByTagName('" + element + "').value='" + text + "';"
                elif by == 'selector':
                    js = "document.querySelector('" + element + "').value='" + text + "';"
                else:
                    log.error('Please enter the correct targeting elements,"id"、"class"、"name"、"tagname"、"selector"')
                    raise NameError('Please enter the correct targeting elements,"id"、'
                                    '"class"、"name"、"tagname"、"selector"、')
                self.js(js)
                log.info(
                    '{0} Send keys:"{1}" content uses js: "{2}", spend {3} seconds'.
                        format(success, css, text, time.time() - t1))
            else:
                log.error('{0} Send keys:"{2}", not find elementr:"{1}", spend {3} seconds'.
                          format(fail, css, text, time.time() - t1))
        except Exception as e:
            log.info('{0} Send keys:"{1}" content: "{2}", spend {3} seconds'.format(fail, css, text, time.time() - t1))
            log.error(e)
            # self.get_page_screenshot(case_name=css + '_点击失败', source=source)
            # BeautifulReport.add_test_img3(css + '_点击失败')
            raise

    def clear_text(self, ele, default=None, n=5):
        """
        清除文本框内容
        :param ele: webelement元素
        :param default: 输入框默认文本
        :param n: 循环次数
        :return:
        """
        try:
            for num in range(n):
                ele.clear()
                if ele.text == '' or ele.text == default:
                    log.info('{0} clear element: "{1}" content, this is show:"{2}"'.format(success, ele, ele.text))
                    break
                else:
                    log.info('Not clear element: "{1}" content:"{2}"'.format(success, ele, ele.text))
        except InvalidElementStateException as i:
            log.error('Not clear element: "{1}" content'.format(fail, ele))
            log.error(i)

    def get_ele_content(self, css, secs=8, source='web'):
        """
        获取元素的内容
        :param css:
        :param secs:
        :return:
        """

        t1 = time.time()
        try:
            if '->' not in str(css):
                text = css.text
            else:
                ele = self.find_element(css, secs)
                text = ele.text
            log.info('{0} Get text of element:"{1}", spend {2} seconds'.format(success, text, time.time() - t1))
        except Exception as e:
            log.error('{0} Get text of element:"{1}", spend {2} seconds'.format(fail, css, time.time() - t1))
            log.error(e)
            # self.get_page_screenshot(case_name=str(css) + '_获取元素内容失败', source=source)
            # BeautifulReport.add_test_img3(str(css) + '_获取元素内容失败')
            raise
        return text

    def get_alert_content(self, secs=1):
        """获取alert弹窗内容"""
        time.sleep(secs)
        content = self.driver.switch_to.alert().text
        return content

    def get_page_title(self, source='web'):
        """获取页面标题"""
        t1 = time.time()
        try:
            current_title = self.driver.title
            log.info(
                '{0} Get current page title:"{1}" , spend {2} seconds'.format(success, current_title, time.time() - t1))
        except Exception as e:
            log.error('Fail get current page title, spend "{1}" seconds'.format(fail, time.time() - t1))
            log.error(e)
            url = self.get_page_url()
            self.get_page_screenshot(case_name=url + '_获取页面标题失败', source=source)
            BeautifulReport.add_test_img3(url + '_获取页面标题失败')
            raise
        return current_title

    def get_page_url(self, source='web'):
        """获取当前页面链接"""
        t1 = time.time()
        try:
            current_url = self.driver.current_url
            log.info('{0} Get current page link:"{1}" , spend {2} seconds'.format(success, current_url, time.time() - t1))
        except Exception as e:
            log.error('Fail get current page link, spend "{1}" seconds'.format(fail, time.time() - t1))
            log.error(e)
            title = self.get_page_title()
            self.get_page_screenshot(case_name=title + '_获取页面链接失败', source=source)
            BeautifulReport.add_test_img3(title + '_获取页面链接失败')
            raise
        return current_url

    def get_page_screenshot(self, file_path=img_path, case_name='bug', source='web', sces=1):
        """
        获取页面截图
        :param file_name:图片存储目录路径
        :param source:来源：web or webview or app or other
        """
        time.sleep(1)
        t1 = time.time()
        img_name = case_name + '.png'
        try:
            self.driver.save_screenshot(os.path.join(file_path, img_name))  # 截取当前页面图片
            # print("screenshot:", img_name)  # 图片写入测试报告
            if source == 'webview':
                self.switch_app_context()
            log.info('{0} Get current page screenshot, spend {1} seconds'.format(success, time.time() - t1))
        except Exception as e:
            log.error('{0} Get current page screenshot, spend {1} seconds'.format(fail, time.time() - t1))
            log.error(e)
            raise

    def get_element_attribute(self, css, name):
        """
        获取元素属性值
        :param css:element
        :param name:属性名称
        :return value:返回属性的值
        """
        try:
            ele = self.find_element(css)
            value = ele.get_attribute(name)
            log.info('成功获取到元素: "{}" 属性值"{}": "{}"'.format(css, name, value))
        except BaseException as b:
            log.error('获取元素属性值失败，原因：{}'.format(b))
            raise
        return value

    def quit(self, sces=1):
        """关闭窗口/app"""
        time.sleep(sces)
        t1 = time.time()
        self.driver.quit()
        log.info('{0} Quit window/app. spend {1} seconds'.format(success, time.time() - t1))

    def action_perform(self, action):
        """
        执行action事件
        :param action:
        :return:
        """
        try:
            action.perform()
            log.info('{0} Execution event!'.format(success))
        except Exception as e:
            log.info('{0} Execution event!'.format(fail))
            log.error(e)
            raise

    def hover_element(self, css, secs=8):
        """
        鼠标悬停在元素上
        :param css:
        :param secs:
        :return:
        """
        t1 =time.time()
        try:
            ele = self.find_element(css, secs)
            action = ActionChains(self.driver)
            action.move_to_element(ele)
            self.action_perform(action)
            log.info('{0} Hover to element:"{1}" , spend {2} seconds'.format(success, css, time.time() - t1))
        except Exception as e:
            log.info('{0} Hover to elementt:"{1}", spend {2} seconds'.format(success, css, time.time() - t1))
            log.error(e)
            raise

    def move_element(self, events):
        """
        移动元素
        :param events:list参数，事件起始,->隔开
        :return:
        """
        t1 = time.time()
        try:
            action = ActionChains(self.driver)
            for event in events:
                if '->' not in event:
                    log.error('{0} Get events:{1},lack of "->"'.format(fail, events))
                    raise NameError('Positioning syntax errors. element:"{0}" lack of "->"'.format(events))
                source = event.split('->')[0]
                target = event.split('->')[1]
                action.drag_and_drop(source, target)
                log.info('{0} Join event:{1},lack of "->"'.format(fail, event, time.time() - t1))
            self.action_perform(action)
            log.info('{0} Execution move event, spend {1} seconds'.format(success, time.time() - t1))
        except Exception as e:
            log.info('{0} Execution move events:{1}, spend {2} seconds'.format(fail, events, time.time() - t1))
            log.error(e)
            raise

    def move_offset(self, css, x_move, y_move=0, num=1, square=1):
        """根据坐标移动"""
        draggable = self.find_element(css)
        # 鼠标按住滑块元素
        ActionChains(self.driver).click_and_hold(draggable).perform()

        n = int(x_move / square)
        # 通过多次拖动来控制速度
        for i in range(num):
            if x_move - n * i < n:
                n = x_move % square
            if y_move - n * i < n:
                y_move = y_move % square
            # 拖动鼠标
            ActionChains(self.driver).move_by_offset(xoffset=n, yoffset=y_move).perform()
        # 释放鼠标
        ActionChains(self.driver).release().perform()

    def win_scroll_page(self, num='0, 200'):
        """window系统滚动页面"""
        if ',' not in num:
            raise NameError('Positioning syntax errors. lack of ","')
        scroll = 'window.scrollBy(' + num + ')'
        self.js(scroll)

    def js(self, js):
        """调用js语句"""
        t1 = time.time()
        try:
            self.driver.execute_script(js)
            log.info('{0} Execute script: "{1}", spend {2} seconds'.format(success, js, time.time() - t1))
        except Exception as e:
            log.info('{0} Unable to execute script: "{1}", spend {2} seconds'.format(fail, js, time.time() - t1))
            log.error(e)
            raise

    def back_button(self, num=1):
        """
        返回按钮事件
        :param num:返回次数
        :return:
        """
        for i in range(num):
            self.driver.back()

    def get_page_source(self, filename=None, secs=2):
        """
        获取页面代码
        :param secs:
        :param filename: 文件名称，后缀为.html
        :return:
        """
        time.sleep(secs)
        page = self.driver.page_source
        file_path = os.path.join(path, 'xiaoe', filename)
        html_file = open(file_path, 'w', encoding='utf-8')
        html_file.write(page)
        time.sleep(secs)
        html_file.close()

    def get_current_handle(self):
        """
        获取当前页面窗口句柄
        :return:
        """
        current_handle = self.driver.current_window_handle
        return current_handle

    def get_handles(self):
        """
        获取所有窗口句柄
        :return:
        """
        handles = self.driver.window_handles
        return handles

    def switch_iframe(self, iframe, ces=0.1):
        """切换iframe"""
        time.sleep(ces)
        try:
            self.driver.switch_to.frame(iframe)
            log.info('成功切换iframe窗口: {}'.format(iframe))
        except BaseException as b:
            log.error('切换iframe窗口失败，原因: {}'.format(b))
            raise

    def switch_handle(self, handle):
        """切换handle"""
        try:
            self.driver.switch_to.window(handle)
            log.info('成功切换handle窗口: {}'.format(handle))
        except BaseException as b:
            log.error('切换handle窗口失败，原因: {}'.format(b))
            raise

    """--------------------------------------------------mobile private-----------------------------------"""
    def app_background(self, secs=2):
        """
        app后台运行
        :param secs: 后台运行时间
        :return:
        """
        self.driver.background_app(secs)

    def get_app_context(self):
        """获取app当前的context"""
        current_context = self.driver.current_context
        return current_context

    def get_app_contexts(self):
        """获取app所有context"""
        contexts = self.driver.contexts
        return contexts

    def get_app_activity(self):
        """获取app的activity"""
        activity = self.driver.current_activity
        return activity.split('.')[-1]

    def wait_activity(self, activity, timeout=8, interval=1):
        """
        等待activity出现
        :param activity:需要等待的activity
        :param timeout: 超时时间
        :param interval: 轮询查找activity时间
        :return:
        """
        t1 = time.time()
        try:
            self.driver.wait_activity(activity, timeout, interval)
            log.info('{0} Find the activity:{1}, spend {2} seconds'.format(success, activity, time.time() - t1))
        except Exception as e:
            log.info('{0} Not find the activity:{1}， spend {2} seconds'.format(fail, activity, time.time() - t1))
            log.error(e)
            self.get_page_screenshot(file_path=screenshot_path, case_name=activity + '_等待activity', source='app')
            BeautifulReport.add_test_img3(activity + '_等待activity')
            raise

    def switch_context(self, context):

        self.driver._switch_to.context(context)

    def switch_app_context(self, secs=0.5):
        """切换app的context"""
        time.sleep(secs)
        t1 = time.time()
        try:
            current_context = self.driver.context
            contexts = self.driver.contexts
            for context in contexts:
                if context != current_context:
                    log.info('{0} Get context:"{1}"'.format(success, context))
                    self.driver._switch_to.context(context)
                    log.info('{0} switch to context:"{1}", spend {2} seconds'.format(success, context, time.time() - t1))
                else:
                    log.info('{0} Context equal current context:"{1}", spend {2} seconds'.
                             format(fail, context, time.time() - t1))
        except Exception as e:
            log.info('{0} switch to context, spend {1} seconds'.format(fail, time.time() - t1))
            log.error(e)
            raise

    def clear_app_text(self, css):
        """
        通过键值清空输入框
        :param text:输入框文本内容
        :param sourrce:输入框来源；app or webview
        :return:
        """
        t1 = time.time()
        try:
            self.click(css)
            text = self.get_ele_content(css)
            self.driver.keyevent(123)
            for i in range(len(text)):
                self.driver.keyevent(67)
            log.info('{0} clear app:"{1}" content:"{2}", spend {3} seconds'.format(success, css, text, time.time() - t1))
        except Exception as e:
            log.error(
                '{0} clear app:"{1}" content, spend {2} seconds'.format(fail, css, time.time() - t1))
            log.error(e)
            raise

    def slipe_up_window(self, num=1):
        """
        向上滑动页面
        num:传入次数，控制滑动次数
        """
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        x1 = width * 0.5
        y1 = height * 0.8
        y2 = height * 0.2
        for i in range(num):
            self.driver.swipe(x1, y1, x1, y2)
            time.sleep(1)

    def slipe_under_window(self, num=1):
        """
        向下滑动页面
        num:传入次数，控制滑动次数
        """
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        x1 = width * 0.5
        y1 = height * 0.4
        y2 = height * 0.8
        for i in range(num):
            self.driver.swipe(x1, y1, x1, y2)
            time.sleep(1)

    """--------------------------------------------------pc private-----------------------------------"""
    def positipo_window(self, title, class_name=None, timeout=3):
        """
        定位窗口
        title:  窗口标题
        class_name: 窗口class
        timeout：等待时间
        :return:
        """
        win = self.driver.window(title=title, class_name=class_name)
        win.wait('exists ready', timeout=timeout, retry_interval=1)
        return win

    def get_exe_controls(self, title, class_name=None, timeout=8):
        """
        获取exe应用控件和属性
        title:  窗口标题
        class_name: 窗口class
        timeout：等待时间
        :return:
        """
        win = self.positipo_window(title=title, timeout=timeout)
        win.print_control_identifiers()

    def click_exe(self, control, title, class_name=None, timeout=8):
        """
        exe应用click事件
        :return:
        """
        win = self.positipo_window(title=title, timeout=timeout)
        win[control].click()

    def checkbox_exe(self, control, title, class_name=None, timeout=8):
        """
        勾选checkbox按钮
        :return:
        """
        win = self.positipo_window(title=title, timeout=timeout)

        win[control].uncheck()








