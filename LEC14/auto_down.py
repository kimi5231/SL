import asyncio
import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/search?q=eclass+tukorea&oq=eclass+tukorea&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDUzNTdqMGoyqAIAsAIB&sourceid=chrome&ie=UTF-8")
    page.get_by_role("cell", name="로그인 Copyright TECH UNIVERSITY").get_by_role("link").click()
    page.get_by_role("textbox", name="아이디").click()
    page.get_by_role("textbox", name="아이디").fill("2022184031")
    page.get_by_role("textbox", name="비밀번호").click()
    page.get_by_role("textbox", name="비밀번호").fill("4067212")
    page.get_by_title("로그인").click()
    page.get_by_text("스크립트언어 (04)").click()
    page.get_by_role("link", name="강의자료").click()   # 강의자료 페이지 클릭

    elms = page.locator('a.site-link').all()
    for i, e in enumerate(elms[:3]):  # 상위 3개만 처리
        print(f'{i}th click')
        e.click()   # 실제 게시물 안에 들어온다.
        time.sleep(1)

        for l in page.locator('a.site-link').all():   # 첨부 파일이 여러 개 있을 수 있다.
            with page.expect_download() as download_info:
                l.click()
            download = download_info.value
            download.save_as(download.suggested_filename)

        time.sleep(1)
        page.click('#myform > div.bbs-rbutton04 > div') # 현재 게시물을 나가서 목록 리스트로 간다.

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
