from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import View
from posts.models import Post

@login_required
def ProfileFeed(request):
    user = request.user
    posts = Post.objects.filter(post_creater= user)
    return render(request, 'profile_feed.html',{"posts":posts})