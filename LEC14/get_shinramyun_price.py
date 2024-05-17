import bs4
import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import time


word = '신라면'
url = f'https://search.shopping.naver.com/search/all?origQuery={word}&pagingIndex=1&pagingSize=40&productSet=total&query={word}&sort=price_asc&timestamp=&viewType=list'

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

p = sync_playwright().start()
browser = p.chromium.launch(headless=False).new_context(
    user_agent=headers['User-Agent'], viewport={'width': 800, 'height': 600}
)

page = browser.new_page()
page.goto(url)

src_size = 0

while src_size < len(page.content()):
    src_size = len(page.content())
    page.keyboard.press('End')
    time.sleep(1)

# r = requests.get(url, headers=headers)
# r.raise_for_status()

# with open('downloaded.html', 'w', encoding='utf-8') as wf:
#     wf.write(r.text)

# 제품명
# <a target="_blank" rel="noopener" class="product_link__TrAac linkAnchor" title="W쇼핑 농심 신라면블랙 134g x 4봉지 - W쇼핑" data-nclick="N=a:lst*N.title,i:44647479314,r:1" data-i="44647479314" data-ms="221844" href="https://cr.shopping.naver.com/adcr.nhn?x=kh%2F1uJfnMZQK1hjjSM597v%2F%2F%2Fw%3D%3Dsn2XT3u68stwaK9wBE6cYCD2Wpe5Ki%2FIu%2BECGhzc9BgWwBi3LAWoXSDALXUpoZu8tpV9vK1Jkn%2BhLTgbSgCIzAhhLtZ1li0RetNmLbMm4vKdplltqjQZv4Nbxb%2F450%2F2sLU9XQJqChCsCvArKvdKVmsbzrLp7%2BcS%2B9xBsD75NaA4BuA2GWOo3PoRrNqKzdrOIbnGUYRpLB2AEi%2BbTn01Olrei9zbsSi72I0GaF%2FoM9uqkXE7AAo7T60fi6L3odR4pZgdVyFjzrWcQU8H6%2Bi%2FGrzlgFVMIfg74kWEEX87WHNCk6v2w9jBqMGR4TTsgYaQnlII%2ByYYqWVu3SSXxcjEJdGjhuD%2BwiOjHnM4m%2FOdbf1aS1mH6fGkCj7iMgf522y1%2FYR7GVulXZ12CjJNDBknXmsUdJv0KR7s0OmdwJjOyXVEFmovGsAtuhqbrSHxFw6fYDYeOW9fAN4p1Tst912%2FwIsGOuUnATf8o1Xp%2Fn0wMjtQrDeR%2B3e8JY50ML8VvQVBkN05NYbxbGkE15LE2%2BDdPZ5sdZ4GwNZKnOM7%2BYXgaHFlsGT8KPw3C4wdpIoXRrzDTKYTOF5KsHq%2BigGAc1pAeZ2gvblAfl7S7Sen551nwpDyvGxAsBwpkGqtkHZzFLiNtb1NmOoRBMBsXNQGXzjfbC%2BFUQB%2FrDAzm2q1KHRsHkfE%3D&amp;nvMid=44647479314&amp;catId=50013941">W쇼핑 농심 신라면블랙 134g x 4봉지 - W쇼핑</a>
# selector = '[class^="product_link"][title]'
# soup = bs4.BeautifulSoup(r.text, 'html.parser')
# elms = soup.select(selector)
# for e in elms:
#     print(e['title'])

# 가격
# <span class="price"><span class="price_num__S2p_v"><em>10,000</em>원</span></span>
# elms = soup.select('.price')
# for e in elms:
#     print(e.get_text())

selector = '[class^="product_item"]'

soup = bs4.BeautifulSoup(page.content(), 'html.parser')

elms = soup.select(selector)
for e in elms:
    title = e.select_one('[class^="product_link"][title]')['title']
    price = e.select_one('.price').text
    print(f'{title} : {price}')

browser.close()
p.stop()