from django.urls import path
from .views import get_all_posts
app_name = "posts"

urlpatterns = [
    path("", get_all_posts, name='posts')
]
