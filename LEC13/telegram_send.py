import requests
import json


telegram_url = 'https://api.telegram.org/bot7146135932:AAHprFIXBUgT1s0GaVJQoMG70zP3DI3E4hU'


def send_message(chat_id, text):
    r = requests.get(f'{telegram_url}/sendMessage', params={'chat_id': chat_id, 'text': text})
    if r.ok:
        print(json.dumps(r.json()['result'], indent=2, ensure_ascii=False))
    else:
        print(f'FAIL:{r.json()}')


def send_photo(chat_id, link):
    r = requests.get(f'{telegram_url}/sendPhoto',
                     params={'chat_id': chat_id,
                             'caption': '링크입니다.',
                             'photo':link})
    if r.ok:
        print(json.dumps(r.json()['result'], indent=2, ensure_ascii=False))
    else:
        print(f'FAIL:{r.json()}')


def send_file(chat_id, fname):
    url = f'{telegram_url}/sendDocument'
    params = {'chat_id': chat_id, 'caption': fname}
    with open(fname, 'rb') as f:
        files = {'document': f}
        r = requests.get(url, params=params, files=files)
        if r.ok:
            print(json.dumps(r.json()['result'], indent=2, ensure_ascii=False))
        else:
            print(f'FAIL:{r.json()}')

link = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6oHy7mq_ki15YwLeGN_Mq9MUYxVbal7tiWg&usqp=CAU'

#send_message(-4246362640, '안녕하세요. 저는 임수영 봇입니다.')
send_photo(-4246362640, link)
send_file(-4246362640, 'cat1.jpg')