from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from smtplib import SMTP, SMTP_SSL, SMTPException

from config import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD, SMTP_USE_SSL


def send_email(receivers, title, content, content_type='text'):
    """
    发送邮件
    :param receivers: 收件人邮件列表
    :param title: 邮件主题
    :param content: 邮件内容
    :param content_type: 默认文本。可以是html
    :return:
    """
    smtp_cli = SMTP_SSL(SMTP_HOST, SMTP_PORT) if SMTP_USE_SSL else SMTP(SMTP_HOST, SMTP_PORT)

    smtp_cli.login(SMTP_USER, SMTP_PASSWORD)

    mail_content_type = 'html' if content_type == 'html' else 'plain'
    msg = MIMEText(content, mail_content_type, 'utf-8')
    msg["From"] = formataddr(["四叶草安全", SMTP_USER])
    msg["To"] = formataddr(['', ','.join(receivers)])
    msg['Subject'] = Header(title, 'utf-8')

    try:
        smtp_cli.sendmail(SMTP_USER, receivers, msg.as_string())
        smtp_cli.quit()
        # print("邮件发送成功")
        return True
    except SMTPException:
        # print("Error: 无法发送邮件")
        return False


if __name__ == '__main__':
    send_email(['12345678@qq.com', 'zhangxing@seclover.com'], '测试邮件', 'hello world!')
