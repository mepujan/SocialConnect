from django.shortcuts import render, redirect
from .models import Post
from comment.form import CommentForm
from .forms import PostForm
from user.models import Profile, Relationship
from django.contrib.auth.decorators import login_required
from django.db.models import Q


@login_required(login_url='/profile/login')
def add_new_post(request):
    form = PostForm()
    profile_ = Profile.objects.get(user=request.user)
    request_available = Relationship.objects.filter(
        Q(receiver=profile_) & Q(status="send"))
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            profile = Profile.objects.get(user=request.user)
            instance.author = profile
            instance.save()
            return redirect("/")
    return render(request, 'homepage.html', {"form": form, 'profile': profile_, 'request_count': len(request_available)})


@login_required(login_url='/profile/login')
def add_comment(request):
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=post_id)
        if form.is_valid:
            instance = form.save(commit=False)
            instance.user = Profile.objects.get(user=request.user)
            instance.post = post
            instance.save()
            return redirect("/")


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
        "form": form,
        'profile': profile
    }
    return render(request, 'update-post.html', context)
