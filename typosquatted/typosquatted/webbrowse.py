import sys
import asyncio
import re
from pyppeteer import launch

def fetchURL(URL:str):
    if("https://" in URL):
        name = '_'+URL.replace('.','_').replace('https://','')
    elif("http://" in URL):
        name = '_'+URL.replace('.','_').replace('http://','')
    name = URL

    async def browse():
        browser = await launch()
        page = await browser.newPage()
        try:
            await page.setViewport({'width': 1366,'height': 768})
            await page.goto(URL) #change this to website passed in.
            await page.screenshot({'path':name+'.png','fullPage' : False})
            st= await page.content()
            f = open(name +".html", "w") #need to make an array of files to dump them at.
            f.write(st)
            print("Success!")
            f.close()
            
            return name
        except:
            #st="Error Occurred - Either the website does not exist, or this device is not connected to wifi"
            name="404"
            return name
        await browser.close()
        
    name=asyncio.get_event_loop().run_until_complete(browse())
    return name

if len(sys.argv) > 1 :
    URL=sys.argv[1]
    fetchURL(URL)
