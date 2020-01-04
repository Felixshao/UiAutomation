import time
import os
import yagmail
from config.getProjectPath import get_project_path
from config.readConfig import readConfig
from common.log import Logger

path = get_project_path()
email_data = readConfig().get_email()
load_time = time.strftime('%Y-%m-%d', time.localtime())
log_path = os.path.join(path, 'report', 'log', 'logs' + str(load_time) + '.log')
report_path = os.path.join(path, 'report', 'report', 'report.html')
log = Logger('sendEmail').get_logger()


def send_annex_email():
    """
    发送附件邮件
    :return: 
    """
    t1 = time.time()
    try:

        if email_data['on_off'] == 'on':
            email = yagmail.SMTP(user=email_data['user'], password=email_data['password'], host=email_data['host'])
            content = '自动化报告' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            file_name = [report_path, log_path]
            email.send(to=email_data['email_to'], subject='自动化报告' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                       contents=content, attachments=file_name)
            log.info('Success send report to email: "{0}", spend {1} seconds'.format(email_data['email_to'], time.time() - t1))
        else:
            print('Mail switch is shutdown,please open mail switch in the config.ini!')
            log.info('Mail switch is shutdown,please open mail switch in the config.ini!')
    except Exception as e:
        log.info('Fail send report to email: "{0}", spend {1} seconds'.format(email_data['email_to'], time.time() - t1))
        log.error(e)
        raise


def send_body_email():
    content = '自动化报告' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    

