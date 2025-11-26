from django.shortcuts import render,get_object_or_404,get_list_or_404,redirect
from ..models import Post,About,Contact,Project,ClientMessage,Resume
from django.utils import timezone
from django.views import View
from django.views.generic import DetailView , ListView
from  ..forms import MessageForm
from django.urls import reverse,reverse_lazy
from django.http import JsonResponse,FileResponse
import json
from django.contrib.auth.models import User
from django.db import IntegrityError
from ..utils import auto_mail_reply
from django.views.decorators.cache import never_cache



def index(request):
    about = About.objects.all()
    about = None if len(about)==0 else about[0]
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("-published_date")[:3]

    context = {
            "about" : about,
            "posts" : posts,
            }

    return render(request,"blog/index.html",context)


def about(request):
    about = About.objects.all()
    about = None if len(about)==0 else about[0]
    context = {"about":about}
    return render(request,"blog/about.html",context)

@never_cache
def contact(request):

    if request.method == "POST":

        email = request.POST.get('email')
        message = request.POST.get('message')
        ClientMessage.objects.create(email = email, message = message)
        auto_mail_reply(email)

        return JsonResponse({'msg':'success'})
    contact = Contact.objects.all()
    contact = None if len(contact)==0 else contact[0]
    msgform = MessageForm()
    context ={
            "contact":contact,
            "message_form":msgform,
            }
    return render(request,"blog/contact.html",context)

def blog_index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("-published_date")[:3]

    context = {
            "posts" : posts,
            }
    return render(request,"blog/blog_index.html",context)

def blog_detail(request,pk):
    post = get_object_or_404(Post,pk=pk,published_date__lte=timezone.now())
    context = {
            "post":post,
            }
    return render(request,"blog/detail.html",context)

class ProjectListView(ListView):
    model = Project
    template_name = 'blog/projects.html'
    context_object_name = 'projects'

class ProjectDetail(DetailView):
    model = Project
    template_name = 'blog/project_detail.html'
    context_object_name = 'project'

def resumepdf(request):
    file = get_object_or_404(Resume,pk=1).file

    return FileResponse(file,filename='michael_ayeni_resume.pdf')


    






