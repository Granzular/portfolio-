from .views import views
from .views import ajax_views
from django.urls import path ,include
from django.contrib.auth.decorators import login_required

app_name = "blog"

urlpatterns =[
    path('',views.index,name='index'),
    path('about/<int:pk>',views.About.as_view(),name='about'),
    path('contact/',views.contact,name='contact'),
    path('posts/<pk>/detail/',views.detail,name='detail'),
    path('tools/',views.tools,name='tools'),
    path('tools/inspect_tool/',views.Inspect_tool.as_view(),name="inspect_tool"),
    path('index/',views.IndexView.as_view(),name="IndexView"),

    path('blog/',views.blogIndex,name="blog"),
    path('ajaxIndex/',ajax_views.ajaxIndex,name="ajaxIndex"),
    ]
