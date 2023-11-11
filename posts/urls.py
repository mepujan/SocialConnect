from django.urls import path
from .views import get_all_posts, add_new_post
app_name = "posts"

urlpatterns = [
    path("", get_all_posts, name='posts'),
    path("add-post", add_new_post, name="new-post")
]
