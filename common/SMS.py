from twilio.rest import Client
from config.readConfig import readConfig
from common.log import Logger

twilio_data = readConfig().get_sms()
log = Logger('common.SMS.py').get_logger()


def twilio_sms(body):
    """通过twilio发送短信"""
    try:
        client = Client(twilio_data['account_sid'], twilio_data['account_token'])   # 配置twilio
        message = client.messages.create(to=twilio_data['to'], from_=twilio_data['from'], body=body)    # 新建短信
        log.info('Success send messages, messages sid:{0}, body:{1}'.format(message.sid, message.body))
    except Exception as e:
        log.error('Fail send messages!')
        log.error(e)
        print('发送短信失败，错误原因:{}'.format(e))
