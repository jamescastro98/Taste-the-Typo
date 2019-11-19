from django.views import generic
from .forms import WebForm
from django.shortcuts import render
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
            time.sleep(5)
            input = form.data["weburl"]
            return render(request, "result.html", {'input':input})