from playwright.sync_api import sync_playwright
import time


url = 'https://lolchess.gg/builder/guide/8467f1b81ba0c9ab7e0bff6a996aa7feaa0c2d5d?type=guide'

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

p = sync_playwright().start()
browser = p.chromium.launch(headless=False).new_context(
    user_agent=headers['User-Agent'], viewport={'width':800, 'height':800}
)

page = browser.new_page()
page.goto(url)
time.sleep(1)

page.evaluate('window.scrollTo(0, 1300)')
#page.click('#content-container > div.BuilderLayout.css-10cwa7w.e15zni9b0 > div.flex-1 > div.css-17qq1xt.e15zni9b2 > div.css-olyd6o.e1g8be6w0 > div.css-10kp3ze.ewri1el0 > div > nav > div.TabNavItem.selected.css-1kf5ye3.e146eslx1')
time.sleep(1)