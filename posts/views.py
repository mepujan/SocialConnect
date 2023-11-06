from django.shortcuts import render
from .models import Post


def get_all_posts(request):
    posts = Post.objects.all()
    return render(request, "post.html", {'posts': posts})
