from django.shortcuts import render, redirect
from django.views import View
from posts.models import Post

class HomeView(View):
    def get(self,request):
        queryResult = Post.objects.prefetch_related()
        if queryResult.count() > 0:
            posts = queryResult 
            return render(request,'home.html',{"posts":posts})
        else:
            return render(request,'home.html')