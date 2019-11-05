import sys
import asyncio
import re
from pyppeteer import launch

# def test(URL:str,PATH:str):
#     async def browse():
#         browser = await launch()
#         page = await browser.newPage()
#         # print(URL)    # debugging
#         name = '_'+URL.replace('.','_').replace('https://','') #Underscore to help all the .png to stay in one place for debugging
        
#         try:
#             # print(imgName)    # debugging 
#             await page.goto(URL) #change this to website passed in.
#             await page.screenshot({'path':PATH+'/IMG/'+ name+'.png','fullPage' : True})
#             str= await page.content()
#         except:
#             str="Error Occurred - Either the website does not exist, or this device is not connected to wifi"
#             print(str)
#         await browser.close()
#         f = open(PATH+"/HTML/"+ name +".html", "w") #need to make an array of files to dump them at.
#         f.write(str)
#         print("Contents written in browserdump (Error String stored in HTML doc if !exist)")
#         f.close()
#     asyncio.get_event_loop().run_until_complete(browse())

# if len(sys.argv) > 1 :
#     URL=sys.argv[1]
#     PATH=sys.argv[2]
#     test(URL,PATH)
def fetchURL(URL:str):
    async def browse():
        browser = await launch()
        page = await browser.newPage()
        # print(URL)    # debugging
        name = '_'+URL.replace('.','_').replace('https://','') #Underscore to help all the .png to stay in one place for debugging
        
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

if len(sys.argv) > 1 :
    URL=sys.argv[1]
    # PATH=sys.argv[2]
    fetchURL(URL)