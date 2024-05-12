import requests
import json

telegram_url = 'https://api.telegram.org/bot7146135932:AAHprFIXBUgT1s0GaVJQoMG70zP3DI3E4hU'

r = requests.get(f'{telegram_url}/getMe')
if r.ok:
    assert r.headers['content-type'] == 'application/json'
    print(json.dumps(r.json(), indent=2, ensure_ascii=False))