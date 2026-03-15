from playwright.sync_api import sync_playwright
import re

URL = "https://www.alphacyprus.com.cy/live"

with sync_playwright() as p:
    browser = p.firefox.launch(headless=True)
    page = browser.new_page()

    page.goto(URL, wait_until="networkidle")

    html = page.content()

    browser.close()

match = re.search(r'https://l4\.cloudskep\.com/alphacyp/acy/playlist\.m3u8\?wmsAuthSign=[^\'"]+', html)

if match:
    stream = match.group(0)

    playlist = "#EXTM3U\n#EXTINF:-1,Alpha Cyprus\n" + stream

    with open("alpha.m3u8", "w") as f:
        f.write(playlist)

    print("Nieuwe stream:", stream)
else:
    print("Stream niet gevonden")
