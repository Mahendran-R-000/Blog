from django.http import HttpResponseRedirect
from rest_framework import viewsets, status

from .serializers import PostsSerializer
from .models import Posts
import requests
from django.shortcuts import render, redirect


class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all().order_by('title')
    serializer_class = PostsSerializer

    def create(self, request, *args, **kwargs):
        response = super(PostViewSet, self).create(request, *args, **kwargs)
        return HttpResponseRedirect(redirect_to='/')



def home(request):
    response = requests.get('http://127.0.0.1:8000/blog/posts/')
    data = response.json()
    #return render(request, 'post.html', {'data': data})
    return render(request, 'home.html', {'data': data})
