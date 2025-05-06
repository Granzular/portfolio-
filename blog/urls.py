from .views import views
from .views import ajax_views
from django.urls import path ,include

app_name = "blog"

urlpatterns =[
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('posts/<pk>/detail/',views.detail,name='detail'),

        path('ajaxIndex/',ajax_views.ajaxIndex,name="ajaxIndex"),
    
    ]
