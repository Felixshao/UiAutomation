from pywinauto import application


def open_pc_notepad():
    """操作pc记事本应用"""
    # 连接pc应用方式一，backend参数传入应用的backend(使用inspect工具查看)， start发放传入应用exe路径并打开应用
    app = application.Application(backend='uia')
    app.start('notepad.exe')
    # 连接方式二, 传入已打开应用的进程id，在任务管理器可找到
    # app2 = application.Application(backend='uia').start('14260')

    dlg = app.window(title='无标题 - 记事本')     # 选择窗口
    dlg.menu_select(r'帮助(H)->关于记事本(A)')     # 选择应用控件


if __name__ == '__main':
    open_pc_notepad()