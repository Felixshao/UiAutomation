from twilio.rest import Client
from config.readConfig import readConfig
from common.log import Logger

twilio_data = readConfig().get_sms()
log = Logger('common.SMS.py').get_logger()
client = Client(twilio_data['account_sid'], twilio_data['account_token'])   # 配置twilio


def send_msg(body, to=twilio_data['to'], from_=twilio_data['from']):
    """通过twilio发送短信"""
    try:

        message = client.messages.create(to=to, from_=from_, body=body)    # 新建短信
        log.info('Success send messages, messages sid:{0}, body:{1}'.format(message.sid, message.body))
    except Exception as e:
        log.error('Fail send messages!')
        log.error(e)
        print('发送短信失败，错误原因:{}'.format(e))


def call_num():
    """通过twilio打电话"""
    try:
        call = client.calls.create(to=twilio_data['to'], from_=twilio_data['from'],
                                   url='http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient')    # 新建短信
        log.info('Success send messages, messages sid:{0}, music'.format(call.sid))
    except Exception as e:
        log.error('Fail send messages!')
        log.error(e)
        print('拨打电话失败，错误原因:{}'.format(e))


if __name__ == '__main__':
    send_msg('zhe is code!')

