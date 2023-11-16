from django.shortcuts import render
from django.db.models import Q
from comment.form import CommentForm
from posts.forms import PostForm
from posts.models import Post
from user.models import Profile, Relationship
from django.contrib.auth.decorators import login_required


@login_required
def homepage(request):
    profile_ = Profile.objects.get(user=request.user)
    c_form = CommentForm()
    post_form = PostForm()
    posts = Post.objects.all()
    request_available = Relationship.objects.filter(
        Q(receiver=profile_) & Q(status="send"))
    return render(request, "homepage.html", {'posts': posts, 'c_form': c_form, 'profile': profile_, 'post_form': post_form, 'request_count': len(request_available)})
