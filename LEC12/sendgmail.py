import smtplib
import email
from email.message import EmailMessage
import mypass
import mimetypes

id = mypass.id
passwd = mypass.passwd

mail_server = smtplib.SMTP('smtp.gmail.com', 587)
mail_server.ehlo()
mail_server.starttls()
mail_server.login(id, passwd)

msg = EmailMessage()
msg['Subject'] = 'pdf 첨부 전송'
msg['From'] = '임수영<sooyoungsl5231@gmail.com>'
msg['To'] = 'sooyoungsl5231@gmail.com'
msg.set_content('첨부')
fname = 'LEC12 - Email.pdf'
ctype, _ = mimetypes.guess_type(fname)
if not ctype:
    ctype = 'application/octect-stream' # 잘 모를 때 디폴트.
maintype, subtype = ctype.split('/')
with open(fname, 'rb') as f:
    msg.add_attachment(f.read(), maintype=maintype, subtype=subtype, filename=fname)
mail_server.send_message(msg)