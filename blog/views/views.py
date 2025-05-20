from django.shortcuts import render,get_object_or_404,get_list_or_404,redirect
from ..models import Post,About,Contact,Project
from django.utils import timezone
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.views.generic import DetailView , ListView
from  ..forms import NameForm
from django.urls import reverse,reverse_lazy
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from django.db import IntegrityError

# Create your views here.

def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("-published_date")[:3]
    context ={
        "posts":posts
        }
    return render(request,"blog/index.html",context)


def about(request):
    about = About.objects.all()
    about = None if len(about)==0 else about[0]
    context = {"about":about}
    return render(request,"blog/about.html",context)


def contact(request):
    contact = Contact.objects.all()
    contact = None if len(contact)==0 else contact[0]
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

class PortfolioListView(ListView):
    model = Project
    template_name = 'blog/portfolio.html'
    context_object_name = 'projects'

class PortfolioDetail(DetailView):
    model = Project
    template_name = 'blog/portfolioDetail.html'
    context_object_name = 'project'
    






