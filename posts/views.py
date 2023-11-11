from django.shortcuts import render, redirect
from .models import Post
from comment.form import CommentForm
from .forms import PostForm
from user.models import Profile


def get_all_posts(request):
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        post = Post.objects.get(id=request.POST.get('post'))
        if form.is_valid():
            instance = form.save(commit=False)
            # print("clean-data = ", form)
            instance.user = request.user
            instance.post = post
            instance.save()
            return redirect("/posts")
    posts = Post.objects.all()
    return render(request, "post.html", {'posts': posts, 'comment_form': form})


def add_new_post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            profile = Profile.objects.get(user=request.user)
            instance.author = profile
            instance.save()
            return redirect("/")
    return render(request, 'homepage.html', {"form": form})
