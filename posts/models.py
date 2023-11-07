from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from datetime import datetime
from user.models import Profile
from abstract.abstract import BaseModel


class Post(BaseModel):
    content = models.TextField()
    image = models.ImageField(upload_to="posts", null=True, blank=True, validators=[
                              FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='posts')
    liked = models.ManyToManyField(Profile, related_name='likes', default=None)

    def __str__(self) -> str:
        return f"{self.user.username} has created post on {datetime.strftime(self.updated, '%a,%d %b, %Y %I:%M:%S %p')}"

    class Meta:
        ordering = ('-updated',)

    @property
    def get_all_comments(self):
        return self.comments.all()

    @property
    def get_comments_count(self):
        return self.comments.count()

    @property
    def get_all_likes(self):
        return self.likes.all()

    @property
    def get_likes_count(self):
        return self.likes.count()


class Like(BaseModel):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=False)

    class Meta:
        ordering = ('-updated',)

    def __str__(self) -> str:
        return f'{self.user.username} liked post {self.post.pk}'
