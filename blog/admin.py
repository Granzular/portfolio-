from django.contrib import admin
from .models import Post,About, Contact,Project,ClientMessage
# Register your models here.

admin.site.register(Post)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Project)
admin.site.register(ClientMessage)
