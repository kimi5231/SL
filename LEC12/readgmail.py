import smtplib
import imapclient
import email
from email.message import EmailMessage
from email.policy import default
import mypass


def print_message(msg):
    print("=" * 200)
    print(f"""\
    수신시각: {msg["Date"]}
    제목:{msg["Subject"]}
    보내는사람:{msg["From"]}
    받는사람:{msg["To"]}
    """)

    for part in msg.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get_content_maintype() == 'text':
            if part.get_content_subtype() == 'plain':
                body = str(part.get_payload(decode=True), part.get_content_charset())
                print(body)
        else:  # 첨부 파일 존재
            fname = part.get_filename()
            if fname:
                print(f'{fname}을 저장합니다.....')
                with open(fname, 'wb') as fp:
                    fp.write(part.get_payload(decode=True))


id = mypass.id
passwd = mypass.passwd

imap_server = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imap_server.login(id, passwd)

imap_server.select_folder('INBOX')
mail_id_list = imap_server.gmail_search('after:2024/4/29 before:2024/5/5')

for id, raw_message in imap_server.fetch(mail_id_list, 'RFC822').items():
    # email message 읽기 완성.
    email_message = email.message_from_bytes(raw_message[b'RFC822'], policy=default)
    print_message(email_message)