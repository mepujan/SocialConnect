from django.shortcuts import render, redirect
from comment.form import CommentForm
from posts.forms import PostForm
from posts.models import Post
from user.models import Profile
from django.contrib.auth.decorators import login_required


@login_required(login_url="/profile/login")
def homepage(request):
    profile_ = Profile.objects.get(user=request.user)
    c_form = CommentForm()
    post_form = PostForm()
    posts = Post.objects.all()
    return render(request, "homepage.html", {'posts': posts, 'c_form': c_form, 'profile': profile_, 'post_form': post_form})
