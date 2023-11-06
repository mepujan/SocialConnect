from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(BaseModel):
    status = models.TextField()
    image = models.ImageField(upload_to="posts", null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.username} has created post on {datetime.strftime(self.updated, '%a,%d %b, %Y %I:%M:%S %p')}"

    class Meta:
        ordering = ('-updated',)

    @property
    def get_all_comments(self):
        return self.comments.all()

    @property
    def get_all_likes(self):
        return self.likes.all()


class Like(BaseModel):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.user.username} liked post {self.post.pk}'
