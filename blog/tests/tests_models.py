import datetime

from django.test import TestCase
from ..models import Post
from django.contrib.auth.models import User
from django.utils import timezone

# Create your tests here.

def create_user():
    return User(username="Testuser",email="test@gmail.com",password="1234")

def create_post(title="Test",text="Testing",days=1,author=create_user()):
    pub_date = timezone.now()-datetime.timedelta(days=days)
    return Post(title=title,text=text,published_date=pub_date,author=author)


class PostModelTests(TestCase):

    def test_published_with_published_post(self):
        published_post = create_post(days=1)
        self.assertIs(published_post.published(),True)


        def test_published_with_unpublished_post(self):
            u = User(username="Testuser",email="test@gmail.com",password="1234")
            u.save()
            pub_date = timezone.now()+datetime.timedelta(days=1)
            unpublished_post = Post(title="Test",text="Testing",published_date=pub_date,author=u)
            self.assertIs(unpublished_post.published(),False)

            
