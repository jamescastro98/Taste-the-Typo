import sys
import asyncio
import re
from pyppeteer import launch

def fetchURL(URL:str):
    name = '_'+URL.replace('.','_').replace('https://','') #Underscore to help all the .png to stay in one place for debugging
    filename = name + ".html"
    async def browse():
        found=False
        browser = await launch()
        page = await browser.newPage()
        # print(URL)    # debugging
         #Underscore to help all the .png to stay in one place for debugging
        name = '_'+URL.replace('.','_').replace('https://','')
        
        try:
            # print(imgName)    # debugging 
            await page.goto(URL) #change this to website passed in.
            await page.screenshot({'path':name+'.png','fullPage' : True})
            st= await page.content()
            f = open(name +".html", "w") #need to make an array of files to dump them at.
            f.write(st)
            print("Success!")
            found=True
            f.close()
            name = '_'+URL.replace('.','_').replace('https://','')
            return name
        except:
            #st="Error Occurred - Either the website does not exist, or this device is not connected to wifi"
            name="404"
            return name
        await browser.close()
  
    name=asyncio.get_event_loop().run_until_complete(browse())
    return name

def fetchRetURL(URL:str):
    name = '_'+URL.replace('.','_').replace('https://','') #Underscore to help all the .png to stay in one place for debugging
    filename = name + ".html"
    async def browse():
        browser = await launch()
        page = await browser.newPage()
        # print(URL)    # debugging
        # name = '_'+URL.replace('.','_').replace('https://','') #Underscore to help all the .png to stay in one place for debugging
        try:
            # print(imgName)    # debugging 
            await page.goto(URL) #change this to website passed in.
            await page.screenshot({'path':name+'.png','fullPage' : True})
            str= await page.content()
        except:
            str="Error Occurred - Either the website does not exist, or this device is not connected to wifi"
            print(str)
        await browser.close()
        f = open(name +".html", "w") #need to make an array of files to dump them at.
        f.write(str)
        print("Contents written in browserdump (Error String stored in HTML doc if !exist)")
        f.close()
    asyncio.get_event_loop().run_until_complete(browse())
    return filename

if len(sys.argv) > 1 :
    URL=sys.argv[1]
    # PATH=sys.argv[2]
    print(fetchURL(URL))
