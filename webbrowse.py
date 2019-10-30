import sys
import asyncio
from pyppeteer import launch

# if len(sys.argv) > 1 :
#     URL = sys.argv[1]

async def browse():
    browser = await launch()
    page = await browser.newPage()
    print(URL)
    try:
        await page.goto(URL) #change this to website passed in.
        await page.screenshot({'path': URL+'.png','fullPage' : True})
        str= await page.content()
    except:
        str="Error Occurred - Either the website does not exist, or this device is not connected to wifi"
        print(str)
    await browser.close()
    f = open("browserdump.html", "w") #need to make an array of files to dump them at.
    f.write(str)
    print("Contents written in browserdump (Error String stored in HTML doc if !exist)")
    f.close()
    return

def browse_helper(URLarg:str):
    print('ping')
    URL = URLarg
    browse()
    asyncio.get_event_loop().run_until_complete(browse())
    return
