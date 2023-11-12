from django.urls import path
from .views import get_all_posts, add_new_post, delete_post, update_post
app_name = "posts"

urlpatterns = [
    path("", get_all_posts, name='posts'),
    path("add-post", add_new_post, name="new-post"),
    path("delete/<int:post_id>", delete_post, name="delete-post"),
    path("update/<int:post_id>", update_post, name="update-post"),
]
