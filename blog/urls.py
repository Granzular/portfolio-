from .views import views
from .views import ajax_views
from django.urls import path ,include

app_name = "blog"

urlpatterns =[
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('blog/posts/',views.blog_index,name='blog_index'),
    path('posts/<pk>/detail/',views.blog_detail,name='detail'),
    path('projects/',views.ProjectListView.as_view(),name='projects'),
    path('projects/<pk>/detail/',views.ProjectDetail.as_view(),name='project-detail'),

        path('ajaxIndex/',ajax_views.ajaxIndex,name="ajaxIndex"),
        path('resume/pdf/',views.resumepdf,name='resumepdf'),
    
    ]
