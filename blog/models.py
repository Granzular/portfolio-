from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


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


