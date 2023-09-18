from django.contrib import admin
from django.contrib import admin
from .models import UserProfile, Post, Comment, ChatRoom, Message

admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(ChatRoom)
admin.site.register(Message)


# Register your models here.
