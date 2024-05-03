import smtplib
import imapclient
import email
from email.message import EmailMessage
from email.policy import default
import mimetypes
import csv
import mypass


def read_mail():
    imap_server = imapclient.IMAPClient('imap.gmail.com', ssl=True)
    imap_server.login(myid, mypasswd)

    imap_server.select_folder('INBOX')
    mail_id_list = imap_server.gmail_search('subject:(주소록)')

    for id, raw_message in imap_server.fetch(mail_id_list, 'RFC822').items():
        email_message = email.message_from_bytes(raw_message[b'RFC822'], policy=default)
        for part in email_message.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get_content_maintype() != 'text':
                fname = part.get_filename()
                if fname:
                    print(f'{fname}을 저장합니다.....')
                    with open(fname, 'wb') as fp:
                        fp.write(part.get_payload(decode=True))
                    read_address_book(fname)


def read_address_book(fname):
    f = open(fname)
    reader = csv.reader(f, skipinitialspace=True)
    for line in reader:
        send_mail(line)
    f.close()


def send_mail(info):
    mail_server = smtplib.SMTP('smtp.gmail.com', 587)
    mail_server.ehlo()
    mail_server.starttls()
    mail_server.login(myid, mypasswd)

    msg = EmailMessage()
    msg['Subject'] = '안녕하세요. 반갑습니다.'
    msg['From'] = 'sooyoungsl5231@gmail.com'
    msg['To'] = info[1]
    msg.set_content(f'''안녕하세요. {info[0]}님. 반갑습니다.
저는 임수영이라고 합니다.
잘 부탁드립니다.''')
    fname = 'cat.jpg'
    ctype, _ = mimetypes.guess_type(fname)
    if not ctype:
        ctype = 'application/octect-stream'
    maintype, subtype = ctype.split('/')
    with open(fname, 'rb') as f:
        msg.add_attachment(f.read(), maintype=maintype, subtype=subtype, filename=fname)
    mail_server.send_message(msg)


myid = mypass.id
mypasswd = mypass.passwd

read_mail()