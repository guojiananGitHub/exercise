from email.mime.text import MIMEText
import smtplib
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


# 输入email地址和口令
from_addr = input('From（QQ邮箱）:')
password = input('Password(授权码):')
# 输入收件人地址：
to_addr = input('To:')
# 输入SMTP服务器地址：
smtp_server = input('SMTP server:')

# 邮件正文
msg = MIMEMultipart()
# msg = MIMEText('真不知道说啥', 'plain', 'utf-8')  # 发送纯文本
# msg = MIMEText('<html><body><h1>Hello</h1>' +
#     '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
#     '</body></html>', 'html', 'utf-8')  # 发送html
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

# 邮件正文是MIMEText:
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片
with open('C:\\Users\\administrator\Desktop\\QQ20181112103228.png', 'rb') as f:
    mime = MIMEBase('image', 'png', filename='QQ20181112103228.png')
    mime.add_header('Content-Disposition', 'attachment', filename='QQ20181112103228.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()