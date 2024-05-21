from playwright.sync_api import sync_playwright
import time


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

# 과제 항목 클릭
page.click('#menu_report')

# 모든 게시물 요소 리스트 확보
elms = page.locator('[class^="subjt_top"]').all()
for e in elms:
    print(e.text_content())
    e.click()
    time.sleep(1)

    text = page.locator('#content_text > table > tbody > tr:nth-child(8) > td p').all()
    for t in text:
        print(t.text_content())
    print(end='\n\n\n')

    page.click('#content_text > div.bbs-rbutton04 > div')
    time.sleep(1)