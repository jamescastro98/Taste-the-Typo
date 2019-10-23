import sys
import asyncio
from pyppeteer import launch

#if it don't work, check your wifi

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto(sys.argv[1]) #change this to website passed in.
    await page.screenshot({'path': 'example.png','fullPage' : True})
    str= await page.content()
    await browser.close()
    f = open("browserdump.html", "w") #need to make an array of files to dump them at.
    f.write(str)
    print("Contents written in browserdump")
    f.close()

asyncio.get_event_loop().run_until_complete(main())
