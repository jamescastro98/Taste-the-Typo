from django.views import generic
from .forms import WebForm
from django.shortcuts import render
from django.conf import settings
from .masternode import setupConnections,gatherTypoSquatSites
from .workernode import start_worker
import signal
import time
import os
import re
import threading
#from models import Post

#change!
def HomeView(request):
    if request.method == 'GET':
        form = WebForm()
    return render(request, "home.html", {'form':form})
#    model = Post
#    context_object_name = "post"

def HTMLView(request):
    htmlname=request.GET.get('htmlname')
    htmlstr=""
    title=""
    num=htmlname.index('/')
    num+=1
    title=htmlname[(num+1):].replace("_",".")

    pngstr="/data/"+htmlname+".png"
    f=open("./data/"+htmlname + ".html")
    for lines in f:
        htmlstr+=lines
    f.close()
    return render(request,"htmlpg.html",{'htmlstr':htmlstr,'pngstr':pngstr,'title':title})

init = True
def ResultView(request):
    global init
    if request.method =='POST':
        form = WebForm(request.POST)
        if form.is_valid():
            print("Request Gotten!")
            Input = form.data["weburl"]
            if (Input.startswith("https://")):
                Input = Input[len("https://"):]
            if (Input.startswith("http://")):
                Input = Input[len("http://"):]
            # Execute Master + Worker Nodes Here
            # masternode setup -Nathan
            # signal.signal(signal.SIGINT, shutdown)
            if init:
                setupConnections()
                init = False
            if not os.path.isdir("./data/{}".format(Input)):
                typoThread = threading.Thread(target = gatherTypoSquatSites, args = (Input,))
                typoThread.setDaemon(True)
                typoThread.start()
            #time.sleep(5)
            return render(request, "result.html", {'input':Input, 'MEDIA_URL':settings.MEDIA_URL})
