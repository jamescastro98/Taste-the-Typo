from django.views import generic
from .forms import WebForm
from django.shortcuts import render
from django.conf import settings
from .masternode import setupConnections,gatherTypoSquatSites
from .workernode import start_worker
import signal

import time
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
    print("data/"+htmlname+".html")
    f=open("./data/"+htmlname + ".html")
    for lines in f:
        htmlstr+=lines
    f.close()
    return render(request,"htmlpg.html",{'htmlstr':htmlstr})

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
            gatherTypoSquatSites(Input)    # not too sure what the arg is
            #
            # workernode setup -Nathan
            
            #start_worker()
            #
            #   note: this should only start one worker, 
            #       not sure if we only want X amount of workers or scale it to
            #       number of typos we generated (i.e. 1 worker every 10 typos)
            #   note2: also commented out the code just in case I break everything
            #

            #time.sleep(5)
            return render(request, "result.html", {'input':Input, 'MEDIA_URL':settings.MEDIA_URL})
