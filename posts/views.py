from django.shortcuts import render, redirect
from .models import Post
from comment.form import CommentForm
from .forms import PostForm
from user.models import Profile
from django.contrib.auth.decorators import login_required


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


@login_required(login_url='/profile/login')
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


@login_required(login_url='/profile/login')
def delete_post(request, post_id):
    Post.objects.get(id=post_id).delete()
    return redirect('/')


@login_required(login_url='/profile/login')
def update_post(request, post_id):
    post = Post.objects.get(id=post_id)
    form = PostForm(instance=post)
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = profile
            instance.save()
            return redirect("/")

    context = {
        "form": form
    }
    return render(request, 'update-post.html', context)
