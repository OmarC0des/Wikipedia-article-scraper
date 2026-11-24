# -- This script is made by --
# --      Omar Ashraf       --
# ----------------------------
from playwright.async_api import async_playwright
import asyncio
URL = 'https://en.wikipedia.org/wiki/Minecraft' # Replace with Wikipedia article URL
async def extract_w():
    async with async_playwright() as p:
        browser = await p.webkit.launch(headless=True)
        page = await browser.new_page()
        await page.goto(URL)
        article = await page.locator('section#mwAQ').inner_text()
        print(article)
        await browser.close()

asyncio.run(extract_w())
