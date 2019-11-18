from django.views import generic
#from models import Post

#change!
class HomeView(generic.TemplateView):
    template_name = 'home.html'
#    model = Post
#    context_object_name = "post"