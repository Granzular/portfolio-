#this module contains code for views involving AJAX
from django.http import JsonResponse
from ..models import Post
from django.urls import reverse
#none view code below
def helper(lst):
    dct = {}
    for i in lst:
        dct[i.id] = {"id":i.id,"title":i.title,"pub_date":i.published_date,"preview":i.preview(),"url":reverse("blog:detail",args=(i.id,))}
    return dct

def ajaxIndex(request):
    post = Post.objects.all()[:3] 
    data = helper(post)
    return JsonResponse(data)
        
