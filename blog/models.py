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

class Tool(models.Model):
    name = models.CharField(max_length=80)
    url = models.URLField()

    def __str__(self):
        return self.name

class About(models.Model):
    text = models.TextField()


class Contact(models.Model):
    info = models.TextField() 
    socials = models.TextField()
    additional_info = models.TextField()

class Question(models.Model):
    text = models.TextField()
    answer = models.OneToOneField("Option",on_delete=models.CASCADE,related_name="correct_answer",null=True)
    def __str__(self):
        return self.text[:20]

class Option(models.Model):
    text = models.CharField(max_length=200)
    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name="options",null=True)

    def __str__(self):
        return self.text

class UserScore(models.Model):
    score = models.IntegerField()
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Quiz(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    questions = models.ManyToManyField(Question)
    users_who_attempted = models.ManyToManyField(User,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Quizes"

