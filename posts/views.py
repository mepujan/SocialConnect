from django.shortcuts import render, redirect
from .models import Post
from comment.form import CommentForm


def get_all_posts(request):
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.post = request.post
            instance.save()
            return redirect("/posts")
    posts = Post.objects.all()
    return render(request, "post.html", {'posts': posts, 'comment_form': form})
