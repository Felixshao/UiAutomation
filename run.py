#! F:/test/python/python.exe
# Filename: run.py

import time
import sys
import os
from common.runReport import run_report
from common.sendEmail import send_annex_email
from common.clearFolder import clearFolder

# 设置启动目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
clear = clearFolder()


if __name__ == '__main__':

    t1 = time.time()
    clear.clear_screenshot()    # 清空截图
    clear.clear_report()  # 清空报告
    # run_report().moreProcess_report()   # 多进程运行用例并生成报告
    # run_report().run_html()
    run_report().pool_report()  # 多进程运行用例并生成报告
    # run_report().run_html()     # 运行用例并生成报告
    send_annex_email()          # 发送报告邮件
    print('总耗时:', time.time() - t1)
