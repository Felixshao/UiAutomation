import pyautogui, pywinauto, subprocess
from time import sleep
from pywinauto import application, ElementNotFoundError
from config.readConfig import readConfig
from common.log import Logger


log = Logger('common.openPC.py').get_logger()
pyautogui.FAILSAFE = False      # 关闭保障，否则jenkins调用时报pyautogui.FailSafeException异常
pyautogui.PAUSE = 1     # 设置gui延迟，默认延迟0.1s


def open_pc_yesheng():
    """打开夜神模拟器"""
    file_path = readConfig().get_exe()['yesheng']
    app = application.Application(backend='uia')
    try:
        app.connect(title_re='夜神模拟器', class_name='Qt5QWindowIcon')
    except ElementNotFoundError:
        app.start(file_path)
    log.info('Sucess open 夜神模拟器!')


def open_pc_appium():
    """打开appium"""
    file_path = readConfig().get_exe()['appium']    # 读取appium.exe文件路径
    app = application.Application(backend='uia')    # 定义application实例
    # app.start(file_path)
    # sleep(2)
    # print(pywinauto.findwindows.find_elements(title='Appium'))
    app.connect(title_re='Appium', class_name='Chrome_WidgetWin_1')
    appium = app.window(title='Appium')     # 指定窗口
    appium.wait("exists ready", timeout=3, retry_interval=3)  # 等待窗口就绪
    # sleep(5)
    appium.print_control_identifiers()
    appium.Button4.click()      # 点击指定按钮（Button4）
    log.info('Sucess start appium!')


def notebook():
    file_path = 'Notepad.exe'
    app = application.Application(backend='uia')
    # app.start('Notepad.exe')
    app.connect(title_re='无标题 - 记事本', class_name='Notepad')
    note = app.window(title='无标题 - 记事本')
    note.draw_outline()
    note.print_control_identifiers()
    note.Edit.ScrollBar.Button2.click()


if __name__ == '__main__':
    open_pc_appium()
    # pass


