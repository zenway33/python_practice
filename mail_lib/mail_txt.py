import smtplib
import email.mime.multipart
import email.mime.text

msg=email.mime.multipart.MIMEMultipart()
msg['from']='ustchacker@tom.com'
msg['to']='blablabla@aliyun.com'
msg['subject']='test'
content='''
	你好，
	        这是一封自动发送的邮件。

        www.ustchacker.com
'''
txt=email.mime.text.MIMEText(content)
msg.attach(txt)

smtp=smtplib
smtp=smtplib.SMTP()
smtp.connect('smtp.tom.com','25')
smtp.login('ustchacker@tom.com','password')
smtp.sendmail('ustchacker@tom.com','blablabla@aliyun.com',str(msg))
smtp.quit()

#     smtplib模块是smtp简单邮件传输协议客户端的实现，为了通用性，有时候发送邮件的时候要带附件或图片，用email.mime来装载内
