from django.db import models
from posts.models import Post
from django.contrib.auth.models import User
from abstract.abstract import BaseModel
from user.models import Profile


class Comment(BaseModel):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    comment = models.CharField(max_length=400)

    class Meta:
        ordering = ('-updated',)

    def __str__(self):
        return f"{self.user.email} commented on post {self.pk}"
