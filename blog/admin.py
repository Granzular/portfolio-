from django.contrib import admin
from .models import Post,About, Contact,Project,ClientMessage,Resume
# Register your models here.

admin.site.register(Post)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Project)
admin.site.register(ClientMessage)
admin.site.register(Resume)
