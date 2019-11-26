from django.views import generic
from .forms import WebForm
from django.shortcuts import render

from masternode import setupConnections, gatherTypoSquatSites, shutdown
from workernode import start_worker

import time
#from models import Post

#change!
def HomeView(request):
    if request.method == 'GET':
        form = WebForm()
    return render(request, "home.html", {'form':form})
#    model = Post
#    context_object_name = "post"

def ResultView(request):
    if request.method =='POST':
        form = WebForm(request.POST)
        if form.is_valid():
            print("Request Gotten!")
            #Execute Master + Worker Nodes Here
            # masternode setup -Nathan
                # signal.signal(signal.SIGINT, shutdown)
                # setupConnections()
                # gatherTypoSquatSites()    # not too sure what the arg is
            #
            # workernode setup -Nathan
                # start_worker()
            #
            #   note: this should only start one worker, 
            #       not sure if we only want X amount of workers or scale it to
            #       number of typos we generated (i.e. 1 worker every 10 typos)
            #   note2: also commented out the code just in case I break everything
            #

            time.sleep(5)
            input = form.data["weburl"]
            return render(request, "result.html", {'input':input})