import bs4
import requests
from bs4 import BeautifulSoup


def print_result():
    platform = ['PC', 'PC방', '콘솔', '모바일']
    for i in range(0, 4):
        print(platform[i].center(60), end='')
    print()

    for i in range(0, 5):
        print(str(i + 1).ljust(10), end='')
        for j in range(0, 4):
            print(game_list[j][i].center(50), end='')
        print()

word = '게임+순위'
url = f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={word}'

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

r = requests.get(url, headers=headers)
r.raise_for_status()

soup = bs4.BeautifulSoup(r.text, 'html.parser')

links = []
link_selector = 'a[nocr][onclick][class^="area_text_box"]'
link_elms = soup.select(link_selector)
for l in link_elms:
    links.append(l['href'])

game_list = [[],[],[],[]]

for i in range(1, 5):
    link = f'https://search.naver.com/search.naver{links[i]}'
    r = requests.get(link, headers=headers)
    r.raise_for_status()
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    selector = 'strong.title > a[nocr][onclick]._text'
    elms = soup.select(selector)
    for e in elms:
        game_list[i-1].append(e.text)

print_result()