from django.shortcuts import render, redirect
from comment.form import CommentForm
from posts.models import Post
from user.models import Profile


def homepage(request):
    profile_ = Profile.objects.get(user=request.user)
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
    return render(request, "homepage.html", {'posts': posts, 'comment_form': form, 'profile': profile_})
