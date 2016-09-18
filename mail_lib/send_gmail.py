#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
#from email.MIMEText import MIMEText
from email.mime.text import MIMEText
#from email.Utils import formatdate
from email.utils import formatdate
from email.utils import formataddr
from email.header import Header


def create_message(from_addr, to_addr, subject, body):
    '''指定された引数を使用して e-mail 用のメッセージオブジェクトを作成します。
    '''
    encoding = 'utf-8'
    sender_name = Header( '黒ヤギさん', encoding ).encode()
    recipient_name = Header('白ヤギさん', encoding ).encode()
    
    message = MIMEText( body.encode( encoding ), 'plain', _charset=encoding )
    message['Subject'] = Header( subject, encoding )
    message['From'] = formataddr( ( sender_name, from_addr ) )
    message['To'] = formataddr( ( recipient_name, to_addr ) )
    message['Date'] = formatdate()
    return message

# def send(from_addr, to_addr, message):
#     smtp = smtplib.SMTP()
#     smtp.sendmail( from_addr, [ to_addr ], message.as_string() )
#     smtp.close()

def send_via_gmail(from_addr, to_addr, message):
    '''message を from_addr を送信元として to_addr に送信します。
    '''
    print( 'create SMTP object' )
    smtp = smtplib.SMTP( 'smtp.gmail.com', 587 )
    print( 'ehlo1' )
    smtp.ehlo()
    print( 'starttls' )
    smtp.starttls()
    print( 'ehlo2' )
    smtp.ehlo()
    print( 'login' )
    smtp.login( from_addr, 'aaaabbbbccccdddd' )
    print( 'sendmail' )
    smtp.sendmail( from_addr, [ to_addr ], message.as_string() )
    print( 'close' )
    smtp.close()

if __name__ == '__main__':
    from_addr = 'from@gmail.com'
    to_addr = 'to@gmail.com'
    message = create_message( from_addr, to_addr, 'テストメールです', 'こんにちはこんにちは' )
    send_via_gmail( from_addr, to_addr, message )
