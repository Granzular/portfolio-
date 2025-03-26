from django.contrib import admin
from .models import Post,Tool,About, Contact,Question,Option,Quiz,UserScore
# Register your models here.

admin.site.register(Post)
admin.site.register(Tool)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Quiz)
admin.site.register(UserScore)
