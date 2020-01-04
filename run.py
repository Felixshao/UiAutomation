import time
from common.runReport import run_report
from common.sendEmail import send_annex_email
from common.clearFolder import clearFolder

clear = clearFolder()


if __name__ == '__main__':

    t1 = time.time()
    clear.clear_folder()    # 清空截图
    # run_report().run_html()     # 运行用例并生成报告
    run_report().moreProcess_report()
    # run_report().thread_run_Beautifuhtml()
    # send_annex_email()          # 发送报告邮件
    print('总耗时:', time.time() - t1)

