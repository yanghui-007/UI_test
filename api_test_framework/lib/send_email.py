import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  #混合MIME格式，支持上传附件
from email.header import Header  #用于使用中文邮件主题
import unittest


def send_email(report_file):
    msg=MIMEMultipart()  #混合MIME格式

    msg.attach(MIMEText(open(report_file,encoding='utf-8').read(),'html','utf-8'))#添加html格式邮件正文（会丢失css）


    #msg['From']='yanghui1234561@163.com'#发件人
    msg['From']='yh@juwan.group'#发件人
    msg['To']='yanghui1234561@163.com'#收件人
    msg['Subject']=Header('接口测试报告','utf-8')#中文邮件主题，指定utf-8编码

    att1=MIMEText(open(report_file,'rb').read(),'base64','utf-8')#二进制格式打开
    att1["Content-Type"]='application/octet-stream'
    att1["Content-Disposition"]='attachment;filename="rep,d"'#filename为邮件中附件显示的名字
    msg.attach(att1)


    try:
        #smtp=smtplib.SMTP_SSL('smtp.163.com')#smtp服务地址，使用SSL模式
        smtp=smtplib.SMTP_SSL('smtp.exmail.qq.com')#smtp服务地址，使用SSL模式
        #smtp.login('yanghui1234561@163.com','123456ace')#用户名和密码
        smtp.login('yh@juwan.group','Sbnisf82V9WCwhrH')#用户名和密码
       # smtp.sendmail("yanghui1234561@163.com","yanghui1234561@163.com",msg.as_string())#第一个是发送的邮箱，第二个是接收邮件的邮箱
        smtp.sendmail("yh@juwan.group","yh@juwan.group",msg.as_string())#第一个是发送的邮箱，第二个是接收邮件的邮箱
    except Exception as e:
        print(e)

    finally:
        smtp.quit()

if __name__=='__main__':
    unittest.main(verbosity=2)
    #send_email('report.html')