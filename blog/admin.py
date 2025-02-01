from django.contrib import admin
from .models import Post,Tool,About, Contact
# Register your models here.

admin.site.register(Post)
admin.site.register(Tool)
admin.site.register(About)
admin.site.register(Contact)
