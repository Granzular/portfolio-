from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

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


    class Meta:
        ordering = ("-published_date",)

class About(models.Model):
    text = models.TextField()


class Contact(models.Model):
    info = models.TextField() 
    socials = models.TextField()
    additional_info = models.TextField()


    def get_additional_info_list(self):
        return self.additional_info.split(',')

    def get_socials_list(self):
        return self.socials.split(',')

    def get_info_list(self):
        return self.info.split(',')


class Project(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='projects',blank=True)
    technologies_used = models.CharField(max_length=500)
    links = models.CharField(max_length=500,blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:portfolioDetail',kwargs = {'pk':self.pk})

    def get_technologies_used_list(self):
        return self.technologies_used.split(',')

    def get_links_list(self):
        return self.links.split(',')

class ClientMessage(models.Model):
    email = models.EmailField()
    message = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES,default="unread")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.status} {self.timestamp.strftime("%d %h %Y--%H:%M:%S")}'

    class Meta:
        ordering = ("-timestamp",)




    
