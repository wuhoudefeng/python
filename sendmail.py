import smtplib
import email.mime.multipart
import email.mime.text

msg = email.mime.multipart.MIMEMultipart()
msg['from'] = '3012522652@qq.com'
msg['to'] = '2662643959@qq.com'
msg['subject'] = 'test'
content = '''''
    你好，
            这是一封自动发送的邮件。


'''
txt = email.mime.text.MIMEText(content)
msg.attach(txt)

#smtp = smtplib
smtp = smtplib.SMTP()
smtp.connect('smtp.qq.com', '465')
smtp.login('3012522652@qq.com', '13579df.')
smtp.sendmail('3012522652@qq.com', '2662643959@qq.com', str(msg))
smtp.quit()