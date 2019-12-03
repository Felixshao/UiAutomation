import os
import time
from config.getMobile import get_mobile
from common.log import Logger
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy as By
from selenium.webdriver.common.action_chains import ActionChains

phone_data = get_mobile()[1]
log = Logger('common.mySelenium').get_logger()
success = 'Success'
fail = 'Fail'


class mySelenium():

    def __init__(self):
        pass

    def browser(self, browser='chrome'):
        """
        配置浏览器
        :param browser:
        """
        log.info('Start a new browser: {0}'.format(browser))
        if browser == 'chrome' or browser == 'CHROME':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox' or browser == 'FIREFOX':
            self.driver = webdriver.Firefox()
        elif browser == 'ie' or browser == 'IE':
            self.driver = webdriver.Ie()
        else:
            log.error("Not found '{0}' browser.you can enter 'chrome' 'firefox' or 'ie'".format(browser))
            raise NameError("Not found '{0}' browser.you can enter 'chrome' 'firefox' or 'ie'".format(browser))
        log.info('{0} Open "{1}" browser.'.format(success, browser))
        return self.driver

    def mobile(self, data=phone_data):
        """
        配置app
        :return:
        """
        t1 = time.time()
        from appium import webdriver
        try:
            self.driver = webdriver.Remote(data['appium_url'], data)
            log.info('{0} Open "{1}" app, spend {2} seconds'.format(success, data['Appname'], time.time() - t1))
        except Exception as e:
            log.info('{0} to open "{1}" app, spend {2} seconds'.format(fail, data['Appname'], time.time() - t1))
            log.error(e)
            raise

    def open_url(self, url):
        t1 = time.time()
        try:
            self.driver.get(url)
            log.info('{0} Open url: {1}, spend {2} seconds'.format(success, url, time.time() - t1))
        except Exception as e:
            log.info('Open link {0}: {1}, spend {2} seconds'.format(fail, url, time.time() - t1))
            log.error(e)
            raise

    def max_window(self):
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
            raise

    def find_element(self, css, secs=8):
        """
        封装查找元素方法，加入WebDriverWait
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
                webElement = \
                    WebDriverWait(self.driver, secs).until(EC.presence_of_element_located((By.ID, element)), message=message)
            elif by == 'class':
                webElement = \
                    WebDriverWait(self.driver, secs).until(EC.presence_of_element_located((By.CLASS_NAME, element)), message=message)
            elif by == 'name':
                webElement = \
                    WebDriverWait(self.driver, secs).until(EC.presence_of_element_located((By.NAME, element)), message=message)
            elif by == 'xpath':
                webElement = \
                    WebDriverWait(self.driver, secs).until(EC.presence_of_element_located((By.XPATH, element)), message=message)
            elif by == 'text':
                webElement = \
                    WebDriverWait(self.driver, secs).until(EC.presence_of_element_located((By.LINK_TEXT, element)), message=message)
            elif by == 'css':
                webElement = WebDriverWait(self.driver, secs).until(EC.presence_of_all_elements_located
                                                                    ((By.CSS_SELECTOR, element)), message=message)
            elif by == 'uiautomator':
                webElement = WebDriverWait(self.driver, secs).until(EC.presence_of_element_located
                                                                    ((By.ANDROID_UIAUTOMATOR, element)), message=message)
            elif by == 'accessibility id':
                webElement = WebDriverWait(self.driver, secs).until(EC.presence_of_element_located
                                                                    ((By.ACCESSIBILITY_ID, element)), message=message)
            else:
                log.error('{0} Targeting elements error:"{1}", spend {2} seconds'.format(fail, css, time.time() - t1))
                raise NameError('Please enter the correct targeting elements,"id"、"class"、"name"、"xpath"、'
                                '"text"、"uiautomator"、"accessibility id"')
            log.info('{0} Find element "{1}" through "{2}", spend {3} seconds'.format(success, element, by, time.time() - t1))
        except Exception as e:
            log.info('{0} Unable to find element "{1}" through "{2}", spend {3} seconds'.format(fail, element, by, time.time() - t1))
            log.error(e)
            raise
        return webElement

    def judge_element_presence(self, css, secs=5):
        """
        判断元素是否存在，返回bool值
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
                webElement = WebDriverWait(self.driver, secs).until(EC.presence_of_element_located((By.ID, ele)))
            elif by == 'class':
                webElement = WebDriverWait(self.driver, secs).until(EC.presence_of_element_located((By.CLASS_NAME, ele)))
            elif by == 'text':
                webElement = WebDriverWait(self.driver, secs).until(EC.presence_of_element_located((By.LINK_TEXT, ele)))
            elif by == 'name':
                webElement = WebDriverWait(self.driver, secs).until(EC.presence_of_element_located((By.NAME, ele)))
            elif by == 'xpath':
                webElement = WebDriverWait(self.driver, secs).until(EC.presence_of_element_located((By.XPATH, ele)))
            elif by == 'uiautomator':
                webElement = WebDriverWait(self.driver, secs).until(EC.presence_of_element_located
                                                                    ((By.ANDROID_UIAUTOMATOR, ele)))
            elif by == 'accessibility id':
                webElement = WebDriverWait(self.driver, secs).until(EC.presence_of_element_located
                                                                    ((By.ACCESSIBILITY_ID, ele)))
            else:
                flag = False
                log.info('{0} Targeting elements error:"{1}", spend {2} seconds'.format(fail, css, time.time() - t1))
                raise NameError('Please enter the correct targeting elements,"id"、"class"、"name"、"xpath"、'
                                '"text"、"uiautomator"、"accessibility id"')
            log.info('{0} Find targeting element:"{1}", spend {2} seconds'.format(success, css, time.time() - t1))
        except:
            flag = False
            log.info('{0} Unable to find element:"{1}", spend {2} seconds'.format(fail, css, time.time() - t1))

        return flag, webElement

    def judge_element_clickable(self, css, secs=5):
        """
        判断元素是否存在，返回bool值
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
                raise NameError('Please enter the correct targeting elements,"id"、"class"、"name"、"xpath"、'
                                '"text"、"uiautomator"、"accessibility id"')
            log.info('{0} The element:"{1}" is clickable, spend {2} seconds'.format(success, css, time.time() - t1))
        except:
            flag = False
            log.info('{0} The element:"{1}" is not clickable, spend {2} seconds'.format(fail, css, time.time() - t1))

        return flag, webElement

    def judge_element(self, css, secs=5):
        """
        判断元素是否存在，返回bool值
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
                webElement = WebDriverWait(self.driver, secs).until(EC.presence_of_element_located((By.ID, ele)))
            elif by == 'class':
                webElement = WebDriverWait(self.driver, secs).until(EC.presence_of_element_located((By.CLASS_NAME, ele)))
            elif by == 'text':
                webElement = WebDriverWait(self.driver, secs).until(EC.presence_of_element_located((By.LINK_TEXT, ele)))
            elif by == 'name':
                webElement = WebDriverWait(self.driver, secs).until(EC.presence_of_element_located((By.NAME, ele)))
            elif by == 'xpath':
                webElement = WebDriverWait(self.driver, secs).until(EC.presence_of_element_located((By.XPATH, ele)))
            elif by == 'uiautomator':
                webElement = WebDriverWait(self.driver, secs).until(EC.presence_of_element_located
                                                                    ((By.ANDROID_UIAUTOMATOR, ele)))
            elif by == 'accessibility id':
                webElement = WebDriverWait(self.driver, secs).until(EC.presence_of_element_located
                                                                    ((By.ACCESSIBILITY_ID, ele)))
            else:
                flag = False
                log.info('{0} Targeting elements error:"{1}", spend {2} seconds'.format(fail, css, time.time() - t1))
                raise NameError('Please enter the correct targeting elements,"id"、"class"、"name"、"xpath"、'
                                '"text"、"uiautomator"、"accessibility id"')
            log.info('{0} Find targeting element:"{1}", spend {2} seconds'.format(success, css, time.time() - t1))
        except:
            flag = False
            log.info('{0} Unable to find element:"{1}", spend {2} seconds'.format(fail, css, time.time() - t1))

        return flag, webElement

    def click(self, css, secs=8):
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
            raise

    def open_new_window(self, css, sces=8):
        """
        打开新窗口并切换到新窗口
        :param css:
        :param sces:
        :return:
        """
        t1 = time.time()
        try:
            current_handle = self.driver.current_window_handle
            self.click(css, sces)
            all_handles = self.driver.window_handles
            for handle in all_handles:
                if handle != current_handle:
                    self.driver.switch_to.window(handle)
            log.info('{0} Click element:"css" open a new window and switch into. spend {1} seconds'.format(success, time.time() - t1))
        except Exception as e:
            log.info('{0} Click element:"css" open a new window and switch into. spend {1} seconds'.format(success, time.time() - t1))
            log.error(e)
            raise

    def send(self, css, test, secs=8):
        """
        输入框写入文本方法
        :param css:
        :param test:
        :param secs:
        :return:
        """
        t1 = time.time()
        try:
            ele = self.find_element(css, secs)
            ele.clear()
            ele.send_keys(test)
            log.info('{0} Send keys:"{1}" content: "{2}", spend {3} seconds'.format(success, css, test, time.time() - t1))
        except Exception as e:
            log.info('{0} Send keys:"{1}" content: "{2}", spend {3} seconds'.format(fail, css, test, time.time() - t1))
            log.error(e)
            raise

    def get_ele_content(self, css, secs=8):
        """
        获取元素的内容
        :param css:
        :param secs:
        :return:
        """
        t1 = time.time()
        try:
            ele = self.find_element(css, secs)
            text = ele.text
            log.info('{0} Get text of element:"{1}", spend {2} seconds'.format(success, css, time.time() - t1))
        except Exception as e:
            log.info('{0} Get text of element:"{1}", spend {2} seconds'.format(fail, css, time.time() - t1))
            log.error(e)
            raise
        return text

    def quit(self):
        """关闭窗口/app"""
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

    def js(self, js):

        t1 = time.time()
        try:
            self.driver.execute_script(js)
            log.info('{0} Execute script: "{1}", spend {2} seconds'.format(success, js, time.time() - t1))
        except Exception as e:
            log.info('{0} Unable to execute script: "{1}", spend {2} seconds'.format(fail, js, time.time() - t1))
            log.error(e)
            raise

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
            raise

    """--------------------------------------------------mobile private-----------------------------------"""
    def send_app_text(self, css, text, secs=8):

        content = self.get_ele_content(css)
        self.click(css)
        self.driver.keyevent(123)   # 移动光标到末尾
        for i in range(len(content)):
            self.driver.keyevent(67)    # 操作退格键
        # self.send(css, text)
        ele = css.split('->')[1]
        # self.driver.set_value(ele, text)
        self.driver.find_element()










