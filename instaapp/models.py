from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    friends = models.ManyToManyField('self', symmetrical=False)
def get_user_input_default():
    return input("Enter the default content for the 'content' field: ")

class Post(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content = models.CharField(default=get_user_input_default, max_length= 255)

    image = models.ImageField(upload_to='post_images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)




class ChatRoom(models.Model):
    sender = models.ForeignKey(UserProfile, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(UserProfile, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)



# Create your models here.
