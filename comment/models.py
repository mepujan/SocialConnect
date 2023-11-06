from django.db import models
from posts.models import Post, BaseModel
from django.contrib.auth.models import User


class Comment(BaseModel):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=400)

    def __str__(self):
        return f"{self.user.email} commented on post {self.pk}"
