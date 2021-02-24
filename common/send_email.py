from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from read_config import ReadConfig
import os
from all_path import Paths


def send_email(latest_report):
    '''
    发送测试报告邮件
    :param latest_report:
    :return:
    '''
    # 将对应SMTP的配置信息进行赋值
    # email_config = ReadConfig()
    # print(email_config)
    cf = ReadConfig()
    smtp_server = cf.get_email('email_server')
    smtp_port = cf.get_email('email_server_port')
    user = cf.get_email('email_username')
    password = cf.get_email('email_passwd')
    from_address = cf.get_email('email_from_address')
    email_receives = cf.get_email('email_receiver')
    security = cf.get_email('email_security')
    # receives = email_receives.split(',')
    subject = 'UI自动化测试报告'
    latest_report = latest_report.replace('\\', '/')

    f = open(latest_report, 'r')
    mail_content = f.read()
    f.close()

    # 构造附件内容
    att = MIMEText(mail_content, 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment;filename="{}"'.format(latest_report.split('/')[-1])

    # 构建发送与接收信息
    msg = MIMEMultipart()
    msg.attach(MIMEText(mail_content, 'html', 'utf-8'))

    msg['subject'] = subject
    msg['From'] = from_address
    msg['To'] = email_receives
    msg.attach(att)

    # 发送附件图片
    pic = os.listdir(Paths.error_img)
    if len(pic) != 0:
        for i in pic:
            with open(os.path.join(Paths.error_img, i), 'rb') as f:
                img_data = f.read()
            msg_img = MIMEImage(img_data, _subtype='octet-stream')
            msg_img.add_header('Content-Disposition', 'attachment', filename=i)
            msg.attach(msg_img)

    # 建立连接
    # 支持SSL加密和不加密
    if security.capitalize() == 'None' or len(security) == 0:
        smtp = smtplib.SMTP(smtp_server, smtp_port)
    else:
        smtp = smtplib.SMTP_SSL(smtp_server, smtp_port)
    try:
        smtp.helo(smtp_server)
        smtp.ehlo(smtp_server)
        smtp.login(user, password)

        # Log().info("开始发送邮件...")
        # 发送邮件
        smtp.sendmail(from_address, email_receives, msg.as_string())
        smtp.quit()
        print('发送邮件成功')
    except BaseException as e:
        print(e)
        # Log().error("邮件发送失败：{}".format(e))
    # else:
    #     Log().info("邮件发送成功!")


# if __name__ == '__main__':
#     p = os.path.join(Paths.report_path, os.listdir(Paths.report_path)[-2])
#     print(p)
#     send_email(p)
