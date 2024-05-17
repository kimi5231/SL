import requests
import json

# 네이버 쇼핑 API의 클라이언트 ID와 시크릿 키를 입력하세요.
client_id = "csTIB8xC7vxuS7mSJnk0"
client_secret = "Fs8sGNuCma"

url = "https://openapi.naver.com/v1/search/shop.json?query=신라면&display=20&sort=asc"
headers = {
    "X-Naver-Client-Id": client_id,
    "X-Naver-Client-Secret": client_secret
}

response = requests.get(url, headers=headers)
rescode = response.status_code

if(rescode == 200):
    response_body = response.json()
    items = response_body['items']
    for item in items:
        print(f"제품명: {item['title']}, 최저가: {item['lprice']}원")
else:
    print("Error Code:", rescode)
