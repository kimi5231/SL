import imapclient
import email
from email.policy import default
import csv


imap_server = imapclient.IMAPClient('imap.gmail.com', ssl=True)

id = 'daehyun.lee.python.test@gmail.com'
passwd = 'lhko qyfb zpou wava'

imap_server.login(id, passwd)
imap_server.select_folder('INBOX')
msg_id_list = imap_server.gmail_search('subject:(등록) after:2024/5/2 before:2024/5/5')
address_list = []

for id, raw_msg in imap_server.fetch(msg_id_list, 'RFC822').items():
    email_msg = email.message_from_bytes(raw_msg[b'RFC822'], policy=default)
    date = email_msg['Date']
    sender_info = email_msg['From']
    sender_address = f'{sender_info.addresses[0].username}@{sender_info.addresses[0].domain}'
    name = email_msg['Subject'].split()[0]
    print(f'{name=}{sender_address=}')
    address_list.append([name, sender_address])

with open('address.csv', 'w', newline='') as wf:
    writer = csv.writer(wf)
    for address in address_list:
        writer.writerow(address)

