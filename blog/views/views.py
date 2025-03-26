from django.shortcuts import render,get_object_or_404,get_list_or_404,redirect
from ..models import Post,Tool,About,Contact,Question,Option, UserScore, Quiz
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


class adderTest(View):

    def get(self,request):
            
        return render(request,"blog/adderTest/home.html")

    def post(self,request):
        quiz = Quiz.objects.get(id=1)
        try:
            username = request.POST["username"].strip().upper()
            password = request.POST["password"]
            user = User()
            user.username = username
            user.set_password(password)
            user.save()
            login(request,user)
        except IntegrityError:
            user = User.objects.get(username= request.POST["username"].strip().upper())
            #Important note, usernames are stored in upper case
            if len(quiz.users_who_attempted.filter(username=user.username))!=0:
                context = {"attempted":True}
                return render(request,"blog/adderTest/home.html",context)
            else:
                login(request,user)
            
        return redirect(reverse("blog:quiz"))

class QuizView(View):

    @method_decorator(login_required(login_url=reverse_lazy("blog:adderTest")))
    def get(self,request):

        user = request.user
        quiz = Quiz.objects.get(id=1)
        try:
            quiz.users_who_attempted.get(id = user.id)
            context = {"Attempted":True}
        except :
            questions = quiz.questions.all()
            options = Option.objects.all()
            context = {
                    "questions":
                    questions,
                    "options":
                    options
                    }

        return render(request,"blog/adderTest/test.html",context)

    def post(self,request):
        user_answer_dict = json.loads(request.body)
        quiz = Quiz.objects.get(id=1)
        questions = quiz.questions.all()
        #refactor the above line of code to get queryset using a proper filter 
        
        user = request.user
        score = 0
        for i in user_answer_dict:
            if questions.get(id=int(i)).answer.id == int(user_answer_dict[i]):
                score += 1

        user_score = UserScore()
        quiz.users_who_attempted.add(user) 
        user_score.user = user
        user_score.score = score
        quiz.save()
        user_score.save()
        logout(request)
        data = {"message":"success","username":user.username,"score":score}
        context = {"quizsuccess":"Thank you for attempting the test! "}
        request.session["context"] = context
        return JsonResponse(data)

