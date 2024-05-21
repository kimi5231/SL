from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup


url = 'https://eclass.tukorea.ac.kr/ilos/main/member/login_form.acl'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'

p = sync_playwright().start()
browser = p.chromium.launch(headless=False).new_context(
    user_agent=user_agent,
    viewport={'width':1024, 'height':800}
)
page = browser.new_page()
page.goto(url)

page.locator('#usr_id').fill('2022184031')
page.fill('#usr_pwd', '4067212')
page.click('#login_btn')

# 스크립트 언어 선택
page.click('#contentsIndex > div.index-leftarea02 > div:nth-child(2) > ol > li:nth-child(8) > em')

# 강의자료 항목 클릭
page.click('#menu_lecture_material')

soup = BeautifulSoup(page.content(), 'html_parser')

# 모든 게시물 요소 리스트 확보
elms = page.locator('a.site-link').all()
for e in elms:
    print(e.text_content())