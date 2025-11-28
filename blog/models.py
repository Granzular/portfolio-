from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
import markdown

STATUS_CHOICES = (
        ('unread','unread'),
        ('in_progress','in_progress'),
        ('completed','completed'),
        )

class Post(models.Model):
    
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def preview(self):
        return self.text[:100]

    def published(self):
        if self.published_date<timezone.now():
            return True
        else:
            return False
    
    def parse_md(self):
        return markdown.markdown(self.text,extensions=['fenced_code', 'codehilite', 'toc', 'tables'])


    class Meta:
        ordering = ("-published_date",)

class About(models.Model):
    text = models.TextField()

    def __str__(self):
        return f"About -- {self.id}"

    def parse_md(self):
        return markdown.markdown(self.text,extensions=['fenced_code', 'codehilite', 'toc', 'tables'])



class Contact(models.Model):
    info = models.TextField() 
    
    def parse_md(self):
        return markdown.markdown(self.info,extensions=['fenced_code', 'codehilite', 'toc', 'tables'])


class Project(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='projects',blank=True)
    technologies_used = models.CharField(max_length=500)
    links = models.CharField(max_length=500,blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:project-detail',kwargs = {'pk':self.pk})

    def get_technologies_used_list(self):
        return self.technologies_used.split(',')

    def get_links_list(self):
        return self.links.split(',')

class ClientMessage(models.Model):
    email = models.EmailField()
    message = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES,default="unread",max_length=12)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.status} {self.timestamp.strftime("%d %h %Y--%H:%M:%S")}'

    class Meta:
        ordering = ("-timestamp",)


class Resume(models.Model):
    file = models.FileField(upload_to='documents')




    
