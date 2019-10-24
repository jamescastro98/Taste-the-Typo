import sys
import asyncio
from pyppeteer import launch
async def main():
    browser = await launch()
    page = await browser.newPage()
    try:
        await page.goto(sys.argv[1]) #change this to website passed in.
        await page.screenshot({'path': 'example.png','fullPage' : True})
        str= await page.content()
    except:
        str="Error Occurred - Either the website does not exist, or this device is not connected to wifi"
        print(str)
    await browser.close()
    f = open("browserdump.html", "w") #need to make an array of files to dump them at.
    f.write(str)
    print("Contents written in browserdump (Error String stored in HTML doc if !exist)")
    f.close()
asyncio.get_event_loop().run_until_complete(main())
