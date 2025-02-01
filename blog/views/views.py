from django.shortcuts import render,get_object_or_404,get_list_or_404,redirect
from ..models import Post,Tool,About,Contact
from django.utils import timezone
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView , ListView
from  ..forms import NameForm
from django.urls import reverse

# Create your views here.

def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("-published_date")[:3]
    context ={
        "posts":posts
        }
    return render(request,"blog/index.html",context)

class IndexView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/index.html"

class About(DetailView):
    template_name = "blog/about.html"
    model = About
    context_object_name = "About"


def blogIndex(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("-published_date")
    context = {"posts":
               posts
               }
    return render(request,"blog/blog.html",context)



def contact(request):
    contact = get_object_or_404(Contact,pk=1);
    context ={
            "contact":contact
            }
    return render(request,"blog/contact.html",context)

def detail(request,pk):
    post = get_object_or_404(Post,pk=pk,published_date__lte=timezone.now())
    context = {
        "post":post
}
    return render(request,"blog/detail.html",context)


def tools(request):
    tools = Tool.objects.all()
    context = {
            'tools':tools
            }
    return render(request,"blog/tools.html",context)


class Inspect_tool(View):

    def get(self,request):
        form = NameForm()
        context = {
                'form':form
                }
        return render(request,"blog/inspect_tool.html",context)

