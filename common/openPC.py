import pyautogui
from time import sleep
from pywinauto import application, ElementNotFoundError
from config.readConfig import readConfig
from common.log import Logger


log = Logger('common.openPC.py').get_logger()


def open_pc_yesheng():
    """打开夜神模拟器"""
    file_path = readConfig().get_exe()['yesheng']
    app = application.Application(backend='uia')
    try:
        app.connect(title_re='夜神模拟器', class_name='Qt5QWindowIcon')
    except ElementNotFoundError:
        app.start(file_path)


def open_pc_appium():
    """打开appium"""
    file_path = readConfig().get_exe()['appium']
    app = application.Application(backend='uia')
    app.start(file_path, timeout=10)
    sleep(5)
    # appium = app.window(title='Appium')
    # appium.print_control_identifiers()
    pyautogui.moveTo(951, 654)  # 鼠标放置appium  start按钮处
    pyautogui.click()       # 点击


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
    # notebook()
    open_pc_yesheng()
    # open_pc_yesheng()


