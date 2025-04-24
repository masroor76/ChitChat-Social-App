from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    post_creater = models.ForeignKey(User,  on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="post_like", blank=True)
    slug = models.SlugField(max_length=200, blank=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post', blank=True)
    post_text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
