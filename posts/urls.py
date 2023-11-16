from django.urls import path
from .views import add_new_post, delete_post, update_post, add_comment
app_name = "posts"

urlpatterns = [
    path("add-post", add_new_post, name="new-post"),
    path("delete/<int:post_id>", delete_post, name="delete-post"),
    path("update/<int:post_id>", update_post, name="update-post"),
    path('add-comment/', add_comment, name="add-comment")
]
