import datetime
import time

from twilio.rest import Client


def prin():
    current_time = datetime.datetime.now()
    print(current_time, type(current_time.hour))
    # if int(current_time) >= 17:
    #     print(1)
    # else:
    #     print(2)


def send_msg():
    account_sid = 'ACefb05e1bae528c777e0ef1582495d5d3'
    account_token = '2d5880790bcbffff800401823630d892'
    client = Client(account_sid, account_token)
    accend = '你好'
    # body = 'hello, 600223 stocks fall warning, the drop is: -8.01, Current stock price is: 8.38'
    body = 'fall warning:-7.01%, price:8.38; stock:600223'
    message = client.messages.create(to='+8618598270580', from_='+12626714958', body=body)
    print(message.sid, message.body)


if __name__ == '__main__':
    prin()
    # import datetime
    # data = datetime.datetime.now().isocalendar()
    # print(str(data[0]) + str(data[0] / 7))
    # print(str(data[0]) + str(data[1]-1))
    # print(datetime.datetime.now())

