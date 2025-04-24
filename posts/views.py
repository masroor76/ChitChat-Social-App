from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import Post
from .forms import PostsForm


class LikePost(View):
    def get( self, request, pk): 
        post = get_object_or_404(Post, pk=pk)
        user = request.user
        post.likes.add(user)
        print(pk, " Likes By ", user)
        return redirect("/")

class UnLikePost(View):
    def get( self, request, pk): 
        post = get_object_or_404(Post, pk=pk)
        user = request.user
        post.likes.remove(user)
        print(pk, " Likes By ", user)
        return redirect("/")


class CreatePost(View):
    @method_decorator(login_required)    
    def get(self,request):
        form = PostsForm()
        return render(request, "posts/create_post.html", {"form":form})
    
    @method_decorator(login_required)    
    def post(self,request):
        postForm = PostsForm(request.POST, request.FILES)
        if postForm.is_valid():    
            cleanedInfo = postForm.cleaned_data
            user=request.user
            print(cleanedInfo['image'])
            post = Post(post_creater= user,title=cleanedInfo['title'],slug=cleanedInfo['slug'], image =cleanedInfo['image'],  post_text=cleanedInfo['post_text'])
            post.save()

            return redirect("/", Warning("jJJj"))
        else:
            return HttpResponse("Post Creation Failed")