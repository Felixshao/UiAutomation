from common.runReport import run_report
from common.sendEmail import send_annex_email

if __name__ == '__main__':

    run_report().run_html()     # 运行用例并生成报告
    # send_annex_email()          # 发送报告邮件